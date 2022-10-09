from tkinter import Menubutton
import modulos.perguntas_1 as p1
import modulos.perguntas_2 as p2
import modulos.perguntas_3 as p3
import modulos.funcoes_auxiliares as fa
import modulos.visualizacao as vi
import sys
import pandas as pd

sys.path.insert(0, "./excel")

df = fa.prep_dataframe("A1 LP.xlsx" ,"EdSheeran")

print("-"*60, "\nFunção 1\n")
mais_opa = p1.i(df, "+")
print("Mais ouvidas por álbum: \n", mais_opa)
menos_opa = p1.i(df, "-")
print("Menos ouvidas por álbum: \n",menos_opa)

#-------------------------------------------------------
print("-"*60, "\nFunção 2\n")
mais_lpa  = p1.ii(df, "+")
print("Mais longas por álbum: \n", mais_lpa)
menos_lpa = p1.ii(df, "-")
print("Menos longas por álbum: \n", menos_lpa)

#-------------------------------------------------------
print("-"*60, "\nFunção 3\n")
p1.iii(df)

#-------------------------------------------------------
print("-"*60, "\nFunção 4\n")
p1.iv(df)


#-------------------------------------------------------
print("-"*60, "\nFunção 5\n")
df2 = fa.prep_dataframe("A1 LP.xlsx", 1)
p1.v(df2)

#-------------------------------------------------------
print("-"*60, "\nFunção 6\n")
p1.vi(df)

print("-"*60, "\nFunção 1\n")

df2 = fa.prep_2(df)

print(p2.i_palavras_comuns_tit_album(df2).head(10))

print("-"*60, "\nFunção 2\n")
print(p2.ii_palavras_comuns_tit_musicas(df2).head(15))

print("-"*60, "\nFunção 3\n")
for album, palavras_comuns in p2.iii(df2).items():
    print("\n\nAlbum: ", album, "\n")
    print(palavras_comuns.head())

print("-"*60, "\nFunção 4\n")
print(p2.iv_palavras_comuns_let_musicas(df2).head(25))

print("-"*60, "\nFunção 5\n")
print(p2.v(df2))

print("-"*60, "\nFunção 6\n")
print(p2.vi(df2).head(20))

#-------------------------------------------------------
print("-"*60, "\nFunção 1\n")
p3.i(df)

print("-"*60, "\nFunção 2\n")
p3.ii(df)

print("-"*60, "\nFunção 3\n")
p3.iii(df)
