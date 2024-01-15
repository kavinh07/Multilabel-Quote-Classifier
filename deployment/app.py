import gradio as gr
import onnxruntime as rt
from transformers import AutoTokenizer
import torch, json

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

with open("tag_types_encoded.json", "r") as fp:
  encode_tag_types = json.load(fp)

tags = list(encode_tag_types.keys())

inf_session = rt.InferenceSession('quote-classifier-quantized.onnx')
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

def classify_quote_tag(description):
  input_ids = tokenizer(description)['input_ids'][:512]
  logits = inf_session.run([output_name], {input_name: [input_ids]})[0]
  logits = torch.FloatTensor(logits)
  probs = torch.sigmoid(logits)[0]
  return dict(zip(tags, map(float, probs))) 

label = gr.outputs.Label(num_top_classes=5)
iface = gr.Interface(fn=classify_quote_tag, inputs="text", outputs=label)
iface.launch(inline=False)