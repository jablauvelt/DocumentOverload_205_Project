from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
from geopy.geocoders import Nominatim
import psycopg2
import sys
import time

class GeopyBolt(Bolt):

	def initialize(self, conf, ctx):
		self.counts = Counter()

	def process(self, tup):

		try:

			conn = psycopg2.connect(database="finalproject", user="postgres", password="pass", host="localhost", port="5432")
			cur = conn.cursor()

			geolocator = Nominatim()

			zipcode = str(tup.values[0]['value'])
			location = geolocator.geocode(zipcode)
			latitude = str(location.latitude)
			longitude = str(location.longitude)

			self.log("ZIPCODE: " + zipcode)
			self.log("LONGITUDE: " + longitude)
			self.log("LATITUDE: " + latitude)

			cur.execute("update zipcode_filename set longitude=%s, latitude=%s where zipcode=%s", (longitude, latitude, zipcode))
			conn.commit()
			conn.close()

		except:

			self.log("**********DATA ERRORS**********")
			self.log("ZIPCODE: " + zipcode)
			self.log("SYSTEM ERROR: " + str(sys.exc_info()[0]))
			cur.execute("update zipcode_filename set longitude=%s, latitude=%s where zipcode=%s", ('na', 'na', zipcode))
			conn.commit()
			conn.close()

		time.sleep(60)
