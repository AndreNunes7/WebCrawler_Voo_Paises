import requests
from bs4 import BeautifulSoup

url = "http://voos.infraero.gov.br/hstvoos/RelatorioPortal.aspx"


# requisiçao
def requisicao(url):
    try:
        busca = requests.get(url)
        if busca.status_code == 200:
            return busca.text
        else:
            print("Erro na requisição")
    except Exception as error:
        print("Erro!!")
        print(error)


# parsing

def parsing(url_p):
    try: 
        soup = BeautifulSoup(url_p, "html.parser")
        return soup
    except Exception as error:
        print("Erro no parsing")
        print(error)

    

# pegando os links

def buscar(link):
    cidades = link.find('div')
    cidade = cidades.find_all("tr")
    nomes_cidade = []
    num_de_voos = []

    for linha in cidade[1:]:
        colunas = linha.find_all("td")
        nome_cidade = colunas[0].get_text()
        nomes_cidade.append(nome_cidade)
        
        
        num_voo = colunas[1].get_text()
        num_de_voos.append(num_voo)
        
    

    max_length = max(len(nome) for nome in nomes_cidade)  # Encontra o comprimento máximo dos nomes

    for cidade, num_voo in zip(nomes_cidade, num_de_voos):
        spaces = " " * (max_length - len(cidade) + 2)  # Adicione espaços para alinhar os números
        print(f"{cidade}:{spaces}{num_voo} N° Voos")



    #print(cidades.prettify())
    # cidade_pai = cidades.find_all('td')
    # city = []
    # for cidade in cidades:
        
    #     city.append(cidade)
        
   




resposta = requisicao(url)
if resposta:
    soup = parsing(resposta)
    if soup:
        print("   -----------------------------------")
        print("      Consulta de voos por cidades: ")
        print("   -----------------------------------")
        links = buscar(soup)
        
        
            


    

