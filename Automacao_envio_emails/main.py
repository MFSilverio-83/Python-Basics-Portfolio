# Importações de bibliotecas
import smtplib
from email.message import EmailMessage
import mimetypes

# Dados do e-mail
remetente = 'mfsilverio2019@gmail.com'
destinatario = 'mfsilverio@ymail.com'
assunto = 'Teste - E-mail com anexo'
mensagem = '''
E-mail teste para envio de anexos.
'''
senha_app = 'bmud fwzy ifyc kttl'
anexo = './formulario.pdf'

# Criar email:
msg = EmailMessage()
msg['From'] = remetente
msg['To'] = destinatario
msg['Subject'] = assunto
msg.set_content(mensagem)

# Anexar arquivo: 
# >> O "_" abaixo indica uma variável que não será utilizada. <<
mime_type, _ = mimetypes.guess_type(anexo) # anexando arquivo
mime_type, mime_type_subtype = mime_type.split('/') # obtendo formato do arquivo

with open(anexo, 'rb') as arquivo:
    msg.add_attachment(arquivo.read(), maintype=mime_type, subtype=mime_type_subtype, filename=anexo)

# Enviando o e-mail:
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
    email.login(remetente, senha_app)
    email.send_message(msg)

print('Email enviado com sucesso')
