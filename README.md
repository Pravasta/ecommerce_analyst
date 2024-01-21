# Dicoding Collection Dashboard ✨

## Overview

Project ini merupakan, project untuk kelas "Belajar analisis data menggunakan Python" dari Dicoding Indonesia. Project ini menganalisa data E-commerce yang ada di negara Brazil. Dimana database ini merupakan database public.

## Project Architecture

- 'assets/' : direktori untuk menyimpan Image, Font, Logo, dll
- 'core/' : direktori import data, dan function yang akan dipanggil pada dashboard.py
- 'data/' : direktori penyimpanan dataset
- 'widgets/' : direktori untuk membuat widgets yang akan ditampilkan pada streamlit
- 'dashboard.py/' : file utama untuk merunning project
- 'notebook.ipynb' : file berisi pengolahan data Google Colab
- 'README.md' : berkas ini

## Setup environment

```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run steamlit app

```
cd submission
streamlit run dashboard.py
```

## Data Source

Data ini berasal dari data yang disediakan oleh [Dicoding](https://www.dicoding.com/)
