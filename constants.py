import winreg

LOCATION = winreg.HKEY_LOCAL_MACHINE
PERMISSIONS = winreg.KEY_READ
try:
    RYZEN_REGISTRY = winreg.OpenKeyEx(LOCATION, r"SYSTEM\\CurrentControlSet\\Services\\amd3dvcache\\Preferences\\App\\League of Legends", access=PERMISSIONS)
except Exception as err:
    print(f"An error occurred while trying to open the specified registry key: {err}")
    exit(-1)