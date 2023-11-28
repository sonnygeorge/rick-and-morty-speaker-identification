from src.initialize_experiments import initialize_experiments
from src.config import CONFIGURED_EXPERIMENTS


def run_experiments():
    experiments = initialize_experiments(CONFIGURED_EXPERIMENTS)
    # TODO: Add optional multiprocessing?
    for experiment in experiments:
        experiment.run()
        experiment.report_results()


if __name__ == "__main__":
    run_experiments()
