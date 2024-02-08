from datetime import datetime, timedelta
import schedule
import time
import APIs.Aggregation as ag 



def job():
    now = datetime.now()
    if now.hour==13:
        ag.insert_idx_data()


# Schedule the job every minute to check if it's within the desired time frame
schedule.every().minute.at(":00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)