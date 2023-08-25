# Consulta de Voos por Cidades

Este é um programa em Python que faz uma requisição a um site da Infraero para consultar informações sobre voos por cidades. Ele utiliza a biblioteca `requests` para fazer a requisição HTTP e a biblioteca `BeautifulSoup` para analisar o HTML da página e extrair as informações relevantes.

## Funcionamento

O programa realiza as seguintes etapas:

1. Faz uma requisição HTTP à URL fornecida usando a biblioteca `requests`.
2. Analisa o HTML da resposta usando a biblioteca `BeautifulSoup` para extrair as informações desejadas.
3. Imprime as informações formatadas na saída.

O código divide as tarefas em funções:

- `requisicao(url)`: Faz a requisição HTTP e retorna o conteúdo da página.
- `parsing(url_p)`: Analisa o conteúdo HTML e retorna um objeto `BeautifulSoup`.
- `buscar(link)`: Extrai informações sobre as cidades e o número de voos a partir do objeto `BeautifulSoup` e as imprime na saída.

## Como usar

1. Certifique-se de ter o Python instalado em sua máquina.

2. Instale as bibliotecas necessárias listadas no arquivo `requirements.txt`. Isso pode ser feito com o seguinte comando: pip install -r requirements.txt
   
3. Copie o código fornecido para um arquivo `.py`.

4. Execute o arquivo Python. O programa fará a consulta e exibirá as informações sobre voos por cidades.

## Observações

- Este código é um exemplo simples de como fazer uma requisição HTTP a um site, analisar o HTML e extrair informações específicas usando a biblioteca `BeautifulSoup`. Ele pode ser estendido e aprimorado para incluir mais funcionalidades ou manipular dados de forma mais complexa.

- O código não lida com possíveis erros de conexão ou problemas na página da web. Em um ambiente de produção, você deve adicionar tratamento de erros e verificações adicionais.

- Certifique-se de respeitar os termos de uso do site ao realizar scraping de dados.

- Lembre-se de que as versões das bibliotecas listadas no arquivo `requirements.txt` podem mudar com o tempo. Verifique as versões mais recentes das bibliotecas antes de instalá-las.


