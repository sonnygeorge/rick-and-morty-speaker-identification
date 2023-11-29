import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from src.globals import RESULTS_CSV_FPATH


IMG_URL = "https://variety.com/wp-content/uploads/2022/08/Rick-and-Morty-Season-6.png?"
SCORES_DF = pd.read_csv(RESULTS_CSV_FPATH, index_col=0)


def plot_dataframe():
    ax = SCORES_DF.plot(kind="bar", legend=True, colormap="viridis")
    plt.xticks(rotation=90, fontsize=6)
    ax.set_ylim([0, .8])
    ax.set_yticks([0, .2, .4, .6, .8])
    plt.tight_layout()
    return plt


st.title("Sanchez Family Classifier")
st.image(IMG_URL)
st.header("Experiment Results")
st.pyplot(plot_dataframe())
