import logging
import os

def setup_logger():
    if not os.path.exists('data/logs'):
        os.makedirs('data/logs')

    logger = logging.getLogger("Analyzer")
    logger.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fh = logging.FileHandler("data/logs/analyzer.log")
    fh.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
