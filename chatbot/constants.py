from pathlib import Path

CWF = Path(__file__)

PROJECT_PATH = str(CWF.parent.parent) + '/'
DATA_PATH = f"{PROJECT_PATH}data/"
RESULT_PATH = f"{PROJECT_PATH}results/"
CKPT_PATH = f"{PROJECT_PATH}ckpt/"