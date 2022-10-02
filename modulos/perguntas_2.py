import numpy as np
import pandas as pd

df = pd.read_excel("A1 LP.xlsx")
df.drop(["Unnamed: 0", "Artista", "Lyric"], axis=1, inplace=True)
df.sort_values(by = "Album", inplace = True)

#df.rename(columns = {"": "Nome"}, inplace=True)
df.set_index(["Album", "Música"], inplace = True)


pd.set_option("display.max_rows", 500)
pd.set_option("display.min_rows", 500)

musicas = df.index.values
lis = []
for musica in musicas:
    lis += musica[1].split()
uni = {}
for palavra in lis:
    uni[palavra] = lis.count(palavra)
uni = pd.Series(uni)

print(uni.sort_values(ascending=False))


# indices = ["Shape of You", "Perfect", "Castle on the Hill", "Thinking Out Loud"]
# colunas = ["Album", "Tempo", "Lyric"]
# dados = [["÷ (Divide)", "03:53", "the club isn't " ], ["÷ (Divide)", "04:23", "este cantor lyrics"], ["÷ (Divide)", "04:27", "teste do teste"], ["× (Multiply)", "02:59", "letra teste"]]
         
# df = pd.DataFrame(dados,index = indices, columns = colunas)