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

mais_opa = p1.i(df, "+")
print("Mais ouvidas por álbum: \n", mais_opa)
menos_opa = p1.i(df, "-")
print("Menos ouvidas por álbum: \n",menos_opa)

#----
mais_lpa  = p1.ii(df, "+")
print("Mais longas por álbum: \n", mais_lpa)
menos_lpa = p1.ii(df, "-")
print("Menos longas por álbum: \n", menos_lpa)

p1.iii

p1.iv

p1.iv

df2 = fa.prep_dataframe("A1 LP.xlsx", 1)
p1.v(df2)

p1.vi