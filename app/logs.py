import sys
import logging

import json_log_formatter

from config import LOG_LEVEL


formatter = json_log_formatter.JSONFormatter()

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logging.basicConfig(level=LOG_LEVEL, handlers=[handler])

logger = logging.getLogger(__name__)
