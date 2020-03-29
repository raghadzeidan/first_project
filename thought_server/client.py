import time
import math
import sys, socket
import datetime
import logging
from thought import Thought
from utils import Connection
#from utils import Reader
logging.basicConfig(level = logging.DEBUG,
                    filename = '.clientlogs.txt',
                    format = '%(levelname).1s %(asctime)s %(message)s',
                    datefmt = '%Y-%m-%d %H:%M:%S')

#def upload_thought(address, user_id, thought):
#    ip, port = address
#    seconds = int(time.time())
#    timestamp_obj = datetime.datetime.fromtimestamp(seconds)
#    thought_obj = Thought(user_id, timestamp_obj, thought)
#    data = thought_obj.serialize()
#    connection = Connection.connect(ip,port)
#    connection.send(data)
#    connection.close()

    

def upload_thought(ip,port):
    logging.info('sending data')
    connection = Connection.connect(ip,port)
    connection.send(b"abcde")
    connection.close()

#client.py does not support commandline, TODO: consider returning it
def main(argv):
    if len(argv) != 4:
        print(f'USAGE: {argv[0]} <address> <user_id> <thought>')
        return 1
    try:
        upload_thought(argv[1],argv[2],argv[3])
        print('done')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1

if __name__ == '__main__':
    argv = sys.argv
    upload_thought(argv[1], int(argv[2]))
