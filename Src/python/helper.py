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


def random_array(size,range_start,range_end , **kargs):
    """
        Function Returns randomly generated array for given size
        Args:
            size (int) : Size of array\n
            -optional keyword args\n
            reverse [boolean] : Returns reservely sorted array (default False)\n
            is_sorted (Boolean) : Returns sorted array (Default Fals)
    """
    message = ""
    array = []
    
    reverse = kargs.get('Reverse', 0)
    is_sorted = kargs.get('is_sorted', 0)
    range_start = kargs.get('start',None)
    range_end = kargs.get('end', None)

    try:
        
        if range_start != None:
            if range_end != None:
                array = [random.randint(range_start, range_end) for i in range(size) ]
            else:
                range_end = range_start + 100000
        else:
            array = [random.randint(15, 999999) for i in range(size)]

        if reverse != 0 or reverse != False:
            array.sort(reverse=True)

        if is_sorted != 0 or is_sorted != False:
            array.sort()
        
        return array

    except Exception as err:
        error = "" 
        message 
        
        return False
