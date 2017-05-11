import math
import random

def NChooseK(n, k):
	if (k == 0) :
		return 1
	numerator = n
	for i in range(n - k + 1, n):
		numerator *= i
	denominator = k
	for i in range(2, k):
		denominator *= i
	return int(numerator/denominator)

def pascalsTriangle():
	for i in range (0, 21):
		print
		for j in range (0, i + 1):
			print NChooseK(i, j),

def biasedCoin(p, k, n):
	return NChooseK(n, k) * math.pow(p, k) * math.pow(1 - p, n - k)

def runExperiment(N, p, k, n):
	random.seed()
	successCount = 0
	probability = 1 - biasedCoin(p, k, n)
	for i in range (1, N):
		if random.random() > probability:
			successCount += 1
	return successCount

def experiment():
	for i in range(1, 4):
		print "N = {0}, Fraction of sucess = {1}".format(math.pow(10, i), runExperiment(int(math.pow(10, i)), 0.250, 0, 4) / math.pow(10, i))
	
