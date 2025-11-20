# gradio_app.py
import gradio as gr
from summarize import get_summarizer, summarize_long_text

MODEL = 'facebook/bart-large-cnn'


summarizer = None


def load():
	global summarizer
	if summarizer is None:
		summarizer = get_summarizer(MODEL, device=-1)
	return 'Model loaded'


def summarize_input(text, min_len, max_len):
	if not text:
		return 'No input provided.'
	return summarize_long_text(summarizer, text, min_length=min_len, max_length=max_len)



demo = gr.Blocks()
demo = gr.Blocks()
with demo:
	gr.Markdown('# Hugging Face Document Summarizer')
	with gr.Row():
		txt = gr.Textbox(lines=15, placeholder='Paste or type your article here...')
		with gr.Column():
			min_l = gr.Slider(50, 300, value=150, label='Min length')
			max_l = gr.Slider(100, 600, value=300, label='Max length')
			btn = gr.Button('Summarize')
			load_btn = gr.Button('Load model')
	out = gr.Textbox(lines=15, label='Summary')

	load_btn.click(fn=load, inputs=None, outputs=None)
	btn.click(fn=summarize_input, inputs=[txt, min_l, max_l], outputs=out)

if __name__ == '__main__':
	demo.launch()