import numpy as np
import pandas as pd


def prep_dataframe(dataframe_nome):
    df = pd.read_excel(dataframe_nome)
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


    if __name__ == "__main__":

        df = prep_dataframe("A1 LP.xlsx")

        # print("-"*60)
        # print(ii_palavras_comuns_tit_musicas(df).head(15))

        print("-"*60)
        print(i_palavras_comuns_tit_album(df).head(10))

        # for album, palavras_comuns in iii(df).items():
        #     print("\n\nAlbum: ", album, "\n")
        #     print(palavras_comuns.head())

        #print(iv_palavras_comuns_let_musicas(df).head(25))

        #print(v(df))

        #print(vi(df))