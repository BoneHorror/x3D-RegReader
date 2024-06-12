import winreg

location = winreg.HKEY_LOCAL_MACHINE
permissions = winreg.KEY_READ

try:
    ryzen_registry = winreg.OpenKeyEx(location, r"SYSTEM\\CurrentControlSet\\Services\\amd3dvcache\\Preferences\\App\\League of Legends", access=permissions)
except Exception as err:
    print(f"An error occurred while trying to open the specified registry key: {err}")
query = winreg.QueryInfoKey(ryzen_registry)
print(query)

value_1 = winreg.QueryValueEx(ryzen_registry, "EndsWith")

if ryzen_registry:
    winreg.CloseKey(ryzen_registry)

print(f"The application with override is: {value_1}")