from __future__ import division
import math
import cmath
import matplotlib.pyplot as plt

# Define recurrence relation
def z(i, x, y):
	if i == 0:
		return complex(x, y)
	else:
		x = z(i - 1, x, y)
		return x * x + complex(x, y)

# Loop and plot all, blue dot if it diverges, red if it does not.
for x in range(-20, 21):
	for y in range(-20, 21):
		ans = 0
		for i in range (0, 15):
			ans = z(i, x/10, y/10)
			if cmath.isinf(ans):
				plt.plot(x / 10, y / 10, 'bo')
				break
		if not cmath.isinf(ans):
			plt.plot(x / 10, y / 10, 'ro')

plt.suptitle('Blue = Diverts, Red = Does not divert', fontsize=14)
plt.show()
