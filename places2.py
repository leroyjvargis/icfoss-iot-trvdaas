import places
import store_db

la = '8.5585854'
lo = '76.8821835'
sp = '35'

loc = la + ', '+ lo
#print loc
loc_name = "Kottayam"
off = "horn adichu"

#places.init(la, lo, sp)

store_db.init(loc, loc_name, off)
