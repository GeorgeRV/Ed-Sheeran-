import numpy as np
import pandas as pd

def prep_dataframe(dataframe_nome, sheet_nome = 0):
    try:
        df = pd.read_excel(dataframe_nome, sheet_name = sheet_nome)
    except:
        print("Erro, arquivo não encontrado")
        raise
    else:
        return df

def sei(df):
    novo_df = df.sort_values(by = "Album", inplace = True)
    novo_df.set_index(["Album", "Música"], inplace = True)
    return novo_df


def arruma_palavra(lista, opc = 0):
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
        arruma = arruma.replace('× ', "")
        arruma = arruma.replace('÷ ', "")
        arruma = arruma.replace('-', "")
        if opc != 0:
            arruma = arruma.replace(opc, "")
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


def em_dataframe(df, nome_index_antigo, nome_coluna):
    """ Trasforma uma serie em um dataframe



    """

    novo_df = pd.DataFrame(df, columns = [nome_coluna])
    novo_df.reset_index(inplace=True)
    novo_df.rename(columns = {"index": nome_index_antigo}, inplace=True)

    return novo_df
