import pandas as pd

# Músicas com mais e menos palavras por álbum
def i (df,mais_ou_menos = "+"):
    df_por_album = df.groupby(["Album"])
    if mais_ou_menos == "+":
        mais_palavras_album = df_por_album["Letra"].transform(max) == df["Letra"]
        mais_palavras_album = df[mais_palavras_album]
        return mais_palavras_album
    elif mais_ou_menos == "-":
        menos_palvras_album = df_por_album["Letra"].transform(min) == df["Letra"]
        menos_palvras_album = df[menos_palvras_album]
        return menos_palvras_album


# Música com mais e menos palavras
def ii(df, mais_ou_menos = "+"):
    if mais_ou_menos == "+":
        mais_palavras = df[df["Letra"]==df["Letra"].max()]
        return mais_palavras
    elif mais_ou_menos == "-":
        menos_palavras = df[df["Letra"]==df["Letra"].min()]
        return menos_palavras


# Há relação entre a quantidade de palavras e a duração das músicas?

#Função para as músicas mais curtas e longas por álbum
def iii(df, mais_ou_menos = "+"):
    mais_palavras_album = i(df, "+") 
    menos_palvras_album = i(df, "-")
    df_por_album = df.groupby(["Album"])
    mais_longas_album = df_por_album["Tempo"].transform(max) == df["Tempo"]
    mais_longas_album = df[mais_longas_album]

    menos_longas_album = df_por_album["Tempo"].transform(min) == df["Tempo"]
    menos_longas_album = df[menos_longas_album]

    #Ver se os dtaframes formados pelas funções acima possuem valores iguais
    if mais_ou_menos == "+":
        maior_tempo_popularidade = pd.merge(mais_longas_album, mais_palavras_album, how='inner')
        return maior_tempo_popularidade
    elif mais_ou_menos == "-":
        menor_tempo_popularidade = pd.merge(menos_longas_album, menos_palvras_album, how='inner')
        return menor_tempo_popularidade

# Resposta: É possível ver que os dois fatores não possuem muita relação, 
#pois as duas funções só retornaram uma música cada.

if __name__ == "__main__":
    df = pd.read_excel("A1 LP.xlsx")
    print("Tudo certo")