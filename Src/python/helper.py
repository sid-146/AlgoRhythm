from datetime import datetime
import random
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


def random_array(size, **kargs):
    message = ""
    """
        Function Returns randomly generated array for given size
        Takes optional args Reverse (Boolean) which returns reversed sorted list
    """
    array_list = []
    
    reverse = kargs.get('Reverse', 0)
    is_sorted = kargs.get('is_sorted', 0)

    try:
        array_list = [random.randint(15, 999999) for i in range(size)]
        
        if reverse != 0 or reverse != False:
            array_list.sort(reverse=True)

        if is_sorted != 0 or is_sorted != False:
            array_list.sort()
        
        return array_list

    except Exception as err:
        error = "" 
        message 
        
        return False