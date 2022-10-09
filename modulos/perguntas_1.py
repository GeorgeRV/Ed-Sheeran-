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
def iii(df, mais_ou_menos = "+"):
    if mais_ou_menos == "+":
        mais_ouvidas = df[df['Popularidade']==df['Popularidade'].max()]
        return mais_ouvidas
    elif mais_ou_menos == "-":
        menos_ouvidas = df[df['Popularidade']==df['Popularidade'].min()]
        return menos_ouvidas

#Músicas mais longas e músicas mais curta
def iv(df, mais_ou_menos = "+"):
    if mais_ou_menos == "+":
        mais_longas = df[df['Tempo']==df['Tempo'].max()]
        return mais_longas
    elif mais_ou_menos == "-":
        menos_longas = df[df['Tempo']==df['Tempo'].min()]
        return menos_longas

#Álbuns mais premiados
def v(df):
    mais_premiado = df[df["Prêmios"]==df["Prêmios"].max()]
    return mais_premiado

# Existe alguma relação entre a duração da música e sua popularidade?
def vi(df, mais_ou_menos = "+"):
    longas_album = ii(df, mais_ou_menos)
    ouvidas_album = i(df, mais_ou_menos) 
    tempo_popularidade = pd.merge(longas_album, ouvidas_album, how='inner')
    print("Maior tempo e maior popularidade: \n", tempo_popularidade)