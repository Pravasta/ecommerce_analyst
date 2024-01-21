def best_worst_perform_product(sns, df, st, plt):
    fig,ax = plt.subplots(nrows=1, ncols=2,figsize=(24,10))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    # Bar sebelah kiri
    sns.barplot(x='order_count', y='product_category_name_english',data=df.head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Penjualan Terbanyak", loc="center", fontsize=15)
    ax[0].tick_params(axis ='y', labelsize=12)

    # Bar sebelah kanan
    sns.barplot(x='order_count',y='product_category_name_english',data=df.sort_values(by='order_count', ascending=True).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Penjualan Terkecil", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)
    
    st.pyplot(fig)