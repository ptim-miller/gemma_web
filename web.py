from flask import Flask, render_template
from flask import request
from pytorch_gemma import GemmaModel

app = Flask(__name__, template_folder='templates', static_folder='static')
# Modify the parameters below as desired.
# output_len indicates the max you allow for model output.
# version options are '2b', '2b-it', '7b', 7b-it'. 'it' indicates an instruction-tuned model.
# Machine - use 'cuda' if you have cuda installed with your Nvidia GPU, otherwise use 'cpu'
# Download the desired model from https://www.kaggle.com/models/google/gemma/frameworks/pyTorch
# Unzip the downloaded archive.tar.gz and put the files under the "model/<version>/" folder
model = GemmaModel(output_len=250, version='2b-it', machine='cuda')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        words = int(request.form['words'])
        temp = float(request.form['temp'])
        top_p = float(request.form['top_p'])
        top_k = int(request.form['top_k'])
        model.output_len = words
        model.temperature = temp
        model.top_p = top_p
        model.top_k = top_k
        textbox = request.form['user_input']
        processed_text = textbox.upper()
        answer = model.get_response(processed_text)
        return render_template('index.html',
                               question=textbox, answer=answer,
                               words=words, temp=temp,top_p=top_p,top_k=top_k,
                               )
    else:
        words = 250
        temp = 0.95
        top_p = 1.0
        top_k = 100
        return render_template('index.html',
                               words=words, temp=temp,top_p=top_p,top_k=top_k
                               )


if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0", port=8080, debug=False)
