from datetime import datetime, timedelta
import schedule
import time
import APIs.Aggregation as ag 


def job():
    now = datetime.now() # This condition will only allow the function to insert data at 13:00
    ag.insert_idx_data()

# Schedule the job to run every second
schedule.every(1).seconds.do(job)

# Calculate end time 1 hour from now
end_time = datetime.now() + timedelta(hours=2)

# Run the scheduler until the current time is less than the end time
while datetime.now() < end_time:
    schedule.run_pending()
    time.sleep(1)