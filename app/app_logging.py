import sys
import logging

import json_log_formatter

import app.config

level = app.config.LOG_LEVEL.upper()

formatter = json_log_formatter.JSONFormatter()

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logging.basicConfig(level=level, handlers=[handler])

logger = logging.getLogger(__name__)
