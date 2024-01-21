
def month_order_widget(df, format_currency, plt, st):
    col1, col2 = st.columns(2)

    with col1:
        total_orders = df.orders_count.sum()
        st.metric("Total orders", value=total_orders)
 
    with col2:
        total_revenue = format_currency(df.revenue.sum(), "AUD", locale='es_CO') 
        st.metric("Total Revenue", value=total_revenue)
    
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(
        df["order_approved_at"],
        df["orders_count"],
        marker='o', 
        linewidth=2,
        color="#90CAF9"
    )
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=15)
    
    st.pyplot(fig)