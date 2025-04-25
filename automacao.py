#automação de envio de emails

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def enviar_email():
#     remetente = "h96352828@gmail.com"
#     senha = "kfad tphx hbke rgoq"
#     destinatario = "hs996352828@gmail.com"
#     assunto = "Teste de envio de email"
#     corpo = "este é um email de teste"

#     mensagem = MIMEMultipart()
#     mensagem["From"] = remetente
#     mensagem["To"] = destinatario
#     mensagem["Subject"] = assunto
#     mensagem.attach(MIMEText(corpo, "plain"))

#     servidor = smtplib.SMTP("smtp.gmail.com", 587)
#     servidor.starttls()
#     servidor.login(remetente, senha)
#     servidor.sendmail(remetente, destinatario, mensagem.as_string())
#     servidor.quit()
#     print("email enviado com sucesso")

# enviar_email()

# automacao de arquivos
# import os

# def organizar_arquivos():
#     pasta = "./arquivos"
#     if not os.path.exists(pasta):
#        os.makedirs(pasta)
#     arquivos_pasta_atual = os.listdir(".")
#     for arquivo in arquivos_pasta_atual:
#         if ".txt" in arquivo:
#             os.rename(arquivo, f"{pasta}/{arquivo}")
#     print("arquivos organizados com sucesso")

# organizar_arquivos()

# automatização no excel
# import openpyxl

# def atualizar_planilha():
#     nome = input("digite o nome: ")
#     idade = int(input("digite a idade: "))
#     profissao = input("digite a profissao: ")
#     workbook = openpyxl.load_workbook("dados.xlsx")
#     aba = workbook.active
#     aba.append([nome, idade, profissao])
#     workbook.save("dados.xlsx")
#     print("planilha atualizada com sucesso")
# atualizar_planilha()

# automatização de web scraping
from bs4 import BeautifulSoup
import requests

def extrair_informacoes_site():
    url = "https://www.nationalgeographic.com/pages/topic/latest-stories"
    headers = {"User-Agent":"Mozilla/5.0"}
    requisicao = requests.get(url, headers=headers)

    if requisicao.status_code == 200:
        pagina = BeautifulSoup(requisicao.text, "html.parser")
        titulos = pagina.find_all(class_="sr-only")
        for titulo in titulos:
            print(titulo.text)

extrair_informacoes_site()
