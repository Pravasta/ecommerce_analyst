import seaborn as sns
sns.set(style='dark')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import urllib
import streamlit as st
from babel.numbers import format_currency
from core.data_import import all_df, location_df, maps_df
from core.data_df_function import month_order, sum_order, rfm, mapping
from widgets.slider_widgets import slider_widgets
from widgets.header_widget import header_widget
from widgets.order_month_widget import month_order_widget
from widgets.sum_order_widget import best_worst_perform_product
from widgets.rfm_widget import rfm_widgets
from widgets.maps_widget import maps_widget, MapBrazil

if __name__ == '__main__':
    min_date = all_df['order_approved_at'].min()
    max_date = all_df['order_approved_at'].max()

    slider, start_date, end_date= slider_widgets(min_date, max_date)

    main_df = all_df[(all_df['order_approved_at'] >= str(start_date)) & 
                 (all_df['order_approved_at'] <= str(end_date))
                 ]

    month_order_df = month_order(df=main_df)
    sum_order_df = sum_order(df=main_df)
    rfm_df = rfm(main_df)
    location = mapping(df=location_df)

    map_plot = MapBrazil(maps_df, mpimg=mpimg, plt=plt, st=st, urllib=urllib)


    # WIDGET
    # Header
    header_widget(isHeader=True, title='Dashboard Reporting Eccomerce Brazill :sunglasses:')
    
    # Month Widget
    header_widget(isHeader=False, title='Month Order')
    month_order_widget(month_order_df, format_currency, plt=plt, st=st)
    
    # Best Worst Perform
    header_widget(isHeader=False, title='Best & Worst Performing Product')
    best_worst_perform_product(sns=sns, df=sum_order_df, st=st, plt=plt)
    
    # Maps Widget
    header_widget(isHeader=False, title='Jumlah Order By Customer State')
    maps_widget(sns=sns, df=location, plt=plt, st=st)
    
    # Maps Widget
    st.set_option('deprecation.showPyplotGlobalUse', False)
    header_widget(isHeader=False, title='Peta Sebaran pelanggan di Brazil')
    map_plot.mapz_brazil_widgets()
    
    # RFM Parameters
    header_widget(isHeader=False, title='Best Customer based on RFM Parameters')
    rfm_widgets(rfm_df=rfm_df,format_currency=format_currency,
                plt=plt, sns=sns,st=st
                )
    
    st.caption('Copyright (c) Pravasta 2024')


    