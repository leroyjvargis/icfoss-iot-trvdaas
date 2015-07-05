import location
import store_db
import places
import ir
#import camera
import time

store_db.init("nil", "nil", "Start")
flag = 0;

while True:
	if flag == 0:
		location.init()
		flag = 1;
	else
		location.track()

	if ir.track() == 1:
		loc_coords = location.find()
		loc_name = places.find(loc_coords)
		store_db.init(loc_coords, loc_name, "Lane crossed")

	time.sleep(1)
	
