import numpy as np
import pandas as pd


def arruma_palavra(lista):
    """ Remove alguns caracteres especiais de um conjunto de palavras e retorna uma lista com as palavras "arrumadas"

    :type lista: list or tuple

    """
    lista_nova = []
    for palavra in lista:
        arruma = palavra.lower()
        arruma = arruma.replace('(', "")
        arruma = arruma.replace(')', "")
        arruma = arruma.replace(',', "")
        arruma = arruma.replace('?', "")
        arruma = arruma.replace('’', "'")
        arruma = arruma.replace('× ', '')
        arruma = arruma.replace('÷ ', '')
        lista_nova.append(arruma)
    return lista_nova


def count_palavras(lista_palavras):
    """ Conta palavras de uma lista e retorna uma Série em ordem decrescente

    """
    count_palavra = {}
    for palavra in lista_palavras:
        count_palavra[palavra] = lista_palavras.count(palavra)
        
    count_palavra = pd.Series(count_palavra)
    count_palavra.sort_values(ascending=False, inplace = True)

    return count_palavra


def i_palavras_comuns_tit_album(df):

    album_musica = df.index.values

    titulo_album = {}
    for album in album_musica:
        album = arruma_palavra(album)
        alb = album[0].replace("- EP", "")
        titulo_album[alb] = ""
    
    palavras_album = []
    for key in titulo_album.keys():
        palavras_album += key.split()

    count_palavra = count_palavras(palavras_album)

    return count_palavra


def ii_palavras_comuns_tit_musicas(df):

    album_musica = df.index.values

    palavras_musica = []
    for musica in album_musica:
        palavras_musica += musica[1].split()

    palavras_musica = arruma_palavra(palavras_musica)

    count_palavra = count_palavras(palavras_musica)

    return count_palavra


def iii():
    return ""


def iv_palavras_comuns_let_musicas(df):
    letras = list(df["Lyric"].values)

    lista = []
    for letra in letras:
        lista.append(letra)

    palavras_letras = []
    for palavras in lista:
        palavras_letras += palavras.split()

    palavras_letras = arruma_palavra(palavras_letras)

    return count_palavras(palavras_letras)


def v(df):
    album_letra = df["Lyric"]
    album_letra = album_letra.droplevel("Música")
    
    letras = album_letra.to_list()
    albuns = list(album_letra.index.values)

    letras = arruma_palavra(letras)
    albuns = arruma_palavra(albuns)

    recorrencia = {}
    for num in range(len(letras)):
        try:
            recorrencia[albuns[num]] += letras[num].count(albuns[num])
        except KeyError:
            recorrencia[albuns[num]] = letras[num].count(albuns[num])

    recorrencia = pd.Series(recorrencia)
    recorrencia.sort_values(ascending=False, inplace = True)

    return recorrencia


def vi(df):
    musica_letra = df["Lyric"]
    musica_letra = musica_letra.droplevel("Album")
    
    letras = musica_letra.to_list()
    musicas = list(musica_letra.index.values)

    letras = arruma_palavra(letras)
    musicas = arruma_palavra(musicas)

    recorrencia = {}
    for num in range(len(musicas)):
        recorrencia[musicas[num]] = letras[num].count(musicas[num])

    recorrencia = pd.Series(recorrencia)
    recorrencia.sort_values(ascending=False, inplace = True)

    return recorrencia




df = pd.read_excel("A1 LP.xlsx")
df.drop(["Unnamed: 0", "Artista"], axis=1, inplace=True)
df.sort_values(by = "Album", inplace = True)
df.set_index(["Album", "Música"], inplace = True)

pd.set_option("display.max_rows", 500)
pd.set_option("display.min_rows", 500)


# print("-"*60)
# print(ii_palavras_comuns_tit_musicas(df).head(15))

# print("-"*60)
# print(i_palavras_comuns_tit_album(df).head(10))

#print(iv_palavras_comuns_let_musicas(df).head(25))

print(v(df))

#print(vi(df))

# indices = ["Shape of You", "Perfect", "Castle on the Hill", "Thinking Out Loud"]
# colunas = ["Album", "Tempo", "Lyric"]
# dados = [["÷ (Divide)", "03:53", "the club isn't " ], ["÷ (Divide)", "04:23", "este cantor lyrics"], ["÷ (Divide)", "04:27", "teste do teste"], ["× (Multiply)", "02:59", "letra teste"]]
         
# df = pd.DataFrame(dados,index = indices, columns = colunas)