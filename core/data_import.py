import pandas as pd

all_df = pd.read_csv('data/all_data_df.csv')

datetime_columns = ["order_approved_at"]

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

geolocation_df = pd.read_csv('data/geolocation.csv')

geo_customer_df = all_df.groupby(by=['customer_id','customer_unique_id', 'customer_zip_code_prefix', 'customer_state']).order_id.nunique().reset_index()

location_df = pd.merge(
    left=geo_customer_df,
    right=geolocation_df,
    how='left',
    left_on='customer_zip_code_prefix',
    right_on='geolocation_zip_code_prefix'
)

maps_df = location_df.drop_duplicates(subset='customer_unique_id')