
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt



def generar_graficos(datos: DataFrame, datos_norm: DataFrame):
    """
    -----------------------------------------------------------------------------------------------------
                METODO ENCARGADO DEL MODELADO Y MUESTRA DE LOS DISTINTOS GRÁFICOS.
    -----------------------------------------------------------------------------------------------------

    Genera un gráfico por cada característica que muestra la distribución de los distintos registros
    agrupados y diferenciados por género.
    Los datos se muestran primero sin normalizar y luego normalizados en dos figuras distintas.
    """

    #Primera figura de datos sin normalizar
    fig, axes = plt.subplots(3, 3, figsize=(12, 7))
    fig.canvas.manager.set_window_title("Datos sin normalizar")

    sns.violinplot(x="genero", y="trigliceridos", hue="genero", data=datos, ax=axes[0, 0])
    axes[0, 0].set_title("Trigliceridos")
    axes[0, 0].set_xlabel(" ")
    axes[0, 0].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="hdl", hue="genero", data=datos, ax=axes[0, 1])
    axes[0, 1].set_title("HDL")
    axes[0, 1].set_xlabel(" ")
    axes[0, 1].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="ldl", hue="genero", data=datos, ax=axes[0, 2])
    axes[0, 2].set_title("LDL")
    axes[0, 2].set_xlabel(" ")
    axes[0, 2].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="colesterol", hue="genero", data=datos, ax=axes[1, 0])
    axes[1, 0].set_title("Colesterol")
    axes[1, 0].set_xlabel(" ")
    axes[1, 0].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="hematies", hue="genero", data=datos, ax=axes[1, 1])
    axes[1, 1].set_title("Hematies")
    axes[1, 1].set_xlabel(" ")
    axes[1, 1].set_ylabel("millones/mm³")

    sns.violinplot(x="genero", y="hemoglobina", hue="genero", data=datos, ax=axes[1, 2])
    axes[1, 2].set_title("Hemoglobina")
    axes[1, 2].set_xlabel(" ")
    axes[1, 2].set_ylabel("g/dl")

    sns.violinplot(x="genero", y="hematocrito", hue="genero", data=datos, ax=axes[2, 0])
    axes[2, 0].set_title("Hematocrito")
    axes[2, 0].set_xlabel(" ")
    axes[2, 0].set_ylabel("%")

    sns.violinplot(x="genero", y="leucocitos", hue="genero", data=datos, ax=axes[2, 1])
    axes[2, 1].set_title("Leucocitos")
    axes[2, 1].set_xlabel(" ")
    axes[2, 1].set_ylabel("mL")

    sns.violinplot(x="genero", y="vsg", hue="genero", data=datos, ax=axes[2, 2])
    axes[2, 2].set_title("VSG")
    axes[2, 2].set_xlabel(" ")
    axes[2, 2].set_ylabel("mm/h")


    #Segunda figura de datos normalizados
    fig2, axes2 = plt.subplots(3, 3, figsize=(12, 7))
    fig2.canvas.manager.set_window_title("Datos normalizados")

    sns.violinplot(x="genero", y="trigliceridos", hue="genero", data=datos_norm, ax=axes2[0, 0])
    axes2[0, 0].set_title("Trigliceridos")
    axes2[0, 0].set_xlabel(" ")
    axes2[0, 0].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="hdl", hue="genero", data=datos_norm, ax=axes2[0, 1])
    axes2[0, 1].set_title("HDL")
    axes2[0, 1].set_xlabel(" ")
    axes2[0, 1].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="ldl", hue="genero", data=datos_norm, ax=axes2[0, 2])
    axes2[0, 2].set_title("LDL")
    axes2[0, 2].set_xlabel(" ")
    axes2[0, 2].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="colesterol", hue="genero", data=datos_norm, ax=axes2[1, 0])
    axes2[1, 0].set_title("Colesterol")
    axes2[1, 0].set_xlabel(" ")
    axes2[1, 0].set_ylabel("mg/dl")

    sns.violinplot(x="genero", y="hematies", hue="genero", data=datos_norm, ax=axes2[1, 1])
    axes2[1, 1].set_title("Hematies")
    axes2[1, 1].set_xlabel(" ")
    axes2[1, 1].set_ylabel("millones/mm³")

    sns.violinplot(x="genero", y="hemoglobina", hue="genero", data=datos_norm, ax=axes2[1, 2])
    axes2[1, 2].set_title("Hemoglobina")
    axes2[1, 2].set_xlabel(" ")
    axes2[1, 2].set_ylabel("g/dl")

    sns.violinplot(x="genero", y="hematocrito", hue="genero", data=datos_norm, ax=axes2[2, 0])
    axes2[2, 0].set_title("Hematocrito")
    axes2[2, 0].set_xlabel(" ")
    axes2[2, 0].set_ylabel("%")

    sns.violinplot(x="genero", y="leucocitos", hue="genero", data=datos_norm, ax=axes2[2, 1])
    axes2[2, 1].set_title("Leucocitos")
    axes2[2, 1].set_xlabel(" ")
    axes2[2, 1].set_ylabel("mL")

    sns.violinplot(x="genero", y="vsg", hue="genero", data=datos_norm, ax=axes2[2, 2])
    axes2[2, 2].set_title("VSG")
    axes2[2, 2].set_xlabel(" ")
    axes2[2, 2].set_ylabel("mm/h")

    plt.tight_layout()
    plt.show()
