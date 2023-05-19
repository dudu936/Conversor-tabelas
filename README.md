# Conversão de PDF para Excel
Este código em Python permite converter tabelas de um arquivo PDF para um arquivo Excel (.xlsx) usando as bibliotecas tabula, pandas e openpyxl. O código contém funções para remover linhas e colunas indesejadas, separar colunas com base em um separador específico e criar um arquivo Excel a partir das tabelas extraídas.

Pré-requisitos
Certifique-se de ter as seguintes bibliotecas instaladas:
pandas
tabula
openpyxl

Você pode instalá-las usando o pip:
pip install pandas tabula-py openpyxl

Como usar
Coloque o arquivo PDF que contém as tabelas na mesma pasta que o arquivo Python.
Abra o arquivo Python e altere os parâmetros conforme necessário:
pdf_file: Nome do arquivo PDF a ser convertido (padrão: "relatorio.pdf").
xlsx_file: Nome do arquivo Excel de saída (padrão: "relatorio.xlsx").
index: Índice da linha que contém os nomes das colunas (padrão: 0).
print_display: Imprimir as tabelas no console (padrão: False).
ignore: Ignorar os parâmetros columns, rows e separator e converter todas as tabelas sem modificação (padrão: False).
columns: Lista de nomes de colunas a serem removidas (padrão: []).
rows: Lista de valores em células a serem removidas (padrão: []).
separator: Lista de nomes de colunas a serem separadas com base em um separador específico (padrão: []).
Execute o arquivo Python.

O arquivo Excel de saída será criado na mesma pasta com o nome especificado em xlsx_file.

Observações
Certifique-se de que o arquivo PDF esteja bem formatado e as tabelas estejam claramente definidas.
As tabelas serão extraídas a partir de todas as páginas do arquivo PDF. Se você deseja extrair tabelas de páginas específicas, modifique o parâmetro pages na chamada da função pdf.read_pdf().
Ao usar os parâmetros columns, rows e separator, certifique-se de fornecer os valores corretos para remover as linhas e colunas indesejadas ou separar as colunas conforme necessário.
Se você encontrar problemas na conversão, verifique se todas as dependências estão instaladas corretamente e se o arquivo PDF está acessível pelo código.

Limitações
Este código pode não funcionar corretamente se as tabelas no arquivo PDF tiverem uma formatação complexa ou se estiverem muito diferentes em termos de estrutura.
O código atual trata cada tabela no arquivo PDF separadamente. Se o arquivo contiver várias tabelas com estruturas diferentes, pode ser necessário modificar o código para lidar com cada tabela de forma personalizada.
Como o código utiliza a biblioteca tabula para extrair as tabelas do arquivo PDF, ele depende da capacidade do tabula em reconhecer corretamente as tabelas e convertê-las em objetos DataFrame do pandas. Portanto, a precisão da extração de tabelas
