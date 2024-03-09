<sub>*Copyright 2024, Paul T. Miller > For Academic Use  
Gemma folder Copyright 2024 Google distributed under Apache License, V2</sub> 

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
## Methods to run
Code is provided to test gemma models on a local computer. Three methods are provided:

+ Jupyter Notebook (pytorch_gemma.ipynb)
+ Web UI (python3 web.py)
+ Command line (python3 main.py)

*** 
## Modify the parameters as desired
The output_size indicates the max you allow for model output.  
Version options are '2b', '2b-it', '7b', 7b-it'. The 'it' in name indicates a pre-trained model.   
Machine - use 'cuda' if you have cuda installed with an Nvidia GPU, otherwise use 'cpu'.  
Download the desired model from https://www.kaggle.com/models/google/gemma/frameworks/pyTorch.  
Recommend starting with 2b-it. (Worked on simple laptop with RTX2060 6GB VRAM).  
Extract contents from the downloaded archive.tar.gz and put the files under the 'model/\<version\>/' folder.  
