import logging
import os
from datetime import datetime

# Crear carpeta logs
os.makedirs("logs", exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Archivo: logs/ejecucion_YYYYMMDD.log
filename = datetime.now().strftime("logs/ejecucion_%Y%m%d.log")

# Handler para archivo
file_handler = logging.FileHandler(filename, encoding="utf-8")
file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Handler para consola
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))

# Configurar logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)