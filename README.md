# 🚀 Sanchez Family Classifier

**_🚧 Under Construction 🚧_**

Demo data science project to take input text and classify which member of the Sanchez family from Rick and Morty is most likely to say it.

![Sanchez Family](https://variety.com/wp-content/uploads/2022/08/Rick-and-Morty-Season-6.png?w=1000)

## ✨ Motivation

Demonstrate the building of a basic data science project/experiment, emphasizing project structure & code quality (as opposed to sophistication).

## ✨ Goals

- [ ] ⚡ Lightning-fast ⚡ inference pipeline

## ✨ Contents

- `run_experiment.py`: Script for experiment that trains models and determines the best given input configs
- `experiment_configs.yaml`: Experiment input configs
- `experiment_results_report.md`: Automatically-generated report of the results of the last experiment
- `create_features.py`: Feature creation functions
- `data.csv`: Rick and Morty script data
- `current_best_model.pkl`: The current best model given experiment runs
- `gradio_app.py`: Basic Gradio app to demo the current best model

## ✨ Feature Creation

### Counts of Top Contentful N-Grams

**Intuition:** Sanchez family members are likely to have characteristic words/phrases (e.g. _"wubba lubba dub dub"_ for Rick or _"aw geez"_ for Morty).

### Average Word Embeddings by POS-Tag Groups

**Intuition:** Since we are avoiding LLMs (BERT sentence embeddings, etc.) for inference speed, we use Gensim embeddings as an efficient way to embed the semantic content of the input text. We average these embeddings across POS-tag groups (Verbs, Nouns, etc.) to avoid the dillution of topical/semantic information since word embeddings, by nature, also capture syntactic information. We use the `en_core_web_sm` spaCy model for efficient POS-tagging. 

### Other Low-Hanging Features

- Total token count
- Total token counts by POS-tag group
- Total stop-word token count
- Word-embedding variance scalars by POS-tag group

### Current Ideas & To-Do

1. Weight embedding averages by TF-IDF scores:
    - $\text{TF}(t, d) = \frac{\text{Number of times term } t \text{ appears in a document } d}{\text{Total number of terms in the document}}$
    - $\text{IDF}(t, D) = \log \left( \frac{\text{Total number of documents in the corpus } D}{\text{Number of documents with term } t \text{ in it}} \right)$
    - $\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$
2. Calculate unigram/bigram/trigram counts (and other misc counts useful for TF-IDF), and pass those dicts to frequency extractors that use them.
3. Use SpaCy's "Matcher"(?) to extract phrases (e.g. "wubba lubba dub dub")?
4. Generate markdown reports and save them to .md files and a clean, minimal printout of name & results to the console
5. Add auto-gen'ed experiment names
6. Add to Gradio app the dashboard of experiments results with:
    - Multi-color grouped bar charts of metrics where each group is an experiment and each bar is a performance metric (plus avg feature importance chart?)
    - Pick-a-model multiselect that shows the markdown report of the selected model and loads the interactive inference app for that model... (plus feature importance chart?)
