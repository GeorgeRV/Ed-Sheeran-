import pandas as pd

indices = ["Shape of You", "Perfect", "Castle on the Hill", "Thinking Out Loud"]
colunas = ["Album", "Tempo", "Lyric"]
dados = [["÷ (Divide)", "03:53", "the club isn't " ], ["÷ (Divide)", "04:23", "este cantor lyrics"], ["÷ (Divide)", "04:27", "teste do teste"], ["× (Multiply)", "02:59", "letra teste"]]
         
df = pd.DataFrame(dados,index = indices, columns = colunas)