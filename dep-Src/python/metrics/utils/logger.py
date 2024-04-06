import logging
import datetime
import os
# temp import
# import helpers

def get_logger(path, event=""):
    """
        path : current directory path (use get_path function in helpers)
        event is optional but it helps to organize your logs according to your run
    """
    date = datetime.datetime.now()
    print(path)
    # os.makedirs(path, exist_ok=True)
    if event == "":
        path = f"{path}\Logs"
        os.makedirs(path, exist_ok=True)
        filename = f"{path}\Log_file_{date.strftime('%Y_%m_%d_%H_%M_%S')}.log"
    else:
        print("running else")
        path = f"{path}\Logs\{event}"
        print("Updated path ",path)
        os.makedirs(path, exist_ok=True)
        filename = f"{path}\Log_file_{date.strftime('%Y_%m_%d_%H_%M_%S')}.log"

    # logger 
    _format = "%(funcName)s - %(asctime)s - %(levelname)s: %(message)s"
    logging.basicConfig(filename=filename, level=logging.DEBUG, format=_format)
    logger = logging.getLogger()
    print('logger Created')
    logger.addHandler(logging.StreamHandler())

    return logger
