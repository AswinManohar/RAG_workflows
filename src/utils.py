import pandas as pd
import string

def clean_text(text):
    """
    Simple text cleaning: lowercase and remove punctuation.
    """
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.split() # Return list of tokens for BM25

def load_data(filepath="data/sample_food_data_base.csv"):
    """
    Loads the food database and prepares the corpus.
    """
    try:
        df = pd.read_csv(filepath)
        # Create a corpus from food_name and ingredients
        # We'll combine them for better search context
        corpus = []
        for index, row in df.iterrows():
            text = f"{row['food_name']} {row['ingredients']}"
            corpus.append(text)
        return df, corpus
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return None, None
