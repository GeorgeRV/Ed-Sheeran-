import numpy as np
import pandas as pd
import sys
import os
try:
    import modulos.perguntas_1 as p1
    import modulos.perguntas_2 as p2
    import modulos.perguntas_3 as p3
except:
    import perguntas_1 as p1
    import perguntas_2 as p2
    import perguntas_3 as p3


def prep_dataframe(dataframe_nome, sheet_nome = 0):
    """ Prepara uma panilha

    :param dataframe_nome: Nome da panilha
    :type dataframe_nome: string
    :param sheet_nome: Nome da aba ou seu index
    :type sheet_nome: string or int

    Recebe uma planilha do excel e o nome ou index da aba e e tenta retornar em um dataframe

    """
    try:
        df = pd.read_excel(dataframe_nome, sheet_name = sheet_nome)
    except:
        print("Erro, arquivo não encontrado")
        raise
    else:
        return df

def prep_2(df):
    """ Prepara o dataframe do Ed Sheeran de meneira específica

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    Recebe um dataframe e o retorna com um multiIndex 

    """
    novo_df = df
    novo_df.sort_values(by = "Album", inplace = True)
    novo_df.set_index(["Album", "Música"], inplace = True)
    return novo_df


def arruma_palavra(lista, opc = None):
    """ Remove alguns caracteres especiais de um conjunto de palavras e retorna uma lista com as palavras "arrumadas"

    :param lista: Lista com palavras(strings)
    :type lista: list or tuple
    :param opc: Caracter opcional a ser removido
    :type opc: string 

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
        arruma = arruma.replace('-', " ")
        if opc != None:
            arruma = arruma.replace(opc, "")
        lista_nova.append(arruma)
    return lista_nova


def count_palavras(lista_palavras):
    """ Conta palavras de uma lista e retorna uma Série em ordem decrescente

    :param lista_palavras: Lista com palavras(strings) 
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

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame
    :param nome_index_antigo: Nome do index antigo 
    :type nome_index_antigo: string
    :param nome_coluna: Nome da coluna
    :type nome_coluna: string

    """

    novo_df = pd.DataFrame(df, columns = [nome_coluna])
    novo_df.reset_index(inplace=True)
    novo_df.rename(columns = {"index": nome_index_antigo}, inplace=True)

    return novo_df


def pausa_limpa():
    """ Pausa e limpa a tela

    """
    os.system("PAUSE")
    os.system('cls')


def grupo_funcao(grup, func):
    """ Escreve na tela o grupo e função que vão execultadas

    :param grup: Número do grupo
    :type grup: int
    :param func: Número da função
    :type func: int

    """
    print(f"\t\t---Grupo  {grup}---")
    print(f"-------------------Função {func}-------------------\n")


def funcoes_1():
    """ Escreve na tela todas as funções do grupo 1 com o dataframe preparado

    """

    df = prep_dataframe("A1 LP.xlsx" ,"EdSheeran")
    df2 = prep_dataframe("A1 LP.xlsx", 1)

    grupo_funcao(1,1)
    mais_opa = p1.i(df, "+")
    print("Mais ouvidas por álbum: \n", mais_opa)
    pausa_limpa()

    grupo_funcao(1,1)
    menos_opa = p1.i(df, "-")
    print("Menos ouvidas por álbum: \n",menos_opa)
    pausa_limpa()


    grupo_funcao(1,2)
    mais_lpa  = p1.ii(df, "+")
    print("Mais longas por álbum: \n", mais_lpa)
    pausa_limpa()

    grupo_funcao(1,2)
    menos_lpa = p1.ii(df, "-")
    print("Menos longas por álbum: \n", menos_lpa)
    pausa_limpa()


    grupo_funcao(1,3)
    mais_ouvidas = p1.iii(df, "+")
    print("Mais ouvidas: \n", mais_ouvidas)
    pausa_limpa()

    grupo_funcao(1,3)
    menos_ouvidas = p1.iii(df, "-")
    print("Menos ouvidas: \n", menos_ouvidas)
    pausa_limpa()


    grupo_funcao(1,4)
    mais_longas = p1.iv(df, "+")
    print("Mais longas: \n", mais_longas)
    pausa_limpa()

    grupo_funcao(1,4)
    menos_longas = p1.iv(df, "-")
    print("Menos longas: \n", menos_longas)
    pausa_limpa()


    grupo_funcao(1,5)
    mais_premiado = p1.v(df2)
    print("Álbum mais premiado: \n", mais_premiado)
    pausa_limpa()


    grupo_funcao(1,6)
    maior_tempo_popularidade = p1.vi(df, "+")
    print("Maior tempo e maior popularidade: \n", maior_tempo_popularidade)
    pausa_limpa()

    grupo_funcao(1,6)
    menor_tempo_popularidade = p1.vi(df, "-")
    print("Menor tempo e maior popularidade: \n", menor_tempo_popularidade)
    pausa_limpa()

def funcoes_2():
    """ Escreve na tela todas as funções do grupo 2 com o dataframe preparado

    """

    df = prep_dataframe("A1 LP.xlsx" ,"EdSheeran")
    df = prep_2(df)

    grupo_funcao(2,1)
    print(p2.i_palavras_comuns_tit_album(df).head(10))
    pausa_limpa()

    grupo_funcao(2,2)
    print(p2.ii_palavras_comuns_tit_musicas(df).head(15))
    pausa_limpa()


    for album, palavras_comuns in p2.iii(df).items():
        grupo_funcao(2,3)
        print("\n\nAlbum: ", album, "\n")
        print(palavras_comuns.head())
        pausa_limpa()


    grupo_funcao(2,4)
    print(p2.iv_palavras_comuns_let_musicas(df).head(25))
    pausa_limpa()


    grupo_funcao(2,5)
    print(p2.v(df))
    pausa_limpa()


    grupo_funcao(2,6)
    print(p2.vi(df).head(20))
    pausa_limpa()


def funcoes_3():
    """ Escreve na tela todas as funções do grupo 3 com o dataframe preparado

    """

    df = prep_dataframe("A1 LP.xlsx" ,"EdSheeran")

    grupo_funcao(3,1)
    mais_palavras_album = p3.i(df, "+")
    print("Músicas com mais palavras por álbum: \n", mais_palavras_album)
    pausa_limpa()

    grupo_funcao(3,1)
    menos_palvras_album = p3.i(df, "-")
    print("Músicas com menos palavras por álbum: \n", menos_palvras_album)
    pausa_limpa()


    grupo_funcao(3,2)
    mais_palavras = p3.ii(df, "+")
    print("Mais palavras: \n", mais_palavras)
    pausa_limpa()

    grupo_funcao(3,2)
    menos_palavras = p3.ii(df, "-")
    print("Menos palavras: \n", menos_palavras)
    pausa_limpa()


    grupo_funcao(3,3)
    maior_tempo_popularidade = p3.iii(df, "+")
    print("Maior tempo e maior número de palavras: \n", maior_tempo_popularidade)
    pausa_limpa()

    grupo_funcao(3,3)
    menor_tempo_popularidade = p3.iii(df, "-")
    print("Menor tempo e menor número de palavras: \n", menor_tempo_popularidade)