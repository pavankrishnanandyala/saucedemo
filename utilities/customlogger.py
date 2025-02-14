import logging
import os


class logGen:
    @staticmethod
    def logger():
        # Create Logs directory if it doesn't exist
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Set up logging with absolute path
        log_file = os.path.join(log_dir, "automation.log")
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )
        return logging.getLogger()