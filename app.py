import os

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import transforms
import streamlit as st
from matplotlib.patheffects import withStroke


from src.globals import RESULTS_CSV_FPATH, DATA_DIR_PATH


IMG_URL = "https://variety.com/wp-content/uploads/2022/08/Rick-and-Morty-Season-6.png?"

RICK_ONLY_NAME = "Rick-Only"
UNIGRAM_ONE_HOT_NAME = "Unigram One-Hot"


_READABLE_NAME_MAP = {
    "LgstcRgrssn": "Logistic Regression",
    "GrdntBstng": "Gradient Boosting",
    "RndmFrst": "Random Forest",
    "DcsnTr": "Decision Tree",
    "GssnNB": "Naive Bayes",
}

_model_counts = {
    "LgstcRgrssn": 0,
    "GrdntBstng": 0,
    "RndmFrst": 0,
    "DcsnTr": 0,
    "GssnNB": 0,
}


def get_readable_name(name: str) -> str:
    """Converts unreadable experiment names to human-readable names."""
    if "RckPrdctr" in name:
        return RICK_ONLY_NAME
    if "LgstcRgrssn" in name and "1fs" in name:
        return UNIGRAM_ONE_HOT_NAME
    for model in _model_counts:
        if model in name:
            _model_counts[model] += 1
            return f"{_READABLE_NAME_MAP[model]} {_model_counts[model]}"
    raise ValueError(f"Unrecognized experiment name: {name}")


SCORES_DF = pd.read_csv(RESULTS_CSV_FPATH, index_col=0)
SCORES_DF["number agnostic sortable index"] = SCORES_DF.index.str[:5]
SCORES_DF = SCORES_DF.sort_values(by=["number agnostic sortable index", "Accuracy"])
SCORES_DF = SCORES_DF.drop(columns=["number agnostic sortable index"])
_readable_names = SCORES_DF.index.map(get_readable_name)
NAME_MAP = {new: old for new, old in zip(_readable_names, SCORES_DF.index)}
SCORES_DF.index = _readable_names
_rows_to_move = SCORES_DF.loc[[RICK_ONLY_NAME, UNIGRAM_ONE_HOT_NAME]]
_remaining_rows = SCORES_DF.drop([RICK_ONLY_NAME, UNIGRAM_ONE_HOT_NAME])
SCORES_DF = pd.concat([_rows_to_move, _remaining_rows])


COLORS = {
    "Decision Tree": "indigo",
    "Gradient Boosting": "darkslategray",
    "Logistic Regression": "dimgray",
    "Naive Bayes": "darkolivegreen",
    "Random Forest": "darkslategray",
}


def plot_scores():
    # Remove Rick-Only and Unigram One-Hot baselines
    df = SCORES_DF.drop([RICK_ONLY_NAME, UNIGRAM_ONE_HOT_NAME])
    # Create basic plot
    ax = df.plot(kind="bar", legend=True, figsize=(9, 6))
    plt.xticks(rotation=90, fontsize=9)
    ax.set_ylim([0.1, 0.66])
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    ax.tick_params(axis="y", labelsize=7)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1), ncol=len(df.columns))
    # Find max values for each category
    max_values = df.max()
    # Prepare colors for x labels
    x_label_colors = []
    for name in df.index:
        if name == RICK_ONLY_NAME or name == UNIGRAM_ONE_HOT_NAME:
            continue
        x_label_colors.append("dimgray")
    # Iterate over the bars
    n_rows = len(df)
    font_size = 4.5 if n_rows > 15 else 5.6
    font_size = font_size if n_rows > 10 else 7
    font_size = 8 if n_rows < 5 else font_size
    for i, bar in enumerate(ax.patches):
        # Infer the column from the index
        column = int(i / n_rows)
        # Annotate the bars with their values
        value = bar.get_height()
        is_max = value == max_values[df.columns[column]]
        shadow_color = "yellow" if is_max else "white"
        shadow_width = 3 if is_max else 5
        alpha = 0.3 if is_max else 1
        # Add annotation
        ax.annotate(
            f"{value:.2f}",
            (bar.get_x() + bar.get_width() / 2.0, value),
            ha="center",
            va="center",
            xytext=(0, 13),
            textcoords="offset points",
            fontsize=font_size,
            rotation=90,
            color="black",
            path_effects=[withStroke(linewidth=shadow_width, foreground=shadow_color, alpha=alpha)],
        )
        if i < len(x_label_colors):
            color = "black" if is_max else x_label_colors[i]
            # Set the x label color for this group
            ax.get_xticklabels()[i].set_color(color)
            # Set the shadow color for this group
            ax.get_xticklabels()[i].set_path_effects(
                [withStroke(linewidth=shadow_width, foreground=shadow_color, alpha=alpha)]
            )

    # Add benchmark lines
    for y, color, linestyle, alpha in [
        (0.6, "steelblue", "dashed", 0.7),
        (0.5, "darkorange", "dashed", 0.7),
        (0.476, "steelblue", "dashdot", 0.7),
        (0.128, "darkorange", "dashdot", 0.7),
        (0.487, "steelblue", "dotted", 0.8),
        (0.275, "darkorange", "dotted", 0.8),
    ]:
        ax.axhline(
            y=y,
            color=color,
            linestyle=linestyle,
            linewidth=1.3,
            zorder=0,
            alpha=alpha,
        )
    # Add benchmark line labels
    trans = transforms.blended_transform_factory(
        ax.get_yticklabels()[0].get_transform(), ax.transData
    )
    for text, y, color in [
        # ("(Benchmarks)", 0.37, "gray"),
        ("Roommate", 0.6, "steelblue"),
        ("Roommate", 0.503, "darkorange"),
        (RICK_ONLY_NAME, 0.47, "steelblue"),
        (RICK_ONLY_NAME, 0.128, "darkorange"),
        (UNIGRAM_ONE_HOT_NAME, 0.487, "steelblue"),
        (UNIGRAM_ONE_HOT_NAME, 0.275, "darkorange"),
    ]:
        text = ax.text(
            1.02,
            y,
            text,
            color=color,
            size=7,
            transform=trans,
            va="center",
        )
        text.set_path_effects([withStroke(linewidth=3, foreground="white")])
    plt.tight_layout()
    return plt


def handle_experiment_selection(selection):
    name = NAME_MAP[selection]
    try:
        with open(os.path.join(DATA_DIR_PATH, f"{name}.md"), "r") as f:
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
selection = st.selectbox("Select an experiment:", SCORES_DF.index)
st.divider()
handle_experiment_selection(selection)
