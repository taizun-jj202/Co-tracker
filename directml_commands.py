# Contains DirectML commands that i require

import torch
import torch_directml

dev = torch_directml.device(0)
print(f"Device in use: {dev.type}")
print(f"Available devices : {torch_directml.device_count()}")
print(f"Default device: {torch_directml.default_device()}")
print(f"Dev name: {torch_directml.device_name(0)}")
print(f"Dev name: {torch_directml.device_name(1)}")
print(f"Torch available: {torch_directml.is_available()}")
print(f"DML available: {torch_directml.is_available()}")

d = (torch_directml.device if torch_directml.is_available() else
     'cuda' if torch.cuda.is_available() else
     'cpu')
tn = torch.tensor([[0,1], [1,2]])
tn.to(dev)
x = torch_directml.context()

print(f'Device in use: {d}, Device name: {torch_directml.device_name(0)}') 