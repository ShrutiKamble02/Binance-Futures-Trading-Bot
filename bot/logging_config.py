import logging
import os


LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "trading.log")


def setup_logger():
    """
    Configure logger for the application.
    Creates logs/trading.log automatically.
    """

    # Create logs folder if it doesn't exist
    os.makedirs(LOG_FOLDER, exist_ok=True)

    logger = logging.getLogger("TradingBot")
    logger.setLevel(logging.INFO)

    # Prevent duplicate log entries
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    # Log to file
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)

    # Log to console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger