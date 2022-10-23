import numpy as np
from numpy import dtype
import pandas as pd

runAudit = {
    'run_id' :pd.Series(dtype='int64'),
    'algorithm_name': pd.Series(dtype='str'),
    'run_start' : pd.Serise(dtype = np.datetime64),
    'run_end' : pd.Serise(dtype = np.datetime64),
    'run_duration' : pd.Series(dtyoe = np.datetime64)

}
