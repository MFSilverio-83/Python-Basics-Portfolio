# importação das bibliotecas que serão utilizadas.
import PyPDF2 as pdf
from pathlib import Path
import openpyxl
import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

# Constantes de configuração. O uso de constantes em MAIÚSCULAS facilita a manutenção do código.
ARQUIVO_PDF_GERAL = "espelho de ponto.pdf"
ARQUIVO_EXCEL = "Lista_emails.xlsx"
DIRETORIO_FOLHAS = "Folhas"
EMAIL_REMETENTE = os.getenv("EMAIL_REMETENTE")
SENHA_EMAIL = os.getenv("SENHA_EMAIL")
SERVIDOR_SMTP = "smtps.uol.com.br"
PORTA_SMTP = 587
ASSUNTO_EMAIL = "Sua Folha de Ponto"
MENSAGEM_EMAIL = "Olá, segue sua folha de ponto em anexo.\n\nAtenciosamente,\nGestão de Pessoas"

def extrair_nome_do_pdf(pagina):
    """
    Extrai o nome de uma página do PDF com base em marcadores de texto.
    Retorna o nome extraído ou None se não for encontrado.
    """
    try:
        texto_pagina = pagina.extract_text()
        # Buscando por marcadores de texto para extrair o nome.
        # Adicionei uma margem de segurança para a posição do nome.
        pos_nome = texto_pagina.find('Nome:') 
        pos_cracha = texto_pagina.find('Crachá:')
        
        # Se os marcadores forem encontrados, extrai e limpa o nome.
        if pos_nome != -1 and pos_cracha != -1:
            # Posição de início: após 'Nome:' + um espaço
            # Posição de fim: onde 'Crachá:' começa
            nome = texto_pagina[pos_nome + len('Nome:'):pos_cracha].strip()
            return nome
        else:
            print(f"[AVISO] Não foi possível encontrar 'Nome:' ou 'Crachá:' na página. Folha ignorada.")
            return None
    except Exception as e:
        print(f"[ERRO] Falha ao extrair texto da página: {e}")
        return None
    

def gerar_folhas_separadas():
    """
    Lê o PDF geral e gera um arquivo PDF separado para cada funcionário.
    """
    # Garante que o diretório de destino existe.
    Path(DIRETORIO_FOLHAS).mkdir(exist_ok=True)
    
    try:
        print(f"Lendo o arquivo PDF principal: {ARQUIVO_PDF_GERAL}")
        # Abre o arquivo em modo de leitura binária
        with open(ARQUIVO_PDF_GERAL, 'rb') as arquivo_principal:
            arquivo_pdf = pdf.PdfReader(arquivo_principal)
            num_paginas = len(arquivo_pdf.pages)
            print(f"Total de {num_paginas} páginas encontradas.")

            folhas_geradas = []
            for i, pagina in enumerate(arquivo_pdf.pages, 1):
                print(f"Processando página {i}/{num_paginas}...", end="\r") # Feedback visual
                nome_funcionario = extrair_nome_do_pdf(pagina)

                if nome_funcionario:
                    # Cria o nome do arquivo, removendo caracteres inválidos para nome de arquivo.
                    nome_arquivo_saida = f"{nome_funcionario.replace('/', '_').replace(' ', '_')}.pdf"
                    caminho_saida = Path(DIRETORIO_FOLHAS) / nome_arquivo_saida

                    arquivo_novo = pdf.PdfWriter()
                    arquivo_novo.add_page(pagina)

                    with caminho_saida.open(mode='wb') as arquivo_final:
                        arquivo_novo.write(arquivo_final)
                    
                    folhas_geradas.append(nome_funcionario)
            
            print("\n" + "="*30)
            print(f"✅ {len(folhas_geradas)} folhas de ponto geradas com sucesso.")
            print("="*30)
            return folhas_geradas

    except FileNotFoundError:
        print(f"\n[ERRO] O arquivo '{ARQUIVO_PDF_GERAL}' não foi encontrado. Verifique o caminho.")
        return []
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro inesperado durante a geração das folhas: {e}")
        return []


