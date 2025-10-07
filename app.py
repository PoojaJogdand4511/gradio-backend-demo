# app.py
import gradio as gr
import requests

# Live backend URL
BACKEND_URL = "https://gradio-backend.onrender.com/process"

def greet(name):
    try:
        response = requests.post(BACKEND_URL, json={"name": name})
        return response.json().get("message")
    except:
        return "Backend not reachable 😞"

with gr.Blocks() as demo:
    gr.Markdown("## Hello Vorithm 👋")
    name_input = gr.Textbox(label="Enter your name")
    output = gr.Textbox(label="Message from Backend")
    submit = gr.Button("Say Hello")
    submit.click(fn=greet, inputs=name_input, outputs=output)

# Run Gradio on port 10001 (Render needs 0.0.0.0)
demo.launch(server_name="0.0.0.0", server_port=10001)
