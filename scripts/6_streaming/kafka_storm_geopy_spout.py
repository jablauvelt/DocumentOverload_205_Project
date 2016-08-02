from __future__ import absolute_import, print_function, unicode_literals

from kafka import KafkaConsumer
from streamparse.spout import Spout

class KafkaSpout(Spout):

	def initialize(self, stormconf, context):
		self.consumer = KafkaConsumer('getsome3')
	
	def next_tuple(self):
		for message in self.consumer:
			self.emit([message])

