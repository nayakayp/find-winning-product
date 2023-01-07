import pandas as pd
pd.set_option("display.max_rows", None)

df=pd.read_csv('dataset/cleaned/Mainan _ Aktivitas Bayi.csv')

df_lower_case = df['Main Product Name'].str.lower()
df_no_extra_words_1 = df_lower_case.str.replace('main product: ','')
df_no_extra_words_2 = df_no_extra_words_1.str.replace('the main product is a ','')
df_no_extra_words_3 = df_no_extra_words_2.str.replace('main product ','')
df_no_punctuation = df_no_extra_words_3.str.replace('[^\w\s]','')

print(df['Main Product Name'].value_counts())

# CLEANING STEP BEFORE CLASSIFY
# 1. Lowercase all words
# 2. Remove punctuation
# 3. Remove 'Main product: ' string
# 4. Remove \n
