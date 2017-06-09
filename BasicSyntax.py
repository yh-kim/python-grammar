# Created by yonghoon on 2017-06-09
# Blog   : http://blog.pickth.com
# Github : https://github.com/yh-kim
# Mail   : yonghoon.kim@pickth.com

# variable
def variableTest():
	print("----variable test----")
	x = 3
	print("variable x = %d" % x)

def operationTest():
	print("----operation test----")
	print("1 - 2 = %d" % (1 - 2))	# -1
	print("4 * 5 = %d" % (4 * 5))	# 20
	print("7 / 5 = %d" % (7 / 5))	# 1
	print("7 / 5 = %f" % (7 / 5))	# 1.400000
	print("3 ** 2 = %d" % (3 ** 2))	# 9

def listTest():
	print("----list test----")
	a = [1, 2, 3, 4, 5]
	print(a)		# [1, 2, 3, 4, 5]
	print("length = %d" % len(a))	# length = 5
	a[4] = 99
	print(a)		# [1, 2, 3, 4, 99]
	print(a[0:2])	# [1, 2]
	print(a[1:])	# [2, 3, 4, 99]
	print(a[:3])	# [1, 2, 3]
	print(a[:-1])	# [1, 2, 3, 4]
	print(a[:-2])	# [1, 2, 3]
	print(a[::-1])	# [99, 4, 3, 2, 1]

def dictionaryTest():
	print("----dictionary test----")
	me = {'height' : 180}
	print(me['height'])		# 180
	me['weight'] = 70
	print(me)				# {'height': 180, 'weight': 70}

# and or not in
def booleanTest():
	print("----boolean test----")
	hungry = True
	sleepy = False

	if hungry:
		print("I'm hungry")						# o

	if not hungry:
		print("I'm not hungry")					# x
	elif hungry and sleepy:
		print("I'm hungry and sleepy")			# x
	else:
		print("I'm not hugry and not sleepy")	# o


def test():
	variableTest()
	print()
	operationTest()
	print()
	listTest()
	print()
	dictionaryTest()
	print()
	booleanTest()

test()