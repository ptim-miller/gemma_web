#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import torch
from gemma import config, model
import warnings

warnings.filterwarnings("ignore")


# create class
class GemmaModel:
    def __init__(self, output_len=50, version='2b-it', machine='cuda'):
        self.output_len: int = output_len
        self.temperature: float = 0.95
        self.top_p: float = 1.0
        self.top_k: int = 100
        self.version = version  # ['2b', '2b-it', '7b', '7b-it']
        self.machine = machine  # ['cuda', 'cpu']
        self.local_dir = f'./models/{version}'
        self.tokenizer_path = os.path.join(self.local_dir, 'tokenizer.model')
        self.ckpt_path = os.path.join(self.local_dir, f'gemma-{version}.ckpt')
        if '2b' in self.version:
            self.model_config = config.get_config_for_2b()
        else:
            self.model_config = config.get_config_for_7b()
        self.model_config.tokenizer = self.tokenizer_path
        torch.set_default_dtype(self.model_config.get_dtype())
        self.device = torch.device(machine)
        self.model = model.GemmaForCausalLM(self.model_config)
        self.model.load_weights(self.ckpt_path)
        self.model = self.model.to(self.device).eval()

    def get_response(self, in_text):
        # print(f"Output limited to {self.output_len} words on a {self.device} device...")
        response = self.model.generate(
            prompts=in_text,
            device=self.device,
            output_len=self.output_len,
            temperature=self.temperature,
            top_p=self.top_p,
            top_k=self.top_k
        )
        return response

    def get_input(self):
        print("Hello HUMAN!!!")
        while True:
            request = input('What is your question or request? (q to quit): ')
            if request != 'q':
                print(self.get_response(request))
                continue
            else:
                print(f'You entered {request} : exiting now!')
                break