def ler_lista_emails():
    """
    Lê a planilha do Excel e retorna um dicionário de funcionários e e-mails.
    """
    try:
        print(f"\nLendo a lista de e-mails do arquivo: {ARQUIVO_EXCEL}")
        lendo_arquivo = openpyxl.load_workbook(ARQUIVO_EXCEL)
        linhas = lendo_arquivo.active
        
        # Cria um dicionário para armazenar os dados.
        emails = {linha[0]: linha[1] for linha in linhas.iter_rows(values_only=True) if linha[0] and linha[1]}
        
        print(f"✅ {len(emails)} e-mails encontrados na planilha.")
        return emails

    except FileNotFoundError:
        print(f"\n[ERRO] O arquivo '{ARQUIVO_EXCEL}' não foi encontrado. Verifique o caminho.")
        return {}
    except Exception as e:
        print(f"\n[ERRO] Falha ao ler a planilha Excel: {e}")
        return {}
    

def enviar_folhas_por_email(folhas_geradas, lista_emails_dict):
    """
    Conecta-se ao servidor SMTP e envia os e-mails com as folhas de ponto.
    """
    if not folhas_geradas or not lista_emails_dict:
        print("\n[AVISO] Não há folhas para enviar ou lista de e-mails vazia. Operação cancelada.")
        return
    
    print("\nConectando ao servidor de e-mail...")
    try:
        # Conecta e faz login no servidor SMTP uma única vez.
        with smtplib.SMTP(SERVIDOR_SMTP, PORTA_SMTP) as smtp_server:
            smtp_server.starttls() # Inicia a conexão TLS (criptografada).
            smtp_server.login(EMAIL_REMETENTE, SENHA_EMAIL)
            print("✅ Conexão e login bem-sucedidos!")
            
            print("\nIniciando o envio de e-mails...")
            # Itera sobre os funcionários para enviar os e-mails.
            for funcionario in folhas_geradas:
                email_destinatario = lista_emails_dict.get(funcionario)
                
                if not email_destinatario:
                    print(f"[AVISO] E-mail não encontrado para '{funcionario}'. Pulando.")
                    continue

                caminho_pdf_anexo = Path(DIRETORIO_FOLHAS) / f"{funcionario.replace(' ', '_')}.pdf"
                
                if not caminho_pdf_anexo.exists():
                    print(f"[AVISO] Arquivo de folha de ponto não encontrado para '{funcionario}'. Pulando.")
                    continue

                # Cria a mensagem de e-mail
                message = EmailMessage()
                message["Subject"] = ASSUNTO_EMAIL
                message["From"] = EMAIL_REMETENTE
                message["To"] = email_destinatario
                message.set_content(MENSAGEM_EMAIL)
                
                # Anexa o arquivo PDF
                with open(caminho_pdf_anexo, "rb") as pdf_file:
                    message.add_attachment(pdf_file.read(), maintype="application", subtype="pdf", filename=caminho_pdf_anexo.name)

                # Envia a mensagem
                smtp_server.send_message(message)
                print(f"📧 E-mail enviado com sucesso para {funcionario} ({email_destinatario}).")

            print("\n" + "="*40)
            print("🎉 Todos os e-mails foram enviados com sucesso!")
            print("="*40)

    except smtplib.SMTPAuthenticationError:
        print("\n[ERRO] Falha de autenticação. Verifique seu e-mail e senha.")
    except smtplib.SMTPConnectError:
        print("\n[ERRO] Falha ao conectar ao servidor SMTP. Verifique o servidor e a porta.")
    except Exception as e:
        print(f"\n[ERRO] Ocorreu um erro durante o envio: {e}")


def main():
    """
    Função principal que orquestra todo o processo.
    """
    # 1. Gera os arquivos PDF individuais
    folhas_geradas = gerar_folhas_separadas()

    # 2. Lê a lista de e-mails da planilha
    lista_emails_dict = ler_lista_emails()
    
    # 3. Envia os e-mails
    enviar_folhas_por_email(folhas_geradas, lista_emails_dict)

if __name__ == '__main__':
    main()
