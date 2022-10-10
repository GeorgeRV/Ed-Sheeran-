import pandas as pd
try:    
    import modulos.funcoes_auxiliares as fa
except:
    import funcoes_auxiliares as fa


#-----------------------------------------------------------------------

def i_palavras_comuns_tit_album(df):
    """ Agrupa as palavras únicas dos títulos dos albuns, as conta e ordena em ordem decrescente

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    Quais são as palavras mais comuns nos títulos dos Álbuns?

    """
    album_musica = df.index.values

    titulo_album = {}
    for album in album_musica:
        album = fa.arruma_palavra(album, " ep")
        titulo_album[album[0]] = ""
    
    palavras_album = []
    for key in titulo_album.keys():
        palavras_album += key.split()

    count_palavra = fa.count_palavras(palavras_album)

    novo_df = fa.em_dataframe(count_palavra, "Palavras", "Contagem")

    return novo_df


#-----------------------------------------------------------------------

def ii_palavras_comuns_tit_musicas(df):
    """ Agrupa as palavras únicas dos títulos das músicas, as conta e ordena em ordem decrescente

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    Quais são as palavras mais comuns nos títulos das músicas?

    """

    album_musica = df.index.values

    palavras_musica = []
    for musica in album_musica:
        palavras_musica += musica[1].split()

    palavras_musica = fa.arruma_palavra(palavras_musica)

    count_palavra = fa.count_palavras(palavras_musica)

    novo_df = fa.em_dataframe(count_palavra, "Palavras", "Contagem")

    return novo_df


#-----------------------------------------------------------------------

def iii(df):
    """ Agrupa as palavras únicas das letras das músicas por album, as conta e ordena em ordem decrescente

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    Quais são as palavras mais comuns nas letras das músicas, por Álbum?

    """

    novo_df = df.droplevel("Música")

    albuns = list(novo_df.index.values)

    letras =  list(novo_df["Letra"].values)

    dic = {}
    dic[albuns[0]] = letras[0].split()
    for num in range(1, len(albuns)):
        if albuns[num] != albuns[num-1]:
            dic[albuns[num]] = letras[num].split()
        else: 
            dic[albuns[num]] += letras[num].split()

    novo_dic = {}
    for key, elemento in dic.items():
        arr = fa.arruma_palavra(elemento)
        cont = fa.count_palavras(arr)
        novo_df = fa.em_dataframe(cont, "Palavras", "Contagem")
        novo_dic[key] = novo_df

    return novo_dic


#-----------------------------------------------------------------------

def iv_palavras_comuns_let_musicas(df):
    """ Agrupa as palavras únicas das letras das músicas, as conta e ordena em ordem decrescente

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    Quais são as palavras mais comuns nas letras das músicas, em toda a discografia?

    """

    letras = list(df["Letra"].values)

    lista = []
    for letra in letras:
        lista.append(letra)

    palavras_letras = []
    for palavras in lista:
        palavras_letras += palavras.split()

    palavras_letras = fa.arruma_palavra(palavras_letras)

    count_palavra = fa.count_palavras(palavras_letras)

    novo_df = fa.em_dataframe(count_palavra, "Palavras", "Contagem")

    return novo_df


#-----------------------------------------------------------------------

def v(df):
    """ Verifica a frequência na qual os títulos dos albuns aparecem nas letras das suas músicas

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    O título de um álbum é tema recorrente nas letras?

    """

    album_letra = df["Letra"]
    album_letra = album_letra.droplevel("Música")
    
    letras = album_letra.to_list()
    albuns = list(album_letra.index.values)

    letras = fa.arruma_palavra(letras)
    albuns = fa.arruma_palavra(albuns, "  ep")

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
    """ Verifica a frequência na qual os títulos dos músicas aparecem nas letras

    :param df: Dataframe do pandas
    :type df: pandas.core.frame.DataFrame

    O título de uma música é tema recorrente nas letras?

    """

    musica_letra = df["Letra"]
    musica_letra = musica_letra.droplevel("Album")
    
    letras = musica_letra.to_list()
    musicas = list(musica_letra.index.values)

    letras = fa.arruma_palavra(letras)
    musicas = fa.arruma_palavra(musicas)

    recorrencia = {}
    for num in range(len(musicas)):
        recorrencia[musicas[num]] = letras[num].count(musicas[num])

    recorrencia = pd.Series(recorrencia)
    recorrencia.sort_values(ascending=False, inplace = True)

    return recorrencia


#-----------------------------------------------------------------------

if __name__ == "__main__":
    import funcoes_auxiliares as fa

    df = fa.prep_dataframe("A1 LP.xlsx")
    df = fa.prep_2(df)

    print("-"*60, "\nFunção 1\n")
    print(i_palavras_comuns_tit_album(df).head(10))

    print("-"*60, "\nFunção 2\n")
    print(ii_palavras_comuns_tit_musicas(df).head(15))

    print("-"*60, "\nFunção 3\n")
    for album, palavras_comuns in iii(df).items():
        print("\n\nAlbum: ", album, "\n")
        print(palavras_comuns.head())

    print("-"*60, "\nFunção 4\n")
    print(iv_palavras_comuns_let_musicas(df).head(25))

    print("-"*60, "\nFunção 5\n")
    print(v(df))

    print("-"*60, "\nFunção 6\n")
    print(vi(df))