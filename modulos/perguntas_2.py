import numpy as np
import pandas as pd

df = pd.read_excel("A1 LP.xlsx")
df.drop(["Unnamed: 0", "Artista"], axis=1, inplace=True)
df.sort_values(by = "Album", inplace = True)
df.set_index(["Album", "Música"], inplace = True)

pd.set_option("display.max_rows", 500)
pd.set_option("display.min_rows", 500)


def palavras_comuns_titalbum(df):
    musicas = df.index.values
    lis = np.array()
    for album in musicas:
        lis[album[0]] = ""
        #print("\nAlbum: \n", album[0])
        #print("\nLis: \n", lis)
    print("\nlis\n\n", lis)
    uni = {}
    for palavra in lis.keys:
        uni[palavra] = lis.count(palavra)
    uni = pd.Series(uni)
    uni.sort_values(ascending=False, inplace = True)
    return uni


def palavras_comuns_titmusicas(df):
    musicas = df.index.values
    lis = []
    for musica in musicas:
        lis += musica[1].split()
        print(type(musica[1].split()))
    uni = {}
    for palavra in lis:
        uni[palavra] = lis.count(palavra)
    uni = pd.Series(uni)
    uni.sort_values(ascending=False, inplace = True)
    return uni




print("-"*60)
print(palavras_comuns_titmusicas(df))

print("-"*60)
#print(palavras_comuns_titalbum(df))


# indices = ["Shape of You", "Perfect", "Castle on the Hill", "Thinking Out Loud"]
# colunas = ["Album", "Tempo", "Lyric"]
# dados = [["÷ (Divide)", "03:53", "the club isn't " ], ["÷ (Divide)", "04:23", "este cantor lyrics"], ["÷ (Divide)", "04:27", "teste do teste"], ["× (Multiply)", "02:59", "letra teste"]]
         
# df = pd.DataFrame(dados,index = indices, columns = colunas)