import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to my practise streamlead')

from bs4 import BeautifulSoup
import pandas as pd, os, glob

import requests, time, os

# genres to fetch
genres = {
    "mystery": "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "poetry": "http://books.toscrape.com/catalogue/category/books/poetry_23/index.html",
    "science": "http://books.toscrape.com/catalogue/category/books/science_22/index.html"
}

# ensure folder exists
os.makedirs("reports/Week_5/data/raw", exist_ok=True)

# download & save each genre
for label, url in genres.items():
    filename = f"data_test/{label}-{time.strftime('%Y%m%d-%H%M%S')}.html"
    resp = requests.get(url)
    with open(filename, "wb") as f:
        f.write(resp.content)
    print(f"Saved {label} HTML to {filename}")



all_books = []

# go through all downloaded HTML files
for filepath in glob.glob("data_test/*.html"):
    label = os.path.basename(filepath).split("-")[0]  # we know that filenames start with genre
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    titles = [a["title"] for a in soup.find_all("a") if a.get("title")]
    
    for t in titles:
        all_books.append({"title": t, "label": label})

# save processed dataset
os.makedirs("data_test/processed", exist_ok=True)
df = pd.DataFrame(all_books)
st.st.dataframe(df)



