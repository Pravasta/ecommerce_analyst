def maps_widget(sns, df, plt, st):
    fig = plt.figure(figsize=(10, 5))
    colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        x='customer_count',
        y='customer_state',
        data=df,
        palette=colors_,
    )

    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)

    st.pyplot(fig)

class MapBrazil:
    def __init__(self, df, mpimg, plt, st, urllib):
        self.df = df
        self.mpimg = mpimg
        self.plt = plt
        self.st = st
        self.urllib = urllib
    
    def mapz_brazil_widgets(self):
        maps_brazil = self.mpimg.imread(self.urllib.request.urlopen('https://i.pinimg.com/564x/b3/9d/e0/b39de04c19f269d2dbc7b27b0118c7ef.jpg'),'jpg')
        ax = self.df.plot(kind="scatter", x="geolocation_lng", y="geolocation_lat", figsize=(10,10), alpha=0.3,s=0.3,c='blue')
        self.plt.axis('off')
        self.plt.imshow(maps_brazil, extent=[-73.98283055, -33.8,-33.75116944,5.4])
        self.st.pyplot()