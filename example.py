import os
import pickle as pkl

import numpy as np

from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
from pydeseq2.utils import load_example_data

# Loading synthetic data
counts_df = load_example_data(
    modality="raw_counts",
    dataset="synthetic",
    debug=False,
)

# printing synthetic counts dataframe
print(counts_df)

# loading synthetic metadata for counts dataframe
metadata = load_example_data(
    modality="metadata",
    dataset="synthetic",
    debug=False,
)

# printing synthetic metadata for counts dataframe
print(metadata)


