import time

def test_run():
	t1 = time.time()
	print "Hello World"
	t2 = time.time()
	print "Time taken is",t2-t1,"seconds"

test_run()