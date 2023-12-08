import os

from src.initialize_experiments import initialize_experiments
from src.config import EXPERIMENTS
from src.globals import DATA_DIR_PATH, RESULTS_CSV_FNAME


def clean_dirs():
    """Remove all .md files and results csv from the data directory."""
    for filename in os.listdir(DATA_DIR_PATH):
        if filename.endswith(".md") or filename == RESULTS_CSV_FNAME:
            os.remove(os.path.join(DATA_DIR_PATH, filename))


def run_experiments():
    """Run all experiments and report results."""
    # clean_dirs()
    experiments = initialize_experiments(EXPERIMENTS)
    # TODO: Add optional multiprocessing?
    for experiment in experiments:
        try:
            experiment.run()
            experiment.report_results()
        except Exception as e:
            print(f"Error running experiment {experiment.name}: {e}")


if __name__ == "__main__":
    run_experiments()
