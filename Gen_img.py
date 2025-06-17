import os
import openai as op
import pyautogui

def gen_image():
    op.api_key = "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"
    user_input = input("Write you prompt Here:")

    respone = op.Image.create(
        prompt = user_input,
        n=1,
        size="1024x1024"
    )

    image_uri = respone['data'][0]['url']
    print(image_uri)
gen_image()