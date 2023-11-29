import os

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from src.globals import RESULTS_CSV_FPATH, DATA_DIR_PATH


IMG_URL = "https://variety.com/wp-content/uploads/2022/08/Rick-and-Morty-Season-6.png?"
SCORES_DF = pd.read_csv(RESULTS_CSV_FPATH, index_col=0)
EXPERIMENTS = list(SCORES_DF.index)


def plot_scores():
    ax = SCORES_DF.plot(kind="bar", legend=True, colormap="viridis")
    plt.xticks(rotation=90, fontsize=6)
    ax.set_ylim([0, 0.8])
    ax.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    plt.tight_layout()
    return plt


def handle_experiment_selection(selection):
    try:
        with open(os.path.join(DATA_DIR_PATH, f"{selection}.md"), "r") as f:
            st.markdown(f.read())
    except FileNotFoundError:
        st.markdown("No experiment description found.")


st.title("Sanchez Family Classifier")
st.image(IMG_URL)
st.divider()
st.header("Comparison of All Experiment Results")
st.pyplot(plot_scores())
st.divider()
st.header("Explore Experiments")
selection = st.selectbox("Select an experiment:", EXPERIMENTS)
st.divider()
handle_experiment_selection(selection)
