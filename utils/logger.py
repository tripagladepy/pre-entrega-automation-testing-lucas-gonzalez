import logging
import os
from datetime import datetime

# Crear carpeta logs
os.makedirs("logs", exist_ok=True)

# Formato
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"

# Archivo: logs/ejecucion_YYYYMMDD.log
filename = datetime.now().strftime("logs/ejecucion_%Y%m%d.log")

logging.basicConfig(
    filename=filename,
    level=logging.INFO,
    format=LOG_FORMAT
)

logger = logging.getLogger()