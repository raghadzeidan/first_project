from .parsers_main import subscribe
import numpy as np
import matplotlib.pyplot as plt
import pika
import json
import blessings
term = blessings.Terminal()


@subscribe('color_image')
def parse_that_fucking_depth(data):
	dic = json.loads(data)
	publish_depth = {}
	publish_depth['user'] = dic['user']
	publish_depth['datetime'] = dic['datetime']
	
	depth_path = dic['depth_image']['data_path']
	height = dic['depth_image']['height']
	width = dic['depth_image']['width']
	float_array = np.load(depth_path)
	plt.imshow(float_array, cmap='hot', interpolation='nearest')
	user_id = dic['user']['userId']
	datetime = dic['datetime']
	save_path = f'/home/user/Desktop/volume/depth_images/images/{user_id}_{datetime}.png'
	depth_publish['path'] = save_path
	plt.savefig(save_path)
	return json.dumps(publish_depth)

def depth_image_parser_callback(channel, method, properties, body):
	'''a callback for the parsing feelings function.
	PROJECT: this allows decoupiling between MQ and actual parsing function'''
	#extracting from user+snapshot (just like run_parser)
	#consider making them one code
	#extracting..
	to_publish=parse_that_fucking_depth(body)
	channel.exchange_declare('depth_image', exchange_type='fanout')
	channel.basic_publish(exchange='depth_image', routing_key='', body=to_publish)


def depth_image_parser_main(mq):#Consider the initialization to be one-for-all
	print(mq)
	connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
	channel = connection.channel()
	
	channel.exchange_declare('parsers', exchange_type='fanout')
	result = channel.queue_declare(queue='', exclusive=True)
	queue_name = result.method.queue
	channel.queue_bind(exchange = 'parsers', queue = queue_name)
	print('depth_Image parser consuming...')

	channel.basic_consume(queue=queue_name, on_message_callback=depth_image_parser_callback, auto_ack=True)
	channel.start_consuming()
	
