import schedule
import time

# Function to count errors in logs.txt
def countErrors():
    with open('logs.txt') as file:
        error_count = 0
        
        for line in file:
            if 'ERROR' in line:
                error_count += 1
        
        print(f'Total errors found: {error_count}')

# Run this function every 15 seconds
schedule.every(15).seconds.do(countErrors)

# Infinite loop to keep checking scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)