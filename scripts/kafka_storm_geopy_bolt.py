from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
from geopy.geocoders import Nominatim
import psycopg2
import time

geolocator = Nominatim()

conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

class GeopyBolt(Bolt):

	def initialize(self, conf, ctx):
		self.counts = Counter()

	def process(self, tup):

		time.sleep(60)
		filename = tup.values[0]['key']
		zipcode = tup.values[0]['value']
		location = geolocator.geocode(zipcode)

		self.log(filename)
		self.log(location.longitude)

		try:
			cur.execute("update zipcode_filename set longitude=%s, latitude=%s where filename=%s and zipcode=%s", (location.longitude, location.latitude, filename, zipcode))
			conn.commit()
		except:
			self.log("No Data Found: " + zipcode)

conn.commit()
conn.close()
