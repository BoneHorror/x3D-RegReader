import winreg
from constants import RYZEN_REGISTRY
from utilities import match_override

query = winreg.QueryInfoKey(RYZEN_REGISTRY)
print(query) #info readout of RYZEN_REGISTRY

application, _= winreg.QueryValueEx(RYZEN_REGISTRY, "EndsWith")
override, _ = winreg.QueryValueEx(RYZEN_REGISTRY, "Type")
override = match_override(override)

if RYZEN_REGISTRY:
    winreg.CloseKey(RYZEN_REGISTRY)

print(f"The application with override is: {application}\nIts override is set to: {override}")
