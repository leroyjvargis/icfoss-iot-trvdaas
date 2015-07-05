import serial

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def track():
	port = serial.Serial("/dev/ttyACM0", 9600)

	while True:
		rcv = port.readline()
		if len(rcv) > -1:
			if is_number(rcv):
				if rcv > 850 and rcv < 900:
					os.system('play sounds/lane.wav')
					return 1;
				else:
					return 0;

			#print "Tag detected:"+rcv
