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


#---------------------------------------------

def i_prop_tempo_letra(df):
    
    return df


#---------------------------------------------

def ii(df):
    return df


#---------------------------------------------

def iii(df):
    return df


#---------------------------------------------

if __name__ == "__main__":

    df = prep_dataframe("A1 LP.xlsx")

    print(i(df))

    print(ii(df))

    print(iii(df))