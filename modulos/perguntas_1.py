import pandas as pd

#Músicas mais ouvidas e músicas menos ouvidas por Álbum
def i(df, mais_ou_menos = "+"):
    df_por_album = df.groupby(["Album"])

    if mais_ou_menos == "+":
        mais_ouvidas_album = df_por_album["Popularidade"].transform(max) == df["Popularidade"]
        mais_ouvidas_album = df[mais_ouvidas_album]
        return mais_ouvidas_album
    elif mais_ou_menos == "-":
        menos_ouvidas_album = df_por_album["Popularidade"].transform(min) == df["Popularidade"]
        menos_ouvidas_album = df[menos_ouvidas_album]
        return menos_ouvidas_album

#Músicas mais longas e músicas mais curtas por álbum
def ii(df, mais_ou_menos = "+"):
    df_por_album = df.groupby(["Album"])

    mais_longas_album = df_por_album["Tempo"].transform(max) == df["Tempo"]

    if mais_ou_menos == "+":
        mais_longas_album = df[mais_longas_album]
        return mais_longas_album
    elif mais_ou_menos == "-":
        menos_longas_album = df_por_album["Tempo"].transform(min) == df["Tempo"]
        menos_longas_album = df[menos_longas_album]
        return menos_longas_album

#Músicas mais ouvidas e músicas menos ouvidas
def iii(df):
    mais_ouvidas = df[df['Popularidade']==df['Popularidade'].max()]
    print("Mais ouvidas: \n", mais_ouvidas)

    menos_ouvidas = df[df['Popularidade']==df['Popularidade'].min()]
    print("Menos ouvidas: \n", menos_ouvidas)

#Músicas mais longas e músicas mais curta
def iv(df):
    mais_longas = df[df['Tempo']==df['Tempo'].max()]
    print("Mais longas: \n", mais_longas)

    menos_longas = df[df['Tempo']==df['Tempo'].min()]
    print("Menos longas: \n", menos_longas)

#Álbuns mais premiados
def v(df):
    mais_premiado = df[df["Prêmios"]==df["Prêmios"].max()]
    print("Álbum mais premiado: \n", mais_premiado)

# Existe alguma relação entre a duração da música e sua popularidade?
def vi(df):
    mais_longas_album = ii(df, "+")
    mais_ouvidas_album = i(df, "+")
    menos_longas_album = ii(df, "-")
    menos_ouvidas_album = i(df, "-") 
    maior_tempo_popularidade = pd.merge(mais_longas_album, mais_ouvidas_album, how='inner')
    print("Maior tempo e maior popularidade: \n", maior_tempo_popularidade)

    menor_tempo_popularidade = pd.merge(menos_longas_album, menos_ouvidas_album, how='inner')
    print("Menor tempo e menor popularidade: \n", menor_tempo_popularidade)

if __name__ == "__main__":
    df = pd.read_excel("A1 LP.xlsx")