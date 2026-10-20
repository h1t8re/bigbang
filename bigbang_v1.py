import math as math

def infinity_space_generator(r):
	for phi in range(0, 360):
		for teta in range(0, 360):
			x = r*math.cos(math.radians(phi))*math.sin(math.radians(teta))
			y = r*math.sin(math.radians(phi))*math.sin(math.radians(teta))
			z = r*math.cos(math.radians(teta))
			yield (x, y, z)
			
def infinity_space_and_time_generator():
	t = 0
	while True:
		t = t +1
		for (x, y ,z) in infinity_space_generator(t):
			yield (x, y, z)

def main():
	for (x, y ,z) in infinity_space_and_time_generator():
		yield (x, y, z)

if __name__ == "__main__":
	main()
