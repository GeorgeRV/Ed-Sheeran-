import pandas as pd

df = pd.read_excel("A1.xlsx")

#Músicas mais ouvidas e músicas menos ouvidas por Álbum
def i():
    df_por_album = df.groupby(["Album"])
    mais_ouvidas_album = df_por_album["Popularidade"].transform(max) == df["Popularidade"]
    mais_ouvidas_album = df[mais_ouvidas_album]
    print("Mais ouvidas por álbum: \n", mais_ouvidas_album)

    menos_ouvidas_album = df_por_album["Popularidade"].transform(min) == df["Popularidade"]
    menos_ouvidas_album = df[menos_ouvidas_album]
    print("Menos ouvidas por álbum: \n", menos_ouvidas_album)

#Músicas mais longas e músicas mais curtas por álbum
def ii():
    mais_longas_album = df_por_album["Tempo"].transform(max) == df["Tempo"]
    mais_longas_album = df[mais_longas_album]
    print("Mais longas por álbum: \n", mais_longas_album)

    menos_longas_album = df_por_album["Tempo"].transform(min) == df["Tempo"]
    menos_longas_album = df[menos_longas_album]
    print("Menos longas por álbum: \n", menos_longas_album)

#Músicas mais ouvidas e músicas menos ouvidas
def iii():
    mais_ouvidas = df[df['Popularidade']==df['Popularidade'].max()]
    menos_ouvidas = df[df['Popularidade']==df['Popularidade'].min()]

    print("Mais ouvidas: \n", mais_ouvidas)
    print("Menos ouvidas: \n", menos_ouvidas)

#Músicas mais longas e músicas mais curta
def iv():
    mais_longas = df[df['Tempo']==df['Tempo'].max()]
    menos_longas = df[df['Tempo']==df['Tempo'].min()]
    print("Mais longas: \n", mais_longas)
    print("Menos longas: \n", menos_longas)

#Álbuns mais premiados
def v():
    df2 = pd.read_excel("A1 LP Prêmios.xlsx")

    mais_premiado = df2[df2["Prêmios"]==df2["Prêmios"].max()]
    print("Álbum mais premiado: \n", mais_premiado)

# Existe alguma relação entre a duração da música e sua popularidade?
def vi():
    maior_tempo_popularidade = pd.merge(mais_longas_album, mais_ouvidas_album, how='inner')
    print("Maior tempo e maior popularidade: \n", maior_tempo_popularidade)

    menor_tempo_popularidade = pd.merge(menos_longas_album, menos_ouvidas_album, how='inner')
    print("Menor tempo e menor popularidade: \n", menor_tempo_popularidade)
