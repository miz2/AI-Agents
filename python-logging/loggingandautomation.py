import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def checklogs():
    with open("system_logs.txt") as file:
        errorcount=0;
        for line in file:
            if "ERROR" in line:
                logging.error(f"Error found in logs: {line.strip()}")
                errorcount+=1
            elif "WARNING" in line:
                logging.warning(f"Warning found in logs: {line.strip()}")
            else:
                logging.info(f"Info found in logs: {line.strip()}")
    logging.info(f"Total errors found: {errorcount}")

checklogs()