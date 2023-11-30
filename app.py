import os

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from src.globals import RESULTS_CSV_FPATH, DATA_DIR_PATH


IMG_URL = "https://variety.com/wp-content/uploads/2022/08/Rick-and-Morty-Season-6.png?"
SCORES_DF = pd.read_csv(RESULTS_CSV_FPATH, index_col=0)
EXPERIMENTS = list(SCORES_DF.index)


def plot_scores():
    ax = SCORES_DF.plot(kind="bar", legend=True, figsize=(6, 5))
    plt.xticks(rotation=90, fontsize=5)
    # Adjust size of plot
    ax.set_ylim([0.1, 0.8])
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8])
    ax.legend(
        loc="upper center", bbox_to_anchor=(0.5, 1), ncol=len(SCORES_DF.columns)
    )
    # Find max values for each category
    max_values = SCORES_DF.max()
    # Iterate over the bars
    n_rows = len(SCORES_DF)
    font_size = 4.5 if n_rows > 10 else 6
    font_size = 7 if n_rows < 5 else font_size
    for i, bar in enumerate(ax.patches):
        # Calculate the column (category) this bar belongs to
        column = int(i / n_rows)
        value = bar.get_height()
        is_max = value == max_values[SCORES_DF.columns[column]]
        fontweight = "bold" if is_max else "normal"
        # Annotate the bars
        ax.annotate(
            f"{value:.2f}",
            (bar.get_x() + bar.get_width() / 2.0, value),
            ha="center",
            va="center",
            xytext=(0, 10),
            textcoords="offset points",
            fontsize=font_size,
            fontweight=fontweight,
            rotation=90,
            color="darkgreen" if is_max else "black",
        )
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
