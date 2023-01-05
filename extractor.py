import os
import openai
import pandas as pd
import numpy as np
import time

openai.api_key = os.getenv("OPENAI_API_KEY")

model = "text-davinci-003"
clean_df = pd.read_csv('dataset/cleaned/Mainan _ Aktivitas Bayi.csv')

def generate_prompt(product_title):
    return """Without your explanation, extract the main product from this product title in english: 
    {}""".format(product_title.capitalize())

def main_product(product_title):
    response = openai.Completion.create(
        model=model,
        prompt=generate_prompt(product_title),
        temperature=0.6,
    )
    return response.choices[0].text 


# Openai: extract main product title for every rows ['Product Title']
print("Start extracting main product title...")
for i,x in enumerate(clean_df['Product Title']):
    is_nan = clean_df['Main Product Name'].isnull()[i]
    if i <= clean_df.shape[0]:
        if(is_nan == True):
            print(f"{i}. {x} ---> {main_product(x).strip()}")
            clean_df['Main Product Name'][i] = main_product(x).strip()
            clean_df.to_csv('dataset/cleaned/Mainan _ Aktivitas Bayi.csv', mode='w')
            time.sleep(5)

# print(clean_df)