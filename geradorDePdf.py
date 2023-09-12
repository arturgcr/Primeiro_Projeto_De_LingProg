from reportlab.pdfgen import canvas


class GeradorPDF: 
    @staticmethod   
    def gerar_pdf(nome_arquivo_txt, nome_arquivo_pdf):
        # Abre o arquivo de texto para leitura
        try:
            with open(nome_arquivo_txt, 'r', encoding='utf-8') as arquivo_txt:
                # Cria um objeto Canvas para gerar o PDF
                c = canvas.Canvas(nome_arquivo_pdf)
                
                # Lê o conteúdo do arquivo de texto e escreve no PDF
                contador = 750
                for linha in arquivo_txt:
                    c.drawString(100, contador, linha.strip())
                    contador -= 20
                    if contador <= 50:
                        contador = 750
                        c.showPage()
                
                # Fecha o objeto Canvas, o que gera o PDF final
                c.save()
                print("PDF gerado com sucesso: " + str(nome_arquivo_pdf))
        except FileNotFoundError:
            print("Arquivo de texto não encontrado: " + str(nome_arquivo_txt))
        except Exception as e:
            print("Ocorreu um erro ao gerar o PDF: " + str(e))
