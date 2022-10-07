import numpy as np
import pandas as pd


def prep_dataframe(dataframe_nome):
    try:
        df = pd.read_excel(dataframe_nome)
    except:
        print("Erro, arquivo não encontrado")
    else:
        df.drop(["Unnamed: 0", "Artista"], axis=1, inplace=True)
        df.sort_values(by = "Album", inplace = True)
        df.set_index(["Album", "Música"], inplace = True)

        pd.set_option("display.max_rows", 500)
        pd.set_option("display.min_rows", 500)

        return df

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

    :type lista_palavras: list or tuple

    """
    count_palavra = {}
    for palavra in lista_palavras:
        count_palavra[palavra] = lista_palavras.count(palavra)
        
    count_palavra = pd.Series(count_palavra)
    count_palavra.sort_values(ascending=False, inplace = True)

    return count_palavra


#-----------------------------------------------------------------------

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


#-----------------------------------------------------------------------

def ii_palavras_comuns_tit_musicas(df):

    album_musica = df.index.values

    palavras_musica = []
    for musica in album_musica:
        palavras_musica += musica[1].split()

    palavras_musica = arruma_palavra(palavras_musica)

    count_palavra = count_palavras(palavras_musica)

    return count_palavra


#-----------------------------------------------------------------------

def iii(df):

    novo_df = df.droplevel("Música")

    albuns = list(novo_df.index.values)

    letras =  list(novo_df["Lyric"].values)

    dic = {}
    dic[albuns[0]] = letras[0].split()
    for num in range(1, len(albuns)):
        if albuns[num] != albuns[num-1]:
            dic[albuns[num]] = letras[num].split()
        else: 
            dic[albuns[num]] += letras[num].split()

    novo_dic = {}
    for key, elemento in dic.items():
        arr = arruma_palavra(elemento)
        cont = count_palavras(arr)
        novo_dic[key] = cont

    return novo_dic


#-----------------------------------------------------------------------

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


#-----------------------------------------------------------------------

def v(df):
    album_letra = df["Lyric"]
    album_letra = album_letra.droplevel("Música")
    
    letras = album_letra.to_list()
    albuns = list(album_letra.index.values)

    letras = arruma_palavra(letras)
    albuns = arruma_palavra(albuns)

    recorrencia = {}

    for album in albuns:
        recorrencia[album] = 0

    for num in range(len(letras)):
        if letras[num].count(albuns[num]) != 0:
            recorrencia[albuns[num]] += 1

    recorrencia = pd.Series(recorrencia)
    recorrencia.sort_values(ascending=False, inplace = True)

    return recorrencia


#-----------------------------------------------------------------------

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


#-----------------------------------------------------------------------

if __name__ == "__main__":

    df = prep_dataframe("A1 LP.xlsx")

    # print("-"*60)
    # print(ii_palavras_comuns_tit_musicas(df).head(15))

    # print("-"*60)
    # print(i_palavras_comuns_tit_album(df).head(10))

    for album, palavras_comuns in iii(df).items():
        print("\n\nAlbum: ", album, "\n")
        print(palavras_comuns.head())

    #print(iv_palavras_comuns_let_musicas(df).head(25))

    #print(v(df))

    #print(vi(df))