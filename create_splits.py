import pandas as pd
from sklearn.model_selection import train_test_split

from src.globals import (
    RAW_SCRIPT_DATA_FPATH,
    SANCHEZ_FAMILY_LABELS,
    TEST_DATA_FPATH,
    DEV_DATA_FPATH,
    TRAIN_DATA_FPATH,
    RANDOM_SEED,
)


MIN_WORDS_IN_UTTERANCE = 6
TEST_EPISODE_NOS = [3, 6, 8]
DEV_EPISODE_NOS = [5, 7, 9]
SPLIT_RATIOS = {
    "train": 0.68,
    "dev": 0.19,
    "test": 0.13,
}


def load_data() -> pd.DataFrame:
    # Read in the raw scripts froom seasons 1-3
    df = pd.read_csv(RAW_SCRIPT_DATA_FPATH)
    # Filter to Sanchez family utterances
    df = df[df["name"].isin(SANCHEZ_FAMILY_LABELS)]
    # Filter out utterances with fewer than `min_words` words
    min_spaces = MIN_WORDS_IN_UTTERANCE - 1
    df = df[df["line"].str.count(" ") >= min_spaces]
    # Rename line and name columns
    df = df.rename(columns={"line": "utterance", "name": "label"})
    print(f"\tTotal Utterances: {len(df)} utterances")
    return df


def save_data(train_df: pd.DataFrame, dev_df: pd.DataFrame, test_df: pd.DataFrame):
    # Sanity check values counts for Sanchez family member across splits
    print("Sanchez family member value counts across splits:")
    print(f"\tTrain: {dict(train_df['label'].value_counts())}")
    print(f"\tDev: {dict(dev_df['label'].value_counts())}")
    print(f"\tTest: {dict(test_df['label'].value_counts())}")
    train_df.to_csv(TRAIN_DATA_FPATH, index=False)
    dev_df.to_csv(DEV_DATA_FPATH, index=False)
    test_df.to_csv(TEST_DATA_FPATH, index=False)


def create_splits_by_episode():
    df = load_data()
    # Split such that episodes are not split across train/dev/test (avoid topic leakage)
    test_df = df[df["episode no."].isin(TEST_EPISODE_NOS)][["utterance", "label"]]
    dev_df = df[df["episode no."].isin(DEV_EPISODE_NOS)][["utterance", "label"]]
    train_df = df[~df["episode no."].isin(TEST_EPISODE_NOS + DEV_EPISODE_NOS)]
    train_df = train_df[["utterance", "label"]]
    save_data(train_df, dev_df, test_df)


def create_random_splits():
    df = load_data()
    # Split randomly
    train_df, test_df = train_test_split(
        df, test_size=SPLIT_RATIOS["test"], random_state=RANDOM_SEED
    )
    adjusted_dev_ratio = SPLIT_RATIOS["dev"] / (1 - SPLIT_RATIOS["test"])
    train_df, dev_df = train_test_split(
        train_df, test_size=adjusted_dev_ratio, random_state=RANDOM_SEED
    )
    save_data(train_df, dev_df, test_df)


if __name__ == "__main__":
    create_splits_by_episode()
    # create_random_splits()
