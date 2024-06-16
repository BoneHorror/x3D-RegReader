
import logging
from constants import LOGFILE
from window import Window

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', filename=LOGFILE, encoding='utf8', level = logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
    logging.FileHandler(LOGFILE, mode = "w")

    window = Window()
    window.run()