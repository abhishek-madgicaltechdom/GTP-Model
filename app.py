# # # Import modules
from jwt import encode, decode
import pickle
import uvicorn
import numpy as np
import nest_asyncio
import pandas as pd
from pyngrok import ngrok
from fastapi import FastAPI

import generate_unconditional_samples as ramdom
import interactive_conditional_samples as generate
# ngrok authtoken 24zyc8WUC4XXyTTYEUVxDxh0frC_3VpHZNCrnuEzLs9DszktT

##### Create the app
app = FastAPI()
##### Home route
@app.get('/')
def index():
    return {'message': 'Hello World, This text generation model'}

@app.get('/random_text')
def text():
  output = ramdom.random_text()
  return {
      'text': output
  }
##### Make a prediction from the passed JSON data and return the predicted Bank Note with the confidence
@app.post('/text')
def text_generate(input_text):
        print(input_text, "input")
        output = generate.interact_model(input_text)
        return {
            'text': f'{input_text}' + ' ' + f'{output}'
        }
        

##### Run the API with uvicorn
if __name__ == '__main__':
    print('Initiated')
    ngrok_tunnel = ngrok.connect(8000)
    print('Public URL:', ngrok_tunnel.public_url)
    nest_asyncio.apply()
    uvicorn.run(app, port=8000)
