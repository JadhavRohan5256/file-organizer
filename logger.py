import logging, requests
from os import makedirs, getcwd, path, getenv
from dotenv import load_dotenv

makedirs("files", exist_ok=True)
load_dotenv()

# Formatter
log_formatter = """***[%(levelname)s]***
    Time: %(asctime)s
    Msg: %(message)s
    File: %(filename)s 
    Line: %(lineno)d
-------------------------------------------------"""

# Custom handler
class CustomHandler(logging.Handler):
    WEBHOOK_DISCORD_URL = getenv("WEBHOOK_DISCORD_URL")

    def emit(self, record):
        log_entry = self.format(record)
        try:
            requests.post(self.WEBHOOK_DISCORD_URL, {"content": log_entry})
        except:
            print("💣Something went wrong!💥")

formatter = logging.Formatter(log_formatter)

# File handler
file_handler = logging.FileHandler(path.join(path.dirname(path.abspath(__file__)), "files/folder_scanning_logger.log"), encoding="utf-8")
file_handler.setFormatter(formatter)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)


# Custom handler
custom_handler = CustomHandler()
custom_handler.setFormatter(formatter)

# Configure logger
logger = logging.getLogger("folder_scanning_logger")
logger.setLevel(logging.DEBUG)
logger.addHandler(custom_handler)
logger.addHandler(file_handler)
logger.addHandler(console_handler)