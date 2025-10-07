# app.py
import gradio as gr
import requests

def call_backend(name):
    url = "https://gradio-backend.onrender.com"
    response = requests.post(url, json={"name": name})
    return response.json().get("message", "Error connecting to backend")

iface = gr.Interface(
    fn=call_backend,
    inputs=gr.Textbox(label="Enter your name"),
    outputs=gr.Textbox(label="Backend Response"),
    title="Hello Vorithm 🌐",
    description="This Gradio app connects to a FastAPI backend!"
)

iface.launch()
