import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrap_albuns(url, id_tabela):
    
    resposta = requests.get(url)
    pagina = BeautifulSoup(resposta.content, "html.parser")
    tabela = pagina.find_all("table", attrs = {"class" : id_tabela})

    table = pd.read_html(str(tabela))
    allas = pd.DataFrame({"Title": [], "Length": []})
    print(len(table))
    for versoes in table: 

        tempo = versoes[["Title", "Length"]].copy()

        n = 0
        for titu in tempo["Title"]:
            #print(titu, titu[1:].find('"'))
            final = titu[1:].find('"')
            tempo["Title"][n] = titu[1:final+1]
            n += 1

        print("\n\nTempo sem o dropna\n",tempo, "\nEsse foi\n\n")
        tempo.dropna(inplace = True)
        print("tempo 12",tempo["Title"][12] == "")
        # try:
        #     tempo.drop("", inplace = True)
        # except:
        #     print("")
        print("\n\nTempo com o dropna\n",tempo, "\nEsse foi\n\n")
        tempo.set_index("Title", inplace = True)

        try:
            allas = allas.merge(tempo, how = "outer", on = ["Title", "Length"])
        except:
            print("deu ruim")
        #print("entao vamos \n\n",allas)
    #allas.drop("Total length:", inplace = True)
    return allas


url = "https://en.wikipedia.org/wiki/%2B_(album)"
id_tabela = "tracklist"
plus = scrap_albuns(url, id_tabela)
#print("\n\n\nBagulho:", plus, "\n\n")
lis = []
lis += plus["Title"][16]
#print(type(plus["Title"][16]), plus["Title"][16], lis)


url = "https://en.wikipedia.org/wiki/X_(Ed_Sheeran_album)"
#print("\n\n\nBagulho:", scrap_albuns(url, id_tabela))



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