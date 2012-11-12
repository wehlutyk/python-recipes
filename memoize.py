# A function to cache the result of another function

def memoize(func):
	cache = {}
	def inner(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return inner

