# print("Hello Mike. Today is Monday, 22 September 2025.")

# Ran this to install PyTorch:
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129

# Ran this to install the packages listed in requirements.txt:
# pip install -r requirements.txt

# Ran this to update pip:
# python -m pip install --upgrade pip

import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
