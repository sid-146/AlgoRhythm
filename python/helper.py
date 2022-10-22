from datetime import datetime
import pandas as pd
import time


def insert_run_records(AlgoName, size):
    """
    This function will insert run records for algorithm for that run

    Args:
    Return:
        Boolean: Indicates success or failure of function
    """
    start_time = time()

    try:
        pass
    except Exception as err:
        error_message = f"|| Error while inserting records in dataframe ||"
        print(err)

    return True