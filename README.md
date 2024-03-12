## Pytorch specific code to use Google's Gemma AI LLM models on a local computer  
  
<sub>*Copyright 2024, Paul T. Miller > For Academic Use  
*Gemma folder Copyright 2024 Google distributed under Apache License, V2</sub> 

<sub>Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at*</sub>

<sub>**http://www.apache.org/licenses/LICENSE-2.0**</sub>

<sub>*Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.*</sub>
  
***
# Get started
## Install the latest NVIDIA system driver https://www.nvidia.com/download/index.aspx
#### If you wish to add cuda and cudnn to your system:
##### https://developer.nvidia.com/cuda-downloads
##### https://developer.nvidia.com/cudnn-downloads
  
## Install torch with cuda support (https://pytorch.org/get-started/locally/)
For Windows: 
+ pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
+ pip3 install immutabledict sentencepiece Flask
  
For Linux: 
+ pip3 install torch torchvision torchaudio immutabledict sentencepiece Flask
+ pip3 install immutabledict sentencepiece Flask
  
Or install using Conda with: 
+ conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
  
***
## Methods to run
Code is provided to test gemma models on a local computer. Three methods are provided:

+ Jupyter Notebook (pytorch_gemma.ipynb)
+ Web UI (python3 web.py)
+ Command line (python3 main.py)

*** 
## Modify the parameters as desired
+ The output_size indicates the max you allow for model output.  
+ Version options are '2b', '2b-it', '7b', 7b-it'. The 'it' in name indicates an instruction-tuned model.  
+ Machine - use 'cuda' if you have cuda installed with an Nvidia GPU, otherwise use 'cpu'.  
+ Download the desired model from https://www.kaggle.com/models/google/gemma/frameworks/pyTorch.   
+ Recommend starting with 2b-it. (Worked on a simple laptop with RTX2060 6GB VRAM).  
+ Extract contents from the downloaded archive.tar.gz and put the files under the 'model/\<version\>/' folder.  

  <img src="models/2b_it_pic.png">

***
## Recommended
The code in this repository was tested with python 3.10, and Nvidia driver version 550.54.14.

  

