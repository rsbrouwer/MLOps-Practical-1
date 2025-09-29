!pip install streamlit
!pip install pandas 
!pip install np
!pip install bs4
!pip install os
!pip install glob

import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to my practise streamlead')

from bs4 import BeautifulSoup
import pandas as pd, os, glob

all_books = []

# go through all downloaded HTML files
for filepath in glob.glob("reports/Week_5/data/raw/*.html"):
    label = os.path.basename(filepath).split("-")[0]  # we know that filenames start with genre
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    
    soup = BeautifulSoup(html, "html.parser")
    titles = [a["title"] for a in soup.find_all("a") if a.get("title")]
    
    for t in titles:
        all_books.append({"title": t, "label": label})

# save processed dataset
os.makedirs("reports/Week_5/data/processed", exist_ok=True)
df = pd.DataFrame(all_books)
df.to_csv("reports/Week_5/data/processed/books.csv", index=False)

print(f"Saved {len(df)} books into reports/Week_5/ data/processed/books.csv")
