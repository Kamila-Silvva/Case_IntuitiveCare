# Scraping ANS e Compactação dos Anexos

Este projeto realiza o web scraping de uma página da ANS (Agência Nacional de Saúde Suplementar), baixa os arquivos PDF dos anexos "Anexo I" e "Anexo II" e os compacta em um arquivo ZIP. A seguir, há uma explicação detalhada sobre o funcionamento do código.

## Funcionalidade

O código realiza as seguintes tarefas:

- **Busca por Links de Anexos**: Acessa o site da ANS e encontra os links para os anexos "Anexo I" e "Anexo II".
- **Download dos Arquivos**: Se os arquivos PDF ainda não estiverem presentes no diretório local, ele realiza o download e salva os arquivos na pasta `anexos_ans`.
- **Compactação dos Arquivos**: Após o download dos arquivos PDF, o código cria um arquivo ZIP contendo os dois anexos, caso ainda não tenha sido gerado.

## Como Funciona

### Variáveis de Configuração:
- **URL**: Endereço da página da ANS.
- **PASTA_DOWNLOADS**: Diretório onde os arquivos PDF serão salvos.
- **NOME_ZIP**: Nome do arquivo ZIP que será criado.
- **ANEXOS_PDF**: Lista contendo os nomes dos anexos que o código buscará.

### Funções:
- **buscar_links()**: Faz o web scraping para encontrar os links dos anexos na página da ANS.
- **baixar_pdfs()**: Realiza o download dos PDFs dos anexos encontrados, mas verifica se o arquivo já existe para evitar downloads desnecessários.
- **criar_zip()**: Compacta os arquivos PDF em um arquivo ZIP, se ainda não existir.
- **main()**: Controla o fluxo do programa, chamando as funções e garantindo que o processo seja realizado na ordem correta.

## Requisitos

- **Python 3.x**

### Bibliotecas:
- **requests**: Para realizar as requisições HTTP.
- **BeautifulSoup**: Para parsear o HTML e fazer o web scraping.
- **zipfile**: Para compactar os arquivos PDF.

Para instalar as dependências necessárias, basta executar:

```bash
pip install requests beautifulsoup4 
```

## Como Usar

Clone o repositório ou baixe o arquivo.

Instale as dependências executando o comando de instalação:

```bash
pip install requests beautifulsoup4
```
Execute o script:

```bash
python nome_do_arquivo.py
```

## Observações

- O código verifica se o arquivo ZIP já foi criado anteriormente, então ele só irá gerar o arquivo ZIP uma vez.
- O diretório anexos_ans será criado automaticamente, caso ele ainda não exista no seu sistema.

# Conclusão

Este projeto tem como objetivo facilitar o acesso e organização dos documentos da ANS. Ao automatizar o processo de coleta e compactação dos anexos, ele permite que o usuário obtenha rapidamente os documentos necessários, sem a necessidade de baixar e organizar manualmente cada anexo. Isso torna o processo mais eficiente e menos propenso a erros.

