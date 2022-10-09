import pandas as pd

df = pd.read_excel("A1 LP.xlsx")


# Músicas com mais e menos palavras por álbum
def i ():
    df_por_album = df.groupby(["Album"])
    mais_palavras_album = df_por_album["Letra"].transform(max) == df["Letra"]
    mais_palavras_album = df[mais_palavras_album]
    print("Músicas com mais palavras por álbum: \n", mais_palavras_album)

    menos_palvras_album = df_por_album["Letra"].transform(min) == df["Letra"]
    menos_palvras_album = df[menos_palvras_album]
    print("Músicas com menos palavras por álbum: \n", menos_palvras_album)

# Música com mais e menos palavras
def ii():
    mais_palavras = df[df["Letra"]==df["Letra"].max()]
    menos_palavras = df[df["Letra"]==df["Letra"].min()]

    print("Mais palavras: \n", mais_palavras)
    print("Menos palavras: \n", menos_palavras)

# Há relação entre a quantidade de palavras e a duração das músicas?

#Função para as músicas mais curtas e longas por álbum
def iv():
    mais_longas_album = df_por_album["Tempo"].transform(max) == df["Tempo"]
    mais_longas_album = df[mais_longas_album]

    menos_longas_album = df_por_album["Tempo"].transform(min) == df["Tempo"]
    menos_longas_album = df[menos_longas_album]

#Ver se os dtaframes formados pelas funções acima possuem valores iguais
def vi():
    maior_tempo_popularidade = pd.merge(mais_longas_album, mais_palavras_album, how='inner')
    print("Maior tempo e maior número de palavras: \n", maior_tempo_popularidade)

    menor_tempo_popularidade = pd.merge(menos_longas_album, menos_palvras_album, how='inner')
    print("Menor tempo e menor número de palavras: \n", menor_tempo_popularidade)

# Resposta: É possível ver que os dois fatores não possuem muita relação, 
#pois as duas funções só retornaram uma música cada.
