import logging

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def divide(a,b):
    try:
        result = a / b
        logging.info(f"Divided {a} by {b} successfully. Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Error dividing {a} by {b}: {e}")

divide(10, 2)
divide(10, 0)