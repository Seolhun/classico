import logging.config

from flask import json

# Setting Logging
with open('logging.json', 'rt') as f:
    config = json.load(f)
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)
