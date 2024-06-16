import winreg
from constants import RYZEN_REGISTRY, log_color
from utilities import match_override, open_reg_entry, log_print

color = log_color()

def app_values(app: str, close=True):
    local_entry = open_reg_entry(app)
    query = winreg.QueryInfoKey(local_entry)
    log_print(query, color.gray, level=0) #info readout of RYZEN_REGISTRY

    application, _= winreg.QueryValueEx(local_entry, "EndsWith")
    override, _ = winreg.QueryValueEx(local_entry, "Type")
    override = match_override(override)

    log_print(f"The application with override is: {color.yellow}{application}{color.clear}\nIts override is set to: {color.yellow}{override}{color.clear}")
    if local_entry:
        if close:
            winreg.CloseKey(local_entry)
        else:
            return local_entry
    else:
        log_print("Lost track of registry entry, aborting", color.red, 5)
    

def get_subkeys(key): #get all folders with specific games... as list?
    iters = 0
    key_list = []
    log_print(f"Getting subkeys from key: {key}", color.yellow)
    try:
        while True:
            subkey = winreg.EnumKey(key, iters)
            iters += 1
            log_print(subkey, color.gray)
            key_list.append(subkey)
    except WindowsError as err:
        log_print(err, color.red, 0)
    return key_list

example = r"\\League of Legends"
regentry = app_values(example, close=False)
baseentry = open_reg_entry()
list = get_subkeys(baseentry)
for item in list:
    print(item)