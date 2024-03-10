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
        word_count = 250
        if 'selected' in request.form:
            word_count = int(request.form['selected'])

        model.output_len = word_count
        textbox = request.form['user_input']
        processed_text = textbox.upper()
        answer = model.get_response(processed_text)
        return render_template('index.html',
                               question=textbox, answer=answer)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0", port=8080, debug=False)
