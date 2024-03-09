from pytorch_gemma import GemmaModel

# Modify the parameters below as desired.
# output_len indicates the number of words max you allow for model output.
# version options are '2b', '2b-it', '7b', 7b-it'. 'it' indicates an instructor trained model.
# Machine - use 'cuda' if you have cuda installed with your Nvidia GPU, otherwise use 'cpu'
# Download the desired model from https://www.kaggle.com/models/google/gemma/frameworks/pyTorch
# Unzip the downloaded archive.tar.gz and put the files under the "model/<version>/" folder
model = GemmaModel(output_len=250, version='2b-it', machine='cuda')
model.get_input()
