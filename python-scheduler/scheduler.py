import schedule   # Library used to schedule tasks at specific intervals
import time       # Library used to pause the program for some time

# Function that will check the logs file for errors
def checklogs():
    # Open the file 'logs.txt' in read mode
    with open('logs.txt') as file:
        
        # Loop through each line in the file
        for line in file:
            
            # Check if the word 'ERROR' exists in the line
            if 'ERROR' in line:
                
                # Print the line where the error was found
                print('Error found:', line)


# Schedule the function 'checklogs' to run every 10 seconds
schedule.every(10).seconds.do(checklogs)


# Infinite loop to keep the program running
while True:
    
    # Run any scheduled tasks that are pending
    schedule.run_pending()
    
    # Pause the program for 1 second to prevent high CPU usage
    time.sleep(1)