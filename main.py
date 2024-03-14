from pytorch_gemma  import GemmaModel

# Modify the parameters below as desired.
# output_len indicates the number of words max you allow for model output.
# version options are '2b', '2b-it', '7b', 7b-it'. 'it' indicates an instruction-tuned model.
# Machine - use 'cuda' if you have cuda installed with your Nvidia GPU, otherwise use 'cpu'
# Download the desired model from https://www.kaggle.com/models/google/gemma/frameworks/pyTorch
# Unzip the downloaded archive.tar.gz and put the files under the "model/<version>/" folder
model = GemmaModel(output_len=250, version='2b-it', machine='cuda')

# Advanced - customize the following, if you wish
# https://ivibudh.medium.com/a-guide-to-controlling-llm-model-output-exploring-top-k-top-p-and-temperature-parameters-ed6a31313910
# https://medium.com/@daniel.puenteviejo/the-science-of-control-how-temperature-top-p-and-top-k-shape-large-language-models-853cb0480dae
model.temperature = 0.95
model.top_p = 1.0
model.top_k = 100

# get user input
model.get_input()
