import pandas as pd

df = pd.read_csv('output_file.csv')
df['server_time'] = pd.to_datetime(df['server_time'])

start_time = '2024-02-13 12:00:00'
end_time = '2024-02-13 13:00:00'

filtered_df = df[(df['server_time'] >= start_time) & (df['server_time'] < end_time)]
filtered_df['volume_change'] = df['volume'].diff()

df = filtered_df[['id','server_time', 'last_price','volume', 'volume_change', 'source']]
df['server_time'] = pd.to_datetime(df['server_time'])

df.set_index('server_time', inplace=True)

five_min_intervals = df.resample('5T')
median_volumes = five_min_intervals['volume'].median()

prices_at_median_volume = []

for interval_start, median_volume in median_volumes.items():
    interval_data = df[(df.index >= interval_start) & (df.index < (interval_start + pd.Timedelta(minutes=5)))]
    closest_row = interval_data.iloc[(interval_data['volume'] - median_volume).abs().argsort()[0]]
    prices_at_median_volume.append((interval_start, closest_row['last_price']))

prices = [price for _, price in prices_at_median_volume]
average_price = sum(prices) / len(prices)
print(average_price)