import os

import pandas as pd
import torch
import wgan
# Hardware setup
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
device = "cuda" if torch.cuda.is_available() else "cpu"

# Loading and sampling data
file = "data/generated/welfare_dropNA.csv"
file

df = pd.read_csv(file)