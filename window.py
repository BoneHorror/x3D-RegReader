import PySimpleGUI as gui
from utilities import log_print
from constants import * #TODO temp

class Window():
    def __init__(self):
        layout = [[gui.Push(), gui.Text(TITLE_HEADER, font=("Helvetica", 12, "bold")), gui.Push()],
                [gui.Column(scrollable=True, vertical_scroll_only=True, layout=
                    [[gui.Text(TITLE_MODE0)]] #TODO generate based on entry iteration
                    )],
                [gui.Push(), gui.Button(BUTTON_MODE), gui.Button(BUTTON_ADD), gui.Push()]
        ]
        self.window = gui.Window(TITLE_WINDOW, layout, resizable=True)

    def run(self):
        while True:
            event, values = self.window.read()
            if event == gui.WIN_CLOSED:
                log_print("x3D RegReader Shutting Down")
                break
            log_print(f"\033[0;30mExecuting event: {event}...\033[0;0m")