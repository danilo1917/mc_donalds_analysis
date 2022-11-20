import csv
import pandas as pd
import matplotlib.pyplot as plt
import forms
import numpy as np

def show_graph(y_values, x_values, x_labels):
    # import numpy as np
    # Data for plotting
    t = y_values
    s = x_values

    fig, ax = plt.subplots()
    ax.set(xlabel='Carboidratos', ylabel='Calorias',
        title='Carboidratos x calorias')
    ax.grid()
    fig.savefig("test.png")
    plt.stem(s, t)
    ax2 = ax.twiny()
    result_reg = [forms.f(x_values[x], y_values[x], x_values, y_values) for x in range(len(x_values))]
    ax2.plot(x_values, result_reg, color='red')
    plt.show()


df = pd.read_csv("Analise de dados/mc_donalds_analysis/menu.csv")
x_labels = [" "]
calorias = [i for j,i in enumerate(df["Calories"]) if x_labels[0] in df["Item"][j] ]
carboidratos = [i for j,i in enumerate(df["Carbohydrates"]) if x_labels[0] in df["Item"][j] ]

# Calcular valores médios:

# for i, v in enumerate(set(carboidratos)):
#     posicoes = [t for t in range(len(carboidratos)) if carboidratos[t]==v]
#     media_cal = 0
#     for k in range(len(calorias)):
#         if k in posicoes:
#             media_cal += calorias[k]
#     for n in posicoes:
#         calorias[n] = media_cal/len(posicoes)

for i in range(len(carboidratos)-1):
    if carboidratos[i+1]<carboidratos[i]:
        carboidratos[i], carboidratos[i+1] = carboidratos[i+1], carboidratos[i]
        calorias[i], calorias[i+1] = calorias[i+1], calorias[i]

show_graph(calorias, carboidratos, x_labels)
