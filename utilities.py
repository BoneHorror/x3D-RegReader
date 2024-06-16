import winreg
import logging
from constants import RESET_COLOR, LOCATION, PERMISSIONS, RYZEN_REGISTRY

def match_override(override: int):
    match override:
        case 0:
            return "Frequency"
        case 1:
            return "Cache"

def log_print(text:str, color:str=None, level:int=1):
    if not (type(text) == str): # noqa: E721
        logging.warning(f"Invalid type for text: {type(text)}. Converting to str forcefully")
        text = str(text)
    if color is not None:
        assert type(color) == str # noqa: E721
        print(color+text+RESET_COLOR)
    else:
        print(text)
    match level:
        case 0:
            logging.debug(f"{text}")
        case 1:
            logging.info(f"{text}")
        case 2:
            logging.warning(f"{text}")
        case 3:
            logging.error(f"{text}")
        case 4:
            logging.critical(f"{text}")
            raise Exception(f"{text}")
        
def open_reg_entry(path: str | None = None):
    #combined_path = RYZEN_REGISTRY+path
    if path is None:
        path = ""
    reg_entry = winreg.OpenKeyEx(LOCATION, RYZEN_REGISTRY+path, access=PERMISSIONS)
    return reg_entry