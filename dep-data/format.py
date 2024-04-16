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

configUpdate = {
    'id':pd.Series(dtype='int64'),
    'source':pd.Series(dtypes= 'str'),
    'run_start':pd.Series(dtypes= np.datetime64),
    'run_end' : pd.Series(dtypes= np.datetime64),
    'run_duration':pd.Series(dtypes= np.datetime64),
    'is_active':pd.Series(dtypes= 'int64'),
    'max_run_date':pd.Series(dtype= np.datetime64)
}

