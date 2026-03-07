import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logging.info("Application started")
logging.warning("This is a warning message")
logging.error("An error occurred")
logging.critical("Critical issue encountered")
logging.debug("This is a debug message that won't be logged due to the INFO level")

print("Logging messages have been written to logs/app.log")
