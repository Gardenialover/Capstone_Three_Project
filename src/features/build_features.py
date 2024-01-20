import pandas as pd
import numpy as np
from config import DTYPES



def read_tsv_file(file_path):
    try:
        df = pd.read_csv(file_path, delimiter='\t', index_col= False)
        df.rename(columns ={"Unnamed: 0": "id"}, inplace = True)
        return df
    except FileNotFoundError:
        print("File not found, please check the file path.")
        return None
 

# def column_data_types(df, dtypes):
#         """Update column data types in a dataframe"""
#         for col, dtype in dtypes.items():
#             if col in df.columns:
#                 df[col]=df[col].astype(dtype)
#         return df
                
                
        