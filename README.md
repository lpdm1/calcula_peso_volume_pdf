# Extração de Dados de PDFs

Este projeto contém um script em Python para extrair informações específicas de arquivos PDF. O script busca por valores associados a "ESPÉCIE" e "PESO LIQUIDO" em documentos PDF e calcula o total desses valores a partir de múltiplos arquivos PDF em uma pasta.

## Funcionalidade

O script realiza as seguintes tarefas:
1. **Extrair Dados de PDFs**: Abre e lê o conteúdo de arquivos PDF.
2. **Capturar Valores**:
   - **ESPÉCIE**: Captura o número imediatamente antes da palavra "ESPECIE".
   - **PESO LIQUIDO**: Captura o valor numérico após a frase "PESO LIQUIDO".
3. **Processar Vários PDFs**: Itera através de todos os arquivos PDF em uma pasta especificada, acumulando os totais dos valores encontrados.

## Requisitos

- Python 3.6 ou superior
- Bibliotecas Python:
  - `PyPDF2`
  - `re` (incluída com Python)

Você pode instalar as bibliotecas necessárias usando `pip`:

```bash
pip install PyPDF2
```

## Como Usar
1. Clone o Repositório:
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO
```
2. Configurar o Caminho da Pasta:
Abra o arquivo script.py e ajuste o caminho da pasta pasta_pdf para o diretório onde seus arquivos PDF estão localizados.
```python
pasta_pdf = r"C:\Users\itinerario\Desktop\pratica"
```
Executar o Script:
```bash
python script.py
```
O script processará todos os arquivos PDF na pasta especificada e exibirá o valor total associado a "ESPÉCIE" e o peso líquido total.

## Exemplo de Saída
```plaintext
Iniciando o script...
Processando arquivos na pasta: C:\Users\itinerario\Desktop\pratica

Processando arquivo: C:\Users\itinerario\Desktop\pratica\exemplo.pdf
Valor associado a ESPÉCIE encontrado: 1
Peso Líquido encontrado: 0.23 kg

Valor Total de ESPÉCIE: 1
Peso Líquido Total: 0.23 kg
```
## Detalhes do Código
```extrair_dados(pdf_path)```: Lê o conteúdo do PDF e usa expressões regulares para extrair o valor de "ESPÉCIE" e "PESO LIQUIDO".

```processar_pdfs(pasta):``` Itera por todos os arquivos PDF na pasta fornecida e acumula os totais encontrados.

**Main Block:** Configura o caminho da pasta e chama as funções para processar os PDFs e exibir os resultados.


## Contribuições
Contribuições são bem-vindas! Se você encontrar um bug ou quiser adicionar uma nova funcionalidade, sinta-se à vontade para abrir um "issue" ou enviar um "pull request".

## Licença
Este projeto é licenciado sob a MIT License.

```perl
### Notas Adicionais:
- **Substitua `SEU_USUARIO` e `SEU_REPOSITORIO`** no comando de clonagem pelo seu nome de usuário e o nome do repositório no GitHub.
- **Ajuste o caminho** da pasta conforme necessário para o seu ambiente.

Este README deve fornecer uma visão clara sobre o que o script faz, como usá-lo e como contribuir. Ajuste conforme necessário para atender às suas necessidades específicas.```
