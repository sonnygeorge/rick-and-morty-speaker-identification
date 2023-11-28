import pandas as pd

from src.globals import (
    RAW_SCRIPT_DATA_FPATH,
    SANCHEZ_FAMILY_LABELS,
    TEST_DATA_FPATH,
    DEV_DATA_FPATH,
    TRAIN_DATA_FPATH,
)


MIN_WORDS_IN_UTTERANCE = 3

# After some experimenting, these produce nice splits
TEST_EPISODE_NOS = [3, 6]
DEV_EPISODE_NOS = [5]


def create_splits():
    # Read in the raw scripts froom seasons 1-3
    df = pd.read_csv(RAW_SCRIPT_DATA_FPATH)
    # Filter to Sanchez family utterances
    df = df[df["name"].isin(SANCHEZ_FAMILY_LABELS)]
    # Filter out utterances with fewer than `min_words` words
    min_spaces = MIN_WORDS_IN_UTTERANCE - 1
    df = df[df["line"].str.count(" ") >= min_spaces]
    # Rename line and name columns
    df = df.rename(columns={"line": "utterance", "name": "label"})
    # Split such that episodes are not split across train/dev/test (avoid topic leakage)
    test_df = df[df["episode no."].isin(TEST_EPISODE_NOS)][["utterance", "label"]]
    dev_df = df[df["episode no."].isin(DEV_EPISODE_NOS)][["utterance", "label"]]
    train_df = df[~df["episode no."].isin(TEST_EPISODE_NOS + DEV_EPISODE_NOS)]
    train_df = train_df[["utterance", "label"]]
    # Sanity check values counts for Sanchez family member across splits
    print("Sanchez family member value counts across splits:")
    print(f"\tTrain: {dict(train_df['label'].value_counts())}")
    print(f"\tDev: {dict(dev_df['label'].value_counts())}")
    print(f"\tTest: {dict(test_df['label'].value_counts())}")
    # Write to CSV
    train_df.to_csv(TRAIN_DATA_FPATH, index=False)
    dev_df.to_csv(DEV_DATA_FPATH, index=False)
    test_df.to_csv(TEST_DATA_FPATH, index=False)


if __name__ == "__main__":
    create_splits()
