
def rfm_widgets(rfm_df, format_currency, st, plt, sns):
    col1,col2,col3 = st.columns(3)

    with col1:
        avg_recency = round(rfm_df.recency.mean(),1)
        st.metric("Average Recency (days)", value=avg_recency)

    with col2: 
        avg_frequency = round(rfm_df.frequency.mean(), 2)
        st.metric("Average Frequency", value=avg_frequency)

    with col3:
        avg_frequency = format_currency(rfm_df.monetary.mean(), "AUD", locale='es_CO') 
        st.metric("Average Monetary", value=avg_frequency)

    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

    colors = ["#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4", "#72BCD4"]

    sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel('customer_id')
    ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
    ax[0].tick_params(axis ='x', labelsize=15)
    ax[0].set_xticklabels(ax[0].get_xticklabels(), rotation=90)
    ax[0].set_xticks([])


    sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel('customer_id')
    ax[1].set_title("By Frequency", loc="center", fontsize=18)
    ax[1].tick_params(axis='x', labelsize=15)
    ax[1].set_xticklabels(ax[0].get_xticklabels(), rotation=90)
    ax[1].set_xticks([])


    sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=colors, ax=ax[2])
    ax[2].set_ylabel(None)
    ax[2].set_xlabel('customer_id')
    ax[2].set_title("By Monetary", loc="center", fontsize=18)
    ax[2].tick_params(axis='x', labelsize=15)
    ax[2].set_xticklabels(ax[0].get_xticklabels(), rotation=90)
    ax[2].set_xticks([])


    plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=20)
    
    st.pyplot(fig)
