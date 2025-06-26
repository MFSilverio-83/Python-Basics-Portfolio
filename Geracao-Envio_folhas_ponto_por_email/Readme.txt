✨ Folhas de Ponto Automatizadas ✨

Este projeto automatiza um processo manual e repetitivo: a separação e envio de espelhos de ponto por e-mail. Desenvolvido em Python, ele lê um único arquivo PDF contendo as folhas de ponto de todos os funcionários, separa cada uma em um arquivo individual e as envia para o e-mail de cada colaborador, tornando o RH mais eficiente e produtivo.

🚀 Funcionalidades Principais:

Leitura de PDF em Massa: 📖 Processa um arquivo PDF único com múltiplas páginas, cada uma representando um espelho de ponto.

Separação Inteligente: ✂️ Extrai o nome de cada funcionário da página do PDF e gera um arquivo PDF individual para cada um.

Envio de E-mail Automatizado: 📧 Envia cada folha de ponto para o e-mail correspondente do funcionário, lido a partir de uma planilha Excel.

Gestão de Credenciais Segura: 🔒 Utiliza variáveis de ambiente (.env) para armazenar o e-mail e a senha, garantindo que suas credenciais não sejam expostas no código-fonte.

Tratamento de Erros Robusto: ✅ Lida com arquivos não encontrados, erros de autenticação de e-mail e funcionários sem e-mail na planilha, garantindo que o programa continue funcionando sem interrupções inesperadas.

Feedback em Tempo Real: ⏱️ Exibe mensagens de progresso no terminal, informando o usuário sobre cada etapa do processo (leitura, geração e envio).

⚙️ Como Utilizar:

Para colocar a automação em prática, siga estes passos simples.

1. Pré-requisitos
Certifique-se de ter o Python 3.x instalado. Instale as bibliotecas necessárias usando pip:

pip install PyPDF2 openpyxl python-dotenv

2. Configuração dos Arquivos
Crie ou coloque os seguintes arquivos na pasta do seu projeto:

- espelho de ponto.pdf: O arquivo PDF principal contendo todos os espelhos de ponto.

- Lista_emails.xlsx: Uma planilha Excel com duas colunas:
Coluna A: Nome do funcionário (exatamente como aparece no PDF).
Coluna B: Endereço de e-mail do funcionário.

3. Configuração de Variáveis de Ambiente
Para manter suas credenciais seguras, você deve criar um arquivo .env.
- Crie um arquivo na raiz do seu projeto chamado .env.
Adicione as seguintes linhas, substituindo os valores pelos seus dados:

# .env
EMAIL_REMETENTE=seu-email-de-envio@dominio.com
SENHA_EMAIL=sua-senha-do-email

⚠️ ATENÇÃO: Adicione o arquivo .env ao seu .gitignore para garantir que ele nunca seja enviado para o GitHub!

4. Execução do Script
Execute o script a partir do seu terminal:

python seu_script_principal.py

O programa irá então executar todas as etapas automaticamente, fornecendo feedback em cada passo:

Exemplo saída:

Lendo o arquivo PDF principal: espelho de ponto.pdf
Total de 10 páginas encontradas.
Processando página 10/10...
==============================
✅ 10 folhas de ponto geradas com sucesso.
==============================

Lendo a lista de e-mails do arquivo: Lista_emails.xlsx
✅ 8 e-mails encontrados na planilha.

Conectando ao servidor de e-mail...
✅ Conexão e login bem-sucedidos!

Iniciando o envio de e-mails...
📧 E-mail enviado com sucesso para João da Silva (joao.silva@empresa.com).
[AVISO] E-mail não encontrado para 'Maria Souza'. Pulando.
...
========================================
🎉 Todos os e-mails foram enviados com sucesso!
========================================

🏗️ Estrutura do Projeto
O código é modular e segue boas práticas de programação, o que facilita a leitura e a manutenção:

main(): Orquestra o fluxo principal do programa.

gerar_folhas_separadas(): Lê o PDF mestre e cria os PDFs individuais.

ler_lista_emails(): Lê a planilha Excel e retorna os dados de e-mail em um dicionário.

enviar_folhas_por_email(): Lida com a conexão SMTP e o envio de e-mails.

extrair_nome_do_pdf(): Função auxiliar para extrair o nome do funcionário de cada página.

🤝 Contribuições
Sinta-se à vontade para abrir issues com sugestões ou problemas, ou enviar pull requests com melhorias. Toda contribuição é bem-vinda!