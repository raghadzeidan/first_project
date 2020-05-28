from .client import upload_sample
import logging
logging.basicConfig(level = logging.DEBUG,
                    filename = '.client_logs.txt',
                    format = '%(levelname).1s %(asctime)s %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')
