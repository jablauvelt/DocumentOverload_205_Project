# This code snippet is just used to confirm that Kafka is working
# NOT to be used otherwise
# Although this code is a great way to clean out your kafka queues

from geopy.geocoders import Nominatim
from kafka import KafkaConsumer

consumer = KafkaConsumer('getsome3')
geolocator = Nominatim()

for message in consumer:
	# message value and key are raw bytes -- decode if necessary!
	# e.g., for unicode: `message.value.decode('utf-8')`

	zipcode = message.value

	print(zipcode)

#	location = geolocator.geocode(zipcode)
#	print(filename, location.longitude, location.latitude, location.address)
