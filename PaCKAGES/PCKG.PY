import schedule
import time

def job():
    print("I'm working...")
def inprogress():
    print(" job is in progress")
def completed():
    print("job completed")

schedule.every(10).seconds.do(job)
#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(inprogress)
schedule.every().minute.at(":20").do(completed)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("exiting the program....")
