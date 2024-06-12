class GameEntry:
    def __init__(self, identity: str, folder: str, exe: str, value: int) -> None:
        self.identity = identity
        self.folder = folder
        self.exe = exe
        self.value = value