import schedule
import time

def job1():
    print("Job 1 is running")
def job2():
    print("Job 2 is running")

schedule.every(5).seconds.do(job1)
schedule.every(10).seconds.do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)