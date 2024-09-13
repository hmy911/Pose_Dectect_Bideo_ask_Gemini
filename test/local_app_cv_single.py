# pip install google-generativeai
# python -m pip install --upgrade pip

import os
import google.generativeai as genai
from PIL import Image

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

mygoogleapikey = 'AIzaSyDmbIadSL9Ot8CCH1ilPlOdBgO41-MXr-Q'
genai.configure(api_key= mygoogleapikey)

model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

myinput = '請問畫面中人物在做什麼 , 請最簡單回答 如: Squart, Jump, Pullup, Pushup, Run, Walk, Rest'
myimage = 'video/pullout00.png'
a = get_gemini_response(myinput, myimage)
print(a)
