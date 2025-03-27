import os
import zipfile
import pandas as pd
from tabula import read_pdf


def encontrar_arquivo_pdf(nome_arquivo):
    """Verifica se o arquivo PDF existe no diretório."""
    if os.path.exists(nome_arquivo):
        return nome_arquivo
    return None


def extrair_dados_pdf(nome_arquivo_pdf):
    """Extrai tabelas do PDF."""
    print(f"Extraindo dados do arquivo: {nome_arquivo_pdf}...")
    
    try:
        tabelas = read_pdf(nome_arquivo_pdf, pages="all", multiple_tables=True)
        if not tabelas:
            print("Nenhuma tabela encontrada no PDF.")
            return None
        
        df_completo = pd.concat(tabelas, ignore_index=True).dropna(how="all")
        return df_completo

    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None


def tratar_dados(df):
    """Substitui abreviações por descrições completas."""
    print("Processando dados...")

    mapeamento = {
        "OD": "Odontológico",
        "AMB": "Ambulatorial"
    }
    
    return df.replace(mapeamento)


def salvar_e_compactar(df, seu_nome):
    """Salva os dados tratados em CSV e compacta em um ZIP."""
    nome_csv = f"Rol_Procedimentos_{seu_nome}.csv"
    nome_zip = f"Teste_{seu_nome}.zip"

    print(f"Salvando {nome_csv}...")
    df.to_csv(nome_csv, index=False, encoding="utf-8-sig")

    print(f"Criando {nome_zip}...")
    with zipfile.ZipFile(nome_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(nome_csv)

    print("Removendo CSV temporário...")
    os.remove(nome_csv)

    print(f"Processo concluído! Arquivo gerado: {nome_zip}")

def transformar_dados(seu_nome="Kamila"):
    nome_arquivo_pdf = "Anexo I.pdf"
    
    if not (arquivo := encontrar_arquivo_pdf(nome_arquivo_pdf)):  # Sem colchetes
        print("Nenhum arquivo PDF encontrado.")
        return

    df = extrair_dados_pdf(arquivo)
    if df is None or df.empty:
        print("Nenhuma tabela válida foi extraída do PDF.")
        return

    df_tratado = tratar_dados(df)
    salvar_e_compactar(df_tratado, seu_nome)


if __name__ == "__main__":
    transformar_dados()
