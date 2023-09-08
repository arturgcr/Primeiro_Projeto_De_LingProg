from flask import Flask, render_template, request
import os
from datetime import datetime
import webbrowser
import threading
from geradorDePdf import *

"""
/projeto
  main.py
  /templates
    main.html
  /static
    main.css
    main.js

w3school.com

falta:
  - tratamento de erro (cadastro, login)
  - html bem desenvolvido
  - css bem desenvolvido
  - codigo documentado
  - divisão adequada do código
  - pop-up de aviso de erro
  - tela de opção de exibir escrever carta ou gerar pdf
  - gerar pdf
  - txt de envios
  - txt de recebidos

"""
#GeradorPDF.gerar_pdf("bancoDeLogins/logins.txt", "logings.pdf")

app = Flask(__name__)

@app.route("/")
def hello_agendeca(): 
  return render_template("telaDeLogin.html")

# Cria a tela de login
@app.route("/login", methods=["POST"])
def login():
    global nome

    if request.method == "POST":
        if 'cadastro' in request.form:
            cadastro = request.form['cadastro']
            if cadastro == 'cadastro':
                return render_template("telaDeCadastro.html")

        nome = request.form.get("nome")
        senha = request.form.get("senha")

        with open("bancoDeLogins/logins.txt", 'r') as arquivo:
            lista_logins = arquivo.readlines()

            for linha in lista_logins:
                linha = linha.strip()
                lista_info = eval(linha)
                if nome == lista_info[0] and senha == lista_info[1]:
                    return render_template("escreverCarta.html")

        return render_template("telaDeLogin.html")

# Cria a tela de cadastro
@app.route("/menu", methods = ["POST"])
def menu():
  pass
# Cria a tela de cadastro
@app.route("/cadastro", methods = ["POST"])
def cadastro():
  nomeCadastro = request.form.get("nome")
  senha = request.form.get("senha")
  confirmarSenha = request.form.get("senhaConfirmacao")
  usuario = []
  usuario.append(nomeCadastro)
  usuario.append(senha)
  caminho_pasta_usuario = "bancoDeCartas/" + str(nomeCadastro)
  
  if request.method == 'POST':
      if 'botao' in request.form:
        confirmar = request.form['botao']
        if confirmar == 'Confirmar':
          if(confirmarSenha == senha and len(senha) >= 5 and len(nomeCadastro) >= 4 and not os.path.exists(caminho_pasta_usuario)):
            with open("bancoDeLogins/logins.txt", 'a') as arquivo:
              arquivo.write("\n"+str(usuario))
              arquivo.close()
              os.makedirs(caminho_pasta_usuario)  
            with open(str(caminho_pasta_usuario) + "/" + str(nomeCadastro) +".txt", "a") as arquivo:
              arquivo.write("Historico de mensagens de " + str(nomeCadastro))
              arquivo.close()

              return render_template("telaDeLogin.html")
          else:
            return render_template("errou.html")
          
      if 'voltar' in request.form:
        voltar = request.form['voltar']
        if voltar == "Voltar":
           return render_template("telaDeLogin.html")

# Cria a tela de escrita da carta
@app.route('/escreverCarta', methods=["POST"])
def formulario():
    if request.method == 'POST':
        if 'botao' in request.form:
            enviar_carta = request.form['botao']
            if enviar_carta == 'enviar':
                seu_email = request.form.get("from")
                email_pessoa = request.form.get("to")
                data = request.form.get("date")
                mensagem = request.form.get("message")
                with open("bancoDeCartas/" + str(nome) + "/" + str(nome) +".txt", "a") as arquivo:
                  horaAtual = datetime.now()
                  arquivo.write(str("\n\n Data: " + data + "\n Destinatario: " + email_pessoa + "\n Mensagem: "+mensagem+ "\n Remetente: " + seu_email + "\n Horario de envio: "+str(horaAtual.strftime("%H:%M:%S"))))
                  arquivo.close()
          
    return render_template('telaDeLogin.html')


# Daqui pra baixo, tudo serve so pra gerar o site e abrir o seu navegador nele de forma automática
def iniciaSite():
    app.run()

if __name__ == '__main__':
    threadIniciaSite = threading.Thread(target=iniciaSite)
    threadIniciaSite.start()
    try:
      webbrowser.open("http://localhost:5000/")
    except:
      pass