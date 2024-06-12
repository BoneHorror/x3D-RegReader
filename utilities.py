import winreg

def match_override(override: int):
    match override:
        case 0:
            return "Frequency"
        case 1:
            return "Cache"
        
def get_subkeys(): #get all folders with specific games... as list?
    pass