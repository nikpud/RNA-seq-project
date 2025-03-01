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


