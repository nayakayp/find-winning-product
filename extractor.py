import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

print(os.getenv("OPENAI_API_KEY"))
model = "text-davinci-003"
product_title = "BEIENS KUNCI PENGAMAN LACI PINTU LEMARI KULKAS SAFETY LOCK BABY"

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

main_product("SPEEDS Meja Gambar Anak Proyektor Meja Belajar Proyektor Anak 025-3")