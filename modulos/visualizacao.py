import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from PIL import Image


def salva_graf(plot, fig_nome):
    fig = plot.get_figure()
    fig.savefig(fig_nome)


def graf(df, x_nome, y_nome, fig_nome):
    plot = sns.barplot(data = df, x = x_nome, y = y_nome)
    salva_graf(plot, fig_nome)


def img_wordcloud(df, nome = "nuvem.png", coluna = "Palavras", image = -1, color = "black"):

    palavras = df[coluna]

    lis = ""
    for palavra in palavras:
        lis += palavra + " "

    try:
        nuvem = WordCloud(mask = image, width=800, height=800, background_color = color, mode="RGBA").generate(lis)
    except AttributeError:
        nuvem = WordCloud().generate(lis)
    else:
        image_colors = ImageColorGenerator(image)
        nuvem.recolor(color_func = image_colors)
  
    fig, ax = plt.subplots(figsize=(10,6))
    ax.imshow(nuvem, interpolation='bilinear')
    ax.set_axis_off()
    plt.imshow(nuvem)
    nuvem.to_file(nome)


def visualizacao_iii(df):
    for album, palavras_comuns in p2.iii(df).items():        
        match album:
            case "× (Multiply)":
                imagem = np.array(Image.open("Multiply.jpg"))
                img_wordcloud(palavras_comuns, nome = album + ".png", image = imagem, color = "#1BBF44")
            case "÷ (Divide)":
                imagem = np.array(Image.open("Divide.jpg"))
                img_wordcloud(palavras_comuns, nome = album + ".png", image = imagem, color = "#79BED9")   
            case "(Equals)":
                imagem = np.array(Image.open("Equal.jpg"))
                img_wordcloud(palavras_comuns, nome = album + ".png", image = imagem, color = "#D90D1E") 
            case "(Plus)":
                imagem = np.array(Image.open("Plus.jpg"))
                img_wordcloud(palavras_comuns, nome = album + ".png", image = imagem, color = "#C53A01") 
            case other:      
                img_wordcloud(palavras_comuns, nome = album + ".png")

#-----------------------------------------------------------------------

if __name__ == "__main__":
    import funcoes_auxiliares as fa
    import perguntas_2 as p2

    df = fa.prep_dataframe("A1 LP.xlsx")

    # stop = set(STOPWORDS)
    # print(stop)

    print("-"*60)
    fun_i = p2.i_palavras_comuns_tit_album(df).head(10)
    img_wordcloud(fun_i)


    print("-"*60)
    fun_ii = p2.ii_palavras_comuns_tit_musicas(df)
    graf(fun_ii, "Palavras", "Contagem", "teste_2.png")
    print(fun_ii.head(15))
    img_wordcloud(fun_ii, nome = "nuvem2.png")
    

    print("-"*60)
    visualizacao_iii(df)
    
        

    # print("-"*60)

    # fun_iv = p2.iv_palavras_comuns_let_musicas(df)
    # print(fun_iv.head(25))
    # graf(fun_iv, "Palavras", "Contagem", "teste_4.png")
    # img_wordcloud(fun_iv, nome = "nuvem4.png")

    # print("-"*60)
    # fun_v =p2.v(df)
    # graf(fun_v, "Palavras", "Contagem", "teste_5.png")
    # print(fun_v)

    # print("-"*60)
    # fun_vi =p2.vi(df).head(10)
    # graf(fun_vi, "Palavras", "Contagem", "teste_6.png")
    # print(fun_vi)


    # for album, palavras_comuns in p2.iii(df).items():
    #     print("\n\nAlbum: ", album, "\n")
    #     print(palavras_comuns.head())