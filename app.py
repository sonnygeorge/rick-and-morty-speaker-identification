"""Streamlit app for exploring the experiment results... a bit of a code-barf."""

import os

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from matplotlib import transforms
from matplotlib.patheffects import withStroke

from src.run_inference import run_inference

DATA_DIR_PATH = "data"
RESULTS_CSV_FNAME = "results.csv"
RESULTS_CSV_FPATH = os.path.join(DATA_DIR_PATH, RESULTS_CSV_FNAME)
RICK_ONLY_NAME = "Rick-Only"
UNIGRAM_ONE_HOT_NAME = "Unigram One-Hot"
MAX_TOP_N = 5

HEADER_IMG_URL = "https://oyster.ignimgs.com/wordpress/stg.ign.com/2013/12/rickandmorty02_120213_1600.jpg?width=3840"
RICK_IMG_URL = "https://static.wikia.nocookie.net/ricksanchez/images/7/71/Rick.jpg/"
MORTY_IMG_URL = (
    "https://static.wikia.nocookie.net/rickandmorty/images/e/ee/Morty501.png/"
)
BETH_IMG_URL = (
    "https://static.wikia.nocookie.net/rickandmorty/images/5/58/Beth_Smith.png/"
)
SUMMER_IMG_URL = (
    "https://static.wikia.nocookie.net/rickandmorty/images/a/ad/Summer_is_cool.jpeg/"
)
JERRY_IMG_URL = (
    "https://static.wikia.nocookie.net/rickandmorty/images/f/f1/Jerry_Smith.png/"
)

IMG_URLS_BY_LABEL = {
    "Rick": RICK_IMG_URL,
    "Morty": MORTY_IMG_URL,
    "Beth": BETH_IMG_URL,
    "Summer": SUMMER_IMG_URL,
    "Jerry": JERRY_IMG_URL,
}

_READABLE_NAME_MAP = {
    "LgstcRgrssn": "Logistic Regression",
    "GrdntBstng": "Gradient Boosting",
    "RndmFrst": "Random Forest",
    "DcsnTr": "Decision Tree",
    "GssnNB": "Naive Bayes",
    "XGBClssfr": "XGBoost",
}

_model_counts = {
    "LgstcRgrssn": 0,
    "GrdntBstng": 0,
    "RndmFrst": 0,
    "DcsnTr": 0,
    "GssnNB": 0,
    "XGBClssfr": 0,
}

NAMES_TO_HIGHLIGHT = [
    "Logistic Regression 441",  # THE BEST
]

COLORS = {
    "Decision Tree": "dimgray",
    "Gradient Boosting": "dimgray",
    "Logistic Regression": "dimgray",
    "Naive Bayes": "dimgray",
    "Random Forest": "dimgray",
    "XGBoost": "dimgray",
}


def get_readable_name(name: str) -> str:
    """Converts unreadable experiment names to human-readable names."""
    if "RckPrdctr" in name:
        return RICK_ONLY_NAME
    if "LgstcRgrssn" in name and "_1fs" in name:
        return UNIGRAM_ONE_HOT_NAME
    for model in _model_counts:
        if model in name:
            _model_counts[model] += 1
            return f"{_READABLE_NAME_MAP[model]} {_model_counts[model]}"
    raise ValueError(f"Unrecognized experiment name: {name}")


# Load and manipulate results dataframe
SCORES_DF = pd.read_csv(RESULTS_CSV_FPATH, index_col=0)
N_EXPERIMENTS = len(SCORES_DF)
_readable_names = SCORES_DF.index.map(get_readable_name)
NAME_MAP = {new: old for new, old in zip(_readable_names, SCORES_DF.index)}
SCORES_DF.index = _readable_names
SCORES_DF["Accuracy + Macro F1"] = SCORES_DF["Accuracy"] + SCORES_DF["Macro F1"]
NEW_SCORES_DF = pd.DataFrame()
for substring in list(_READABLE_NAME_MAP.values()) + [
    RICK_ONLY_NAME,
    UNIGRAM_ONE_HOT_NAME,
]:
    subgroup = SCORES_DF[SCORES_DF.index.str.contains(substring)]
    top_rows = subgroup.sort_values(by="Accuracy + Macro F1", ascending=False).head(
        MAX_TOP_N
    )
    NEW_SCORES_DF = pd.concat([NEW_SCORES_DF, top_rows])
SCORES_DF = NEW_SCORES_DF
SCORES_DF["number agnostic sortable index"] = SCORES_DF.index.str[:5]
SCORES_DF = SCORES_DF.sort_values(by=["Accuracy + Macro F1"])
SCORES_DF = SCORES_DF.drop(
    columns=["number agnostic sortable index", "Accuracy + Macro F1"]
)
SCORES_DF = SCORES_DF[~SCORES_DF.index.str.contains("Decision Tree")]
SCORES_DF = SCORES_DF[~SCORES_DF.index.str.contains("Random Forest")]

# Uncomment if you want to delete excess .md from data folder

