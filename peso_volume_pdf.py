import re
from PyPDF2 import PdfReader
import os

def extrair_dados(pdf_path):
    # Lê o conteúdo do PDF
    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        texto = ''
        for page in reader.pages:
            texto += page.extract_text()

    # Exibe o texto completo extraído do PDF para verificar o conteúdo
    # print(f"\n--- Texto extraído do PDF ({pdf_path}) ---\n{texto}\n")

    # Ajuste a expressão regular para capturar o número associado a "ESPECIE"
    especie_match = re.search(r"(\d+)\s*ESPECIE", texto, re.IGNORECASE)
    if especie_match:
        especie = int(especie_match.group(1))  # Captura o número e converte para inteiro
        print(f"Valor associado a ESPÉCIE encontrado: {especie}")
    else:
        print(f"Valor de ESPÉCIE não encontrado no PDF: {pdf_path}")
        especie = 0

    # Ajuste a expressão regular para capturar o valor após "PESO LIQUIDO"
    peso_liquido_match = re.search(r"PESO LIQUIDO\s*([\d,\.]+)", texto, re.IGNORECASE)
    if peso_liquido_match:
        peso_liquido = float(peso_liquido_match.group(1).replace(',', '.'))  # Captura o peso e converte para float
        print(f"Peso Líquido encontrado: {peso_liquido} kg")
    else:
        print(f"Peso Líquido não encontrado no PDF: {pdf_path}")
        peso_liquido = 0

    return especie, peso_liquido

def processar_pdfs(pasta):
    especie_total = 0
    peso_liquido_total = 0

    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.pdf'):
            pdf_path = os.path.join(pasta, arquivo)
            print(f"\nProcessando arquivo: {pdf_path}")
            especie, peso_liquido = extrair_dados(pdf_path)
            especie_total += especie
            peso_liquido_total += peso_liquido

    return especie_total, peso_liquido_total

if __name__ == "__main__":
    pasta_pdf = r"C:\Users\itinerario\Desktop\pratica"
    print(f"Iniciando o script...\nProcessando arquivos na pasta: {pasta_pdf}")
    
    if os.path.exists(pasta_pdf):
        print("Pasta encontrada, iniciando a leitura dos PDFs...")
        especie_total_geral, peso_liquido_total_geral = processar_pdfs(pasta_pdf)
        print(f"\nValor Total de ESPÉCIE: {especie_total_geral}")
        print(f"Peso Líquido Total: {peso_liquido_total_geral} kg")
    else:
        print("Pasta não encontrada. Verifique o caminho e tente novamente.")
