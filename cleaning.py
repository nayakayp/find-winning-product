import pandas as pd
import time
# from extractor import main_product
# pd.set_option('display.max_colwidth', None)

df = pd.read_csv('dataset/Mainan _ Aktivitas Bayi.csv')

df_renamed= df.rename(columns ={'css89jnbj_URL':'URL','css1bjwylw':'Product Title', "csso5uqvq": "Price", "css1kr22w32":"Merchant", "css1kr22w3":"City", "css153qjw7": "Total Reviews"})
def rupiahToNumber(rp):
    removeCurrency = rp.replace("Rp","")
    removeDots = removeCurrency.replace(".","")
    return int(removeDots)

def formatReviews(rv):
    removeOpenParentheses = str(rv).replace("(","")
    removeCloseParentheses = removeOpenParentheses.replace(")","")
    return removeCloseParentheses

df_renamed['Price'] = df_renamed['Price'].apply(lambda p: rupiahToNumber(p))

df_renamed['Total Reviews'] = df_renamed['Total Reviews'].apply(lambda r: formatReviews(r))
df_renamed['Total Reviews'] = df_renamed['Total Reviews'].replace('nan', '0')
df_renamed['Total Reviews'] = df_renamed['Total Reviews'].astype(int)

clean_df = df_renamed.dropna()
clean_df['Main Product Name'] = pd.Series(dtype='int')
clean_df.to_csv('dataset/cleaned/Mainan _ Aktivitas Bayi.csv', mode='w')