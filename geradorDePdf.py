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
                for linha in arquivo_txt:
                    c.drawString(100, 750, linha.strip())
                    c.showPage()
                
                # Fecha o objeto Canvas, o que gera o PDF final
                c.save()
                print(f'PDF gerado com sucesso: {nome_arquivo_pdf}')
        except FileNotFoundError:
            print(f'Arquivo de texto não encontrado: {nome_arquivo_txt}')
        except Exception as e:
            print(f'Ocorreu um erro ao gerar o PDF: {str(e)}')
