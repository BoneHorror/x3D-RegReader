import winreg

LOCATION = winreg.HKEY_LOCAL_MACHINE
PERMISSIONS = winreg.KEY_READ
#try:
RYZEN_REGISTRY = r"SYSTEM\\CurrentControlSet\\Services\\amd3dvcache\\Preferences\\App"
#except Exception as err:
#    print(f"An error occurred while trying to open the specified registry key: {err}")
#    exit(-1)

#Logging
LOGFILE = "x3DReg.log"
RESET_COLOR = "\033[0;0m"
class log_color:
    def __init__(self) -> None:
        self.red = "\033[0;31m"
        self.yellow = "\033[0;33m"
        self.gray = "\033[0;30m"
        self.green = "\033[0;32m"
        self.clear = "\033[0;0m"
#UI buttons
TITLE_WINDOW = "x3D RegReader"
TITLE_HEADER = "vcache Optimizer Registry Entries"
TITLE_MODE0 = "Frequency"
TOOLTIP_MODE0 = "This application will try to exclusively use CCD1 frequency cores"
TITLE_MODE1 = "x3D Cache"
TOOLTIP_MODE1 = "This application will try to exclusively use CCD0 cores with extra v-cache"
BUTTON_MODE = "Toggle mode"
BUTTON_ADD = "Add application"
BUTTON_RMV = "Remove"
TOOLTIP_RMV = "Remove this preference override from registry"
#Support for power mode overrides?
