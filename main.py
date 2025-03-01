import os
import pickle as pkl
import pandas as pd
from pydeseq2.dds import DeseqDataSet
from pydeseq2.default_inference import DefaultInference
from pydeseq2.ds import DeseqStats
from pydeseq2.utils import load_example_data

# load count data from airway_scaledcounts csv file
counts_df = pd.read_csv('airway_scaledcounts.csv')
print(counts_df)

# load count data from airway_metadata csv file
metadata = pd.read_csv('airway_metadata.csv')
print(metadata)

# need to convert counts data from floats to integers

# get list of sample names
samples = counts_df.columns.values
print(samples, type(samples))

# convert ndarray to list
samples = samples.tolist()
print(samples)

# remove element that is not a sample name
samples.pop(0)
print(samples)

# convert columns (samples) to int
for sample in samples:
    counts_df = counts_df.astype({sample:'int'})

print(counts_df)

inference = DefaultInference(n_cpus=4)
dds = DeseqDataSet(
        counts=counts_df,
        metadata=metadata,
        design="~dex",
        refit_cooks=True,
        inference=inference
        )


