from dotenv import load_dotenv
load_dotenv()  # loading all the envrionment variables from the .env file

import gradio as gr
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input, image):
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text

# Define the Gradio interface
iface = gr.Interface(
    fn=get_gemini_response,
    inputs=[
        gr.Textbox(label="Enter your question here:"),
        gr.Image(label="Choose an image...", type="pil"),
        # gr.Video(label="Choose an video...", type="pil"),        
    ],
    outputs=gr.Textbox(label="The response is"),
    title="Gemini Multimodal Bot",
    description="Ask Gemini questions about images",
)

# Launch the Gradio interface
iface.launch(share=True)