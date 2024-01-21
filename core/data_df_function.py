import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

def month_order(df):
    month_order_df = df.resample(rule='M', on='order_approved_at',).agg({
       'order_id': 'nunique',
        'price': 'sum'
    })

    month_order_df.index = month_order_df.index.strftime('%B')
    month_order_df = month_order_df.reset_index()

    month_order_df.rename(
        columns={
            'order_id': 'orders_count',
            'price': 'revenue'
        }, inplace=True
    )

    month_order_df = month_order_df.sort_values('orders_count').drop_duplicates('order_approved_at', keep='last')

    month_mapping = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    month_order_df["month_numeric"] = month_order_df["order_approved_at"].map(month_mapping)
    month_order_df = month_order_df.sort_values("month_numeric")
    month_order_df = month_order_df.drop("month_numeric", axis=1)

    return month_order_df

def sum_order(df):
    sum_order_df = df.groupby("product_category_name_english").product_id.count().sort_values(ascending=False).reset_index()

    sum_order_df.rename(
        columns={
            'product_id': 'order_count'
        }, inplace=True
    )

    return sum_order_df

def rfm(df):
    now=dt.datetime(2018,10,20)

    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    rfm_df = df.groupby(by='customer_id' , as_index=False).agg({
        'order_purchase_timestamp': 'max',
        'order_id': 'count',
        'price': 'sum',
    })

    rfm_df.columns = ['customer_id', 'max_order_timestamp','frequency', 'monetary']

    rfm_df['recency'] = rfm_df['max_order_timestamp'].apply(lambda x: (now -x).days)
    rfm_df.drop('max_order_timestamp', axis=1, inplace=True)

    return rfm_df

def mapping(df):
    by_location_df = df.groupby(by='customer_state').customer_id.nunique().reset_index()
    by_location_df.rename(
        columns={
            'customer_id': 'customer_count',
        }, inplace=True
    )

    top5_states_df = by_location_df.sort_values(by='customer_count', ascending=False).head(5)

    return top5_states_df
  




   