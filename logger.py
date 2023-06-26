import sys
from loguru import logger

LEVEL_FILE = "INFO"
LEVEL_CONSOLE = "DEBUG"


# Очищаем настройки по умолчанию
# logger.remove(0)

# подключаем экранный лог
# logger.add(sys.stderr, level=LEVEL_CONSOLE)

# подключаем лог файл
logger.add("ctimer.log", level=LEVEL_FILE, rotation="10 MB", format="{time:YYYY-MM-DD HH:mm:ss} {function}: {message}")
