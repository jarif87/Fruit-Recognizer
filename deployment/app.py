from fastai.vision.all import *
from fastai.vision.all import load_learner
import gradio as gr

fruit_labels = ('Apple', 'Apricot', 'Avocado',
                'Banana', 'Blueberry',
                'Carambola', 'Cherry', 'Fig',
                'Grape', 'Kiwi', 'Lemon',
                'Lychee', 'Mango',
                'Orange', 'Papaya',
                'Pear', 'Pineapple',
                'Raspberry', 'Strawberry', 'Watermelon')

model=load_learner("model/fruit_model_v6.pkl")

def recognize_image(image):
  pred, idx, probs = model.predict(image)
  print(pred)
  return dict(zip(fruit_labels, map(float, probs)))


image = gr.Image()
label = gr.Label()
examples = [
    'test_images/test_0.jpg',
    'test_images/test_1.jpg',
    'test_images/test_2.jpg',
    'test_images/test_4.jpeg'
]

iface = gr.Interface(fn=recognize_image, inputs=image, outputs=label, examples=examples)
iface.launch(inline=False,share=True)