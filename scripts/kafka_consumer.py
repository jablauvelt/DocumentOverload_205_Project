# This code snippet is just used to confirm that Kafka is working
# NOT to be used otherwise

from geopy.geocoders import Nominatim
from kafka import KafkaConsumer

consumer = KafkaConsumer('getsome')
geolocator = Nominatim()

for message in consumer:
	# message value and key are raw bytes -- decode if necessary!
	# e.g., for unicode: `message.value.decode('utf-8')`

	filename = message.key
	zipcode = message.value

	location = geolocator.geocode(zipcode)
	print(filename, location.longitude, location.latitude, location.address)
