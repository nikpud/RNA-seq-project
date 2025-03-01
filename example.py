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


# refit = True not necessary  due to no outliers in synthetic data
inference = DefaultInference(n_cpus=8)
dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design="~condition",  # compare samples based on the "condition"
    # column ("B" vs "A")
    refit_cooks=True,
    inference=inference,
)

print(dds)
