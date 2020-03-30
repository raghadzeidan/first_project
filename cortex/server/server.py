import sys
import logging
#import utils.render as render
#from utils import Connection, Listener
#from thought import Thought, render_from_bytes
import concurrent.futures as cf
import pika
#from parsers_utils.mq import channel
from http.server import HTTPServer, BaseHTTPRequestHandler
HREADS_NUMBER = 5
METADATA_LENGTH = 20

logging.basicConfig(level = logging.DEBUG, 
                filename = '.logs.txt',
                format = '%(levelname).1s %(asctime)s %(message)s)',
                datefmt = '%Y-%m-%d %H:%M:%S')
                
                
class CortextServer(BaseHTTPRequestHandler):
	def do_GET(self):
			#here we should send back the available parsers
			self.send_response(200)
			self.end_headers()
	def do_POST(self):
			content_length = int(self.headers['Content-Length'])
			received_data = self.rfile.read(content_length)
			print(f"Serv - do_Post - {received_data}")
			self.send_response(200)
			self.end_headers()

#def handle_connection(connection):
#    logging.info('Connection handeled')
#    received_bytes = connection.receive(5)
#    client_name = received_bytes.decode('utf-8')
#    color_client_name = "color" + client_name
#    hello_client_name = "hello" + client_name
#    logging.info('publishing to queues')
#    channel.basic_publish(exchange='',routing_key='color_queue',body=color_client_name)
#    channel.basic_publish(exchange='',routing_key='hello_queue',body=hello_client_name)
#    logging.info("{data} this was recieved, at this point the server should do its job".format(data=recieved))
#    logging.info("Server done job.")
    
#def run_server(host, port, publish):
#    logging.info('Server started listening')
#    listener = Listener(port, host)
#    listener.start()
#    executor = cf.ThreadPoolExecutor(THREADS_NUMBER)
#    while True:
#        connection = listener.accept()
#        logging.info('Connection established')
#        executor.submit(handle_connection,connection)

#TODO:bad practice, consider puting them as default args (Server and the serverClass)
def http_run_server(host, port):
	address = (host, int(port))
	httpd = HTTPServer(address, CortextServer)
	logging.info('Starting Context Server.')
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		logging.info('Server Interrupted.')
		pass
	httpd.server_close()
	logging.info('Stopped Server.')
if __name__ == '__main__':
    host = sys.argv[1]
    port = sys.argv[2]
    print(host,port,type(host),type(port),"xx")
    dummy = 1
    #run_server(host,int(port), dummy)
    http_run_server(host, int(port))
