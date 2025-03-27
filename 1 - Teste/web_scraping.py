import os
import requests
import zipfile
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Configuração inicial
URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PASTA_DOWNLOADS = "anexos_ans"
NOME_ZIP = "anexos_ans.zip"
ANEXOS_PDF = ["Anexo I", "Anexo II"]

# Criar pasta se não existir
if not os.path.exists(PASTA_DOWNLOADS):
    os.makedirs(PASTA_DOWNLOADS)

def buscar_links():
    """Acessa o site da ANS e procura os links dos anexos."""
    try:
        print("Conectando ao site da ANS...")
        resposta = requests.get(URL, timeout=10)
        resposta.raise_for_status()
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        links_encontrados = {}
        for link in soup.find_all('a', href=True):
            for anexo in ANEXOS_PDF:
                if anexo.lower() in link.get_text().lower():
                    links_encontrados[anexo] = urljoin(URL, link['href'])
        return links_encontrados
    except requests.exceptions.RequestException as erro:
        print(f"Erro ao acessar o site: {erro}")
        return {}

def baixar_pdfs(links):
    """Baixa os arquivos PDF se eles ainda não estiverem salvos."""
    for nome, url in links.items():
        caminho_arquivo = os.path.join(PASTA_DOWNLOADS, f"{nome}.pdf")
        if os.path.exists(caminho_arquivo):
            print(f"{nome}.pdf já foi baixado antes.")
            continue
        
        try:
            resposta = requests.get(url, stream=True, timeout=10)
            resposta.raise_for_status()
            with open(caminho_arquivo, 'wb') as arquivo:
                for chunk in resposta.iter_content(chunk_size=8192):
                    arquivo.write(chunk)
            print(f"Download finalizado: {nome}.pdf")
        except Exception as erro:
            print(f"Erro ao baixar {nome}: {erro}")

def criar_zip():
    """Cria um arquivo ZIP com os PDFs baixados, se ainda não existir."""
    if os.path.exists(NOME_ZIP):
        print("O arquivo ZIP já foi criado anteriormente.")
        return
    
    try:
        with zipfile.ZipFile(NOME_ZIP, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for arquivo in os.listdir(PASTA_DOWNLOADS):
                caminho_completo = os.path.join(PASTA_DOWNLOADS, arquivo)
                zipf.write(caminho_completo, os.path.basename(caminho_completo))
        print(f"ZIP criado: {NOME_ZIP}")
    except Exception as erro:
        print(f"Erro ao criar ZIP: {erro}")

def main():
    anexos = buscar_links()
    if not anexos:
        print("Nenhum anexo encontrado. Verifique a página manualmente.")
        return
    
    baixar_pdfs(anexos)
    criar_zip()
    print("Processo finalizado. Arquivos prontos.")

if __name__ == "__main__":
    main()