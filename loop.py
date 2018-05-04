import time

def yes(no):
    while True:
        print "yes - %d" % no
        time.sleep(0.5)

def no(no):
    while True:
        print "no - %d" % no
        time.sleep(0.5)

yes(2)
no(3)
