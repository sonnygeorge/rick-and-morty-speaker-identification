import os

import pandas as pd
from sklearn.model_selection import train_test_split

from src.globals import (
    RAW_SCRIPT_DATA_FPATH,
    SANCHEZ_FAMILY_LABELS,
    RANDOM_SEED,
    TRAIN_STR,
    DEV_STR,
    TEST_STR,
    RANDOM_STR,
    BY_EPISODE_STR,
    DATA_DIR_PATH,
)


MIN_WORDS_IN_UTTERANCE = 6
TEST_EPISODE_NOS = [3, 6, 8]
DEV_EPISODE_NOS = [5, 7, 9]
SPLIT_RATIOS = {
    TRAIN_STR: 0.67,
    DEV_STR: 0.20,
    TEST_STR: 0.13,
}


def load_data() -> pd.DataFrame:
    # Read in the raw scripts froom seasons 1-3
    df = pd.read_csv(RAW_SCRIPT_DATA_FPATH)
    # Add previous speaker column
    for _, group in df.groupby("episode no."):
        previous_speaker = group["name"].shift(1)
        df.loc[group.index, "previous speaker"] = previous_speaker
    # Filter to Sanchez family utterances
    df = df[df["name"].isin(SANCHEZ_FAMILY_LABELS)]
    # Filter out utterances with fewer than `min_words` words
    min_spaces = MIN_WORDS_IN_UTTERANCE - 1
    df = df[df["line"].str.count(" ") >= min_spaces]
    # Rename line and name columns
    df = df.rename(columns={"line": "utterance", "name": "label"})
    print(f"\tTotal Utterances: {len(df)} utterances")
    return df


def save_data(
    train_df: pd.DataFrame,
    dev_df: pd.DataFrame,
    test_df: pd.DataFrame,
    method: str,
):
    # Sanity check values counts for Sanchez family member across splits
    print("Sanchez family member value counts across splits:")
    print(f"\tTrain: {dict(train_df['label'].value_counts())}")
    print(f"\tDev: {dict(dev_df['label'].value_counts())}")
    print(f"\tTest: {dict(test_df['label'].value_counts())}")
    train_fpath = os.path.join(DATA_DIR_PATH, f"{TRAIN_STR}_{method}.csv")
    dev_fpath = os.path.join(DATA_DIR_PATH, f"{DEV_STR}_{method}.csv")
    test_fpath = os.path.join(DATA_DIR_PATH, f"{TEST_STR}_{method}.csv")
    train_df.to_csv(train_fpath, index=False)
    dev_df.to_csv(dev_fpath, index=False)
    test_df.to_csv(test_fpath, index=False)


def create_splits_by_episode():
    df = load_data()
    # Split such that episodes are not split across train/dev/test (avoid topic leakage)
    test_df = df[df["episode no."].isin(TEST_EPISODE_NOS)]
    dev_df = df[df["episode no."].isin(DEV_EPISODE_NOS)]
    test_df = test_df[["utterance", "label", "previous speaker"]]
    dev_df = dev_df[["utterance", "label", "previous speaker"]]
    train_df = df[~df["episode no."].isin(TEST_EPISODE_NOS + DEV_EPISODE_NOS)]
    train_df = train_df[["utterance", "label", "previous speaker"]]
    save_data(train_df, dev_df, test_df, method=BY_EPISODE_STR)


def create_random_splits():
    df = load_data()[["utterance", "label", "previous speaker"]]
    # Split randomly
    train_df, test_df = train_test_split(
        df, test_size=SPLIT_RATIOS[TEST_STR], random_state=RANDOM_SEED
    )
    adjusted_dev_ratio = SPLIT_RATIOS[DEV_STR] / (1 - SPLIT_RATIOS[TEST_STR])
    train_df, dev_df = train_test_split(
        train_df, test_size=adjusted_dev_ratio, random_state=RANDOM_SEED
    )
    save_data(train_df, dev_df, test_df, method=RANDOM_STR)


if __name__ == "__main__":
    create_splits_by_episode()
    create_random_splits()
