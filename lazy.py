from collections.abc import Iterable
import itertools

################
# Built-in sets.
################

def empty():
	# Ø
	yield []

def integers():
	# Z
	n = 0
	while True:
		yield n
		yield ~n
		n += 1

def natural():
	# N
	n = 0
	while True:
		yield n
		n += 1

def positive():
	# ℕ
	n = 1
	while True:
		yield n
		n += 1

def rationals():
	# Q
	for i in lazyProd(integers(),positive()):
		yield i[0]/i[1]

#########################
# Vectorizing Arithmetic.
#########################

def addOne(a):
	# The À operation. 
	if isinstance(a,Iterable):
		for i in a:
			yield i + 1
	else:
		yield a + 1

def closedRange(a,b):
	if isinstance(a,Iterable):
		if isinstance(b,Iterable):
			for i in zip(a,b):
				x,y = i
				yield range(x,y+1)
		else:
			for i in a:
				yield range(i,b+1)
	else:
		if isinstance(b,Iterable):
			for i in b:
				yield range(a,i+1)
		else:
			yield range(a,b+1)

def oneRange(a):
	if isinstance(a,Iterable):
		for i in a:
			yield range(1,i+1)
	else:
		yield range(1,a+1)

def operAdd(a,b):
	if isinstance(a,Iterable):
		if isinstance(b,Iterable):
			for i in list(zip(a,b)):
				yield sum(i)
		else:
			for i in a:
				yield i+b
	else:
		if isinstance(b,Iterable):
			for i in b:
				yield a+i
		else:
			yield a + b

def operMul(a,b):
	if isinstance(a,Iterable):
		if isinstance(b,Iterable):
			for i in list(zip(a,b)):
				yield repmul(*i)
		else:
			yield mul(b,a)
	else:
		if isinstance(b,Iterable):
			yield mul(a,b)
		else:
			yield a*b

def operSub(a,b):
	if isinstance(a,Iterable):
		if isinstance(b,Iterable):
			for i in list(zip(a,b)):
				x,y=i
				yield x-y
		else:
			for i in a:
				yield i-b
	else:
		if isinstance(b,Iterable):
			for i in b:
				yield a-i
		else:
			yield a - b

def operMod(a, b):
	if isinstance(a,Iterable):
		if isinstance(b,Iterable):
			for i in list(zip(a,b)):
				x,y=i
				yield x % y
		else:
			for i in a:
				yield i % b
	else:
		if isinstance(b,Iterable):
			for i in b:
				yield a % i
		else:
			yield a % b

def mul(a, b):
	# It's *, if it isn't obvious enough.
	# a is a literal. b is an iterable.
	for i in b:
		x = list(repmul(a,i))
		if isinstance(x[0],str):
			yield ''.join(x)
		else:
			if len(x) == 1:
				yield x[0]
			else:
				yield x
def repmul(a,b):
	if isinstance(a,Iterable):
		for i in a:
			yield b*i
	else:
		yield b*a

##################
# Set comparisons.
##################

def cart(x,y):
	# Cartesian Power.
	out, a = itertools.tee(x)
	# a = int,
	# x = iterable.
	for i in itertools.tee(a, y-1):
		out = lazyProd(out,i)

	for i in out:
		yield i

def cartPow(x,y):
	if isinstance(x,int):
		return cart(y,x)
	else:
		return cart(x,y)

def cut(g, a):
	# Find the a-th item of the iterable.
	# I probably won't vectorize because
	# set theory doesn't require it.

	# The operand a has to be an iterable, too.

	t = g
	z = next(g)
	for i in range(next(a)):
		t = iter(t)
		z = next(t)
	return z

def lazyProd(a,b):
	# Cartesian product.
	a_status = True
	b_status = True
	aPairs = []
	bPairs = []
	while True:
		try:
			aPairs.append(next(a))
			for x,i in enumerate(bPairs):
				if isinstance(aPairs[-1],Iterable):
					yield aPairs[-1]+[i]
				else:
					yield [aPairs[-1]]+[i]
				
		except StopIteration:
			a_status = False
		try:
			bPairs.append(next(b))
			for i in aPairs:
				if isinstance(i,Iterable):
					yield i+[bPairs[-1]]
				else:
					yield [i]+[bPairs[-1]]
		except StopIteration:
			b_status = False
		if a_status == False and b_status == False:
			break

def member(a, g):
	# ∈ operator.

	# As usual g has to be an iterable.
	# a has to be one too.

	head = 0
	first = 0
	if not isinstance(a, Iterable):
		a = iter([a])

	head = g
	head = next(head)
	first = head

	# Next. Is the item an Iterable too?

	op1 = next(a)
	try:
		hd = len(head)
		op = len(op1)
	except:
		hd = head
		op = op1

	temp = g

	check = (op1 == first)

	for i in range(abs(op-hd)+1):
		z = a
		try:
			r = next(temp)
			check = check or op1 == r
			temp = iter(temp)
		except StopIteration:
			return iter([int(check)])

	return iter([int(check)]) # Make sure it's an iterator!

##################
# Set attributes.
##################

def cardin(a):
	# │, cardinality.
	itr = 0
	try:
		for i in a:
			itr += 1
		yield itr
	except StopIteration:
		yield itr

def equalQ(a,b):
	# Check if two finite data are equivalent
	temp = []
	if isinstance(a,Iterable):
		if isinstance(b,Iterable):
			for i in list(zip(a,b)):
				x,y = i
				temp.append(x == y)
		else:
			for i in a:
				temp.append(i == b)
	else:
		if isinstance(b,Iterable):
			for i in b:
				temp.append(a == i)
		else:
			temp.append(a == b)
	yield int(all(temp))

def head(X):
	# X is a constant or an iterator.
	if isinstance(X, Iterable):
		for i in X:
			break
		yield i
	else:
		yield X

def powerset(X):
	# ℙ, Powerset.
	temp = []
	i = 0
	curr = [next(X)]
	while True:
		try:
			for x,j in enumerate(bin(i)[2:][::-1]):
				if j == "1":
					temp += [curr[x]]
		except IndexError:
			try:
				iter(X)
				curr.append(next(X))
				continue
			except StopIteration:
				break
		yield temp
		temp = []
		i += 1

def plm(a):
	if isinstance(a,Iterable):
		out = []
		for i in a:
			yield i
			if i != 0:
				yield -i
	else:
		yield a
		if a != 0:
			yield -a

#####################
# Special utilities.
#####################

def roll(arr,fun):
	while True:
		yield arr[0]
		arr = fun(arr)

# for i in roll([1,2],lambda x:[x[1],x[0]+x[1]]):
# 	print(i)
# 	# The fibonacci sequence is printed.