# for readable, slug in NAME_MAP.items():
#     if "Rick-Only" in readable or "Unigram One-Hot" in readable:
#         print(f"Skipping {readable}")
#         continue
#     if readable in SCORES_DF.index:
#         print(f"Skipping {readable}")
#         continue
#     fpath_to_delete = os.path.join(DATA_DIR_PATH, f"{slug}.md")
#     if os.path.exists(fpath_to_delete):
#         os.remove(fpath_to_delete)
#     print(f"Deleted {fpath_to_delete}")


def plot_scores():
    # Remove Rick-Only and Unigram One-Hot baselines from df
    df = SCORES_DF.drop([RICK_ONLY_NAME, UNIGRAM_ONE_HOT_NAME])
    # Create basic plot
    ax = df.plot(kind="bar", legend=True, figsize=(8, 7))
    plt.xticks(rotation=90, fontsize=9)
    plt.title("Best Experiments From Best Model Varieties", fontsize=10)
    ax.set_ylim([0.1, 0.66])
    ax.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6])
    ax.tick_params(axis="y", labelsize=7)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1), ncol=len(df.columns))
    # # Find max values for each category
    # max_values = df.max()
    # Prepare colors for x labels
    x_label_colors = []
    for model_name in df.index:
        model_name_readable = " ".join(model_name.split(" ")[:-1])
        color = COLORS[model_name_readable]
        x_label_colors.append(color)
    # Iterate over the bars
    # n_rows = len(df)
    # font_size = 4.5 if n_rows > 15 else 5.6
    # font_size = font_size if n_rows > 10 else 7
    font_size = 6.5
    for i, bar in enumerate(ax.patches):
        # Annotate the bars with their values
        value = bar.get_height()
        shadow_color = "white"
        shadow_width = 5
        alpha = 1
        # Set the x label and shadow for this group of bars
        if i < len(x_label_colors):
            if any(name in str(ax.get_xticklabels()[i]) for name in NAMES_TO_HIGHLIGHT):
                color = "black"
                shadow_color = "yellow"
                alpha = 0.6
            else:
                color = x_label_colors[i]
                shadow_color = "white"
            ax.get_xticklabels()[i].set_color(color)
            with_stroke = withStroke(
                linewidth=shadow_width, foreground=shadow_color, alpha=alpha
            )
            ax.get_xticklabels()[i].set_path_effects([with_stroke])
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
            path_effects=[
                withStroke(linewidth=shadow_width, foreground="white", alpha=1)
            ],
        )
    # Add benchmark lines
    for y, color, linestyle, alpha in [
        (0.6, "steelblue", "dashed", 1),
        (0.5, "darkorange", "dashed", 1),
        (0.476, "steelblue", "dashdot", 0.6),
        (0.128, "darkorange", "dashdot", 0.6),
        (0.487, "steelblue", "dotted", 0.7),
        (0.275, "darkorange", "dotted", 0.7),
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
    # plt.savefig(
    #     os.path.join("results_plot.png"),
    #     dpi=300,
    #     bbox_inches="tight",
    # )
    return plt


def handle_experiment_selection(selection):
    """Handle the user's selection of an experiment."""
    name = NAME_MAP[selection]
    try:
        with open(os.path.join(DATA_DIR_PATH, f"{name}.md"), "r") as f:
            st.markdown(f.read())
    except FileNotFoundError:
        st.markdown("No experiment description found.")


# Declare Streamlit app
st.header("Rick & Morty Speaker Identification", divider=True, anchor="center")
st.image(HEADER_IMG_URL)
st.markdown(
    "An interactive applet for exploring the results of [this](https://github.com/sonnygeorge/rick-and-morty-speaker-identification) project."
)
st.header("Run inference on your own text!", divider=True, anchor="center")
st.text("NOTE:")
st.markdown(
    """
Performance is severely hindered by:
- Being restricted to only token/n-gram-based features (E.g. no "sentence" embeddings).
- Only training on around 10 episodes.

See the [writeup](https://github.com/sonnygeorge/rick-and-morty-speaker-identification) for more details.
"""
)
st.divider()
col1, col2 = st.columns([1, 2])
with col2:
    st.text("")
    st.text("")
    st.markdown("Model in use: `Logistic Regression 441`")
    st.text("")
    text_input = st.text_input(
        "Enter your text here:", "Morty I'm a drunk, not a hack."
    )
    st.text("")
    button = st.button("Predict Speaker")
    st.text("(Takes a couple of seconds)")
with col1:
    image = st.image(IMG_URLS_BY_LABEL["Rick"])
if button:
    predicted = run_inference(text_input)
    image.image(IMG_URLS_BY_LABEL[predicted])
st.divider()
st.header("Comparison of top experiment results", divider=True, anchor="center")
st.text(f"Number of experiments run: {N_EXPERIMENTS}")
st.pyplot(plot_scores())
st.header("Explore Experiments", divider=True, anchor="center")
selection = st.selectbox("Select an experiment:", SCORES_DF.index)
handle_experiment_selection(selection)
