from googleplaces import GooglePlaces, types, lang
import os


API_KEY = 'AIzaSyDV9ppODUqGD3gMVz4-72G1OAHj9psNn94'



def init(lat, lng, speed):
	place_ref = GooglePlaces(API_KEY)

	geog_zone = {
		'keyword' : ['school', 'hospital'],
		'loc_type' : [[types.TYPE_SCHOOL], [types.TYPE_HOSPITAL]],
		'speed_lim' : ['25', 'nil'],
		'other_lim' : ['nil', 'no_horn']
	}

	os.system('clear')


	place_latlong = {
		'lat': lat,
		'lng': lng
	}


	for num in range(len(geog_zone['keyword'])):
		#nearby search based on current location
		query_result = place_ref.nearby_search(
	        lat_lng = place_latlong, keyword= geog_zone['keyword'][num],
	        radius=500, types = geog_zone['loc_type'][num])

		if query_result.has_attributions:
		    print query_result.html_attributions	

		
		if len(query_result.places) > 0:
			if geog_zone['keyword'][num] == 'school':
				if speed > geog_zone['speed_lim'][num]:
					os.system('play sounds/warning.wav')
					os.system('play sounds/school.wav')
					os.system('play sounds/speed.wav')
			elif geog_zone['keyword'][num] == 'hospital':
				os.system('play sounds/warning.wav')
				os.system('play sounds/hos.wav')
				os.system('play sounds/horn.wav')

		"""
		for place in query_result.places:
		    print place.name
		    print place.geo_location
		    print place.place_id
		    raw_input("Next?")
		"""

def find(coords):
	query_result = place_ref.nearby_search(
	        lat_lng = coords, radius=50)
	
	return query_result.places.name



#init(la, lo)

