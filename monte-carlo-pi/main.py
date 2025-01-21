import random

def iterate():
	x = random.uniform(0, 1)
	y = random.uniform(0, 1)
	return x**2 + y**2 < 1

inCircle = 0
total = 0
while True:
	inCircle += iterate()
	total += 1
	# area of unit circle = pi, area of this is pi/4
	pi = inCircle / total * 4
	if total % 100000 == 0:
		print("Pi Estimate:", pi)