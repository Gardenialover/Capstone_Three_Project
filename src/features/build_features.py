import pandas as pd
import numpy as np
from config import DTYPES
import spacy
import nltk
import re
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
from textblob import TextBlob
import contractions 
import inflect

def read_tsv_file(file_path):
    try:
        df = pd.read_csv(file_path, delimiter='\t', index_col= False)
        df.rename(columns ={"Unnamed: 0": "id"}, inplace = True)
        return df
    except FileNotFoundError:
        print("File not found, please check the file path.")
        return None

# def remove_special_characters(text):
#     text = text.lower()
#     text = text.replace('&#039', '').replace('\n','').replace('\r', '')
#     text = text.replace(r'[^\w\d\s]',' ')
#     pattern = re.compile(r'[^a-zA-z0-9\s]+')
#     cleaned_text = re.sub(pattern, '', str(text))
#     cleaned_text =' '.join(word.strip() for word in cleaned_text.split())
#     return cleaned_text   


# # convert number into words
# def convert_number(text):
#     p = inflect.engine()
#     temp_text = text.split()
#     new_text = []
#     for word in temp_text:
#         if word.isdigit():
#             temp = p.number_to_words(word)
#             new_text.append(temp)
#         else:
#             new_text.append(word)
#     temp_text = ' '.join(new_text)
#     return temp_text

# def expand_contractions(text):
#     cleaned_text = contractions.fix(text)
#     return cleaned_text

# def remove_whitespace(text):
#     return ' '.join(text.split())



        