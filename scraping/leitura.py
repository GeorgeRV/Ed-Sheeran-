import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap_albuns(url):
    id_tabela = "tracklist"

    resposta = requests.get(url)
    pagina = BeautifulSoup(resposta.content, "html.parser")

    tabela = pagina.find_all("table", attrs = {"class" : id_tabela})

    table = pd.read_html(str(tabela))

    allas = pd.DataFrame({"Title": [], "Length": []})
    print(len(table))
    for versoes in table: 
        tempo = versoes[["Title", "Length"]].copy()
        tempo.set_index("Title", inplace = True)
        try:
            allas = allas.merge(tempo, how = "outer", on = ["Title", "Length"])
        except:
            print("deu ruim")
        print("entao vamos \n\n",allas)
    #allas.drop("Total length:", inplace = True)
    return allas


url = "https://en.wikipedia.org/wiki/%2B_(album)"
print("\n\n\nBagulho:", scrap_albuns(url))

url = "https://en.wikipedia.org/wiki/X_(Ed_Sheeran_album)"
#print("\n\n\nBagulho:", scrap_albuns(url))



# page = requests.get("https://en.wikipedia.org/wiki/%2B_(album)")

# #print(page.content)

# pagina = BeautifulSoup(page.content, "html.parser")

# atributos = {"class":"tracklist-length"}
# respostas = pagina.find_all("td", attrs = atributos)

# tempo = []
# for resposta in respostas:
#     tempo.append(resposta.get_text())

# print(tempo)

# pagina = bs(page.text, "html.parser")
# print(pagina)

# # import pandas as pd

# # df_edsh = pd.read_csv('A1 LP.xlsx')