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

# Inicializa o Flask
app = Flask(__name__)

# Rota da página inicial - tela de login
@app.route("/")
def tela_inicial():
    return render_template("telaDeLogin.html")

# Rota do login
@app.route("/login", methods=["POST"])
def login():
    # Verifica se o botão de cadastro foi apertado
    if 'cadastro' in request.form:
      return render_template("telaDeCadastro.html")

    # Define o nome como global para ser acessado por demais telas
    global nome
    # Obtém o nome e a senha dos campos de texto
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    # Abre o arquivo de logins no modo leitura para verificar senha e nome de usuario
    with open("bancoDeLogins/logins.txt", 'r') as arquivo:
        for linha in arquivo:
            # Avalia a linha como uma lista de informações
            lista_info = eval(linha.strip())
            # Verifica se o nome e a senha de usuario batem
            if nome == lista_info[0] and senha == lista_info[1]:
                # Redireciona para a página de escrever carta se as credenciais estiverem corretas
                return render_template("escreverCarta.html")

    # Redireciona de volta para a tela de login em caso de falha
    return render_template("telaDeLogin.html")

# Rota do cadastro
@app.route("/cadastro", methods=["POST"])
def cadastro():
    # Verifica se o botão de voltar para a tela de login foi apertado, retornando a aba login
    if 'voltar' in request.form:
      return render_template("telaDeLogin.html")

    # Obtém os dados dos campos de texto da tela de cadastro
    nomeCadastro = request.form.get("nome")
    senha = request.form.get("senha")
    confirmarSenha = request.form.get("senhaConfirmacao")
    # O tratamento lower foi feito pa padronizar os arquivos e facilitar a verificação de nomes repetidos
    caminho_pasta_usuario = "bancoDeCartas/" + str(nomeCadastro).lower()

    if request.method == 'POST':
        # Verifica se as condições para o cadastro são atendidas (senha de ter mais de 5 letras, nome mais de 4 e não ter sido cadastrado ainda)
        if confirmarSenha == senha and len(senha) >= 5 and len(nomeCadastro) >= 4 and not os.path.exists(caminho_pasta_usuario):
            # Adiciona as informações de login ao banco txt de logins
            with open("bancoDeLogins/logins.txt", 'a') as arquivo:
                arquivo.write("\n"+str([nomeCadastro, senha]))
                
            # Cria a pasta do usuário
            os.makedirs(caminho_pasta_usuario)
            # Cria o arquivo com o historico de envio do usuario
            with open(str(caminho_pasta_usuario)+"/historico_de_"+str(nomeCadastro)+".txt", "w") as arquivo_cartas:
                arquivo_cartas.write("Historico de mensagens de " + str(nomeCadastro) + ":")
            
            # Redireciona de volta para a tela de login
            return render_template("telaDeLogin.html")
    
    # Reseta a pagina em caso de erro
    return render_template("telaDeCadastro.html")

# Rota para a aba de escrever cartas
@app.route('/escreverCarta', methods=["POST"])
def escrever_carta():
    # Escreve o caminho
    caminho_carta = "bancoDeCartas/"+str(nome).lower()+"/historico_de_"+str(nome)+".txt"
    if request.method == 'POST':
        if 'gerar_pdf' in request.form:
            GeradorPDF.gerar_pdf(caminho_carta, "bancoDeCartas/"+str(nome).lower()+"/historico_de_"+str(nome)+".pdf")
            return render_template("escreverCarta.html")

        if 'botao' in request.form:
            # Obtém os dados do formulário para escrever uma carta
            seu_email = request.form.get("from")
            email_pessoa = request.form.get("to")
            data = request.form.get("date")
            mensagem = request.form.get("message")
            hora_atual = datetime.now().strftime("%H:%M:%S")

            # Faz uma lista dos arquivos que estão nas pasta do usuario
            arquivos_na_pasta = os.listdir("bancoDeCartas/"+str(nome).lower())
            contador = 0
            for verifica in range(len(arquivos_na_pasta)):
                if ".txt" in arquivos_na_pasta[verifica]:
                    contador += 1
            print(str(contador))
            # Cria o caminho para o arquivo com a enumerção de arquivos do usuario
            caminho_carta = "bancoDeCartas/"+str(nome).lower()+"/carta_"+str(contador)+"_de_"+str(nome)+".txt"

            # Escreve a carta no arquivo correspondente
            with open(caminho_carta, "a") as arquivo:
                # Escreve no histórico de envio do usuario
                arquivo.write("\n\nData: "+str(data)+"\nDestinatario: "+
                str(email_pessoa)+"\nMensagem: "+str(mensagem)+"\nRemetente: "+str(seu_email)+
                "\nHorario de envio: "+str(hora_atual))

            GeradorPDF.gerar_pdf(caminho_carta, "bancoDeCartas/"+str(nome).lower()+"/carta_"+str(contador)+"_de_"+str(nome)+".pdf")

            # Sobreescreve a variavel para usar outro caminho
            caminho_carta = "bancoDeCartas/"+str(nome).lower()+"/historico_de_"+str(nome)+".txt"
            # Escreve a carta no historico do usuario
            with open(caminho_carta, "a") as arquivo:
                # Escreve no histórico de envio do usuario
                arquivo.write("\n\nData: "+str(data)+"\nDestinatario: "+
                str(email_pessoa)+"\nMensagem: "+str(mensagem)+"\nRemetente: "+str(seu_email)+
                "\nHorario de envio: "+str(hora_atual))

                # Redireciona de volta para a tela de login
            return render_template('telaDeLogin.html')

# Função para iniciar o site
def inicia_site():
    app.run()

if __name__ == '__main__':
    # Inicia o site em uma thread separada
    threading.Thread(target=inicia_site).start()
    
    try:
        # Abre o navegador automaticamente na página local
        webbrowser.open("http://localhost:5000/")
    except Exception as e:
        print("Erro ao abrir o navegador: " + str(e))
