# Postfix evaluator.

from nst import code, oprnd
from lazy import *

# Pasted all special chars here just in case.
# ℂℍℕℙℚℝℤ

nilads = "αNṄØZQÏ"
dyads = "+-*%¢€§×¨^="
monads = "Ȧ¦Ṗ±|,ıḣL"

numbers = "0123456789"

fwnums = "°¹²³⁴⁵⁶⁷⁸⁹"
# Superscript, just push these digits by themselves.

stack = []

def parse(idx,code):
	if "Ṫ" in code:
		return code.index("Ṫ")
	else:
		op = 0
		count = 0
		for x,i in enumerate(code):
			if count < 0:
				break
			if i in nilads:
				if code[x] in numbers:
					if code[x-1] not in numbers:
						count += 1
				else:
					count += 1
			if i in dyads:
				count -= 1
			op += 1
		return op

def num_iter(i):
	# Create different types of iterables.
	yield i

def str_iter(i):
	# Same as this.
	yield i

def apply(source,code):
	for i in source:
		yield codeRun(code,[i],True)

def filtr(source,code):
	for i in source:
		condition = codeRun(code,[i],True)[-1]
		if isinstance(condition,Iterable):
			if sum(condition)!=0:
				yield i
		else:
			if int(condition)!=0:
				yield i

def nfiltr(source,code):
	for i in source:
		condition = codeRun(code,[i],True)[-1]
		if isinstance(condition,Iterable):
			if sum(condition)==0:
				yield i
		else:
			if int(condition)==0:
				yield i

def codeRun(code,stack,inblock = False):
	def takeInput(idx):
		temp = oprnd[idx]
		# If that's an iterable:
		if isinstance(temp, Iterable):
			stack.append(iter(temp))
		else:
			stack.append(temp)
		return (idx + 1) % len(oprnd)

	idx = 0
	skip = 0
	curr = 0
	# Let's do a preprocessor for code here.
	if code.count('"') % 2 == 1:
		code = '"' + code

	code += " "

	for x, i in enumerate(code): # Implicitly appended space...
		is_end = 0
		try:
			if is_end==1 and inblock:
				return stack
		except:
			pass

		if skip > 0:
			skip -= 1
			continue

		if i == '"':
			if curr == 0:
				stack.append("")
				curr = 1
			else:
				curr = 0
			continue

		if curr == 1:
			stack.append(stack.pop() + i)
			continue

		if i in numbers:
			if code[x - 1] in numbers:
				stack.append(stack.pop() * 10 + int(i))
			else:
				stack.append(int(i))

		try:
			if code[x + 1] in numbers and code[x] in numbers:
				continue
		except:
			pass

		if i in fwnums:
			stack.append(fwnums.index(i))

		if i in dyads:
			if len(stack) == 0:
				idx = takeInput(idx)
			if len(stack) == 1:
				idx = takeInput(idx)
				if "Ṫ" not in code[x:]:
					is_end = 1

		elif i in monads:
			if len(stack)==0:
				idx = takeInput(idx)
				if "Ṫ" not in code[x:]:
					is_end = 1

		if i == "Ṫ":
			is_end = 1

		if i == "α":
			temp = oprnd[idx]
			# If that's an iterable:
			if isinstance(temp, Iterable):
				stack.append(iter(temp))
			else:
				stack.append(iter([temp]))
			idx += 1

		if i == "N":
			stack.append(natural())
		if i == "Ṅ":
			stack.append(positive())

		if i == "Ø":
			stack.append(empty())
		if i == "Z":
			stack.append(integers())

		if i == "Q":
			stack.append(rationals())

		# Set related ops.

		if i == "¦": # Cardinality
			a = stack.pop()
			stack.append(cardin(a))

		if i == "Ṗ": # Powerset
			a = stack.pop()
			stack.append(powerset(a))

		if i == "Ȧ": # Add One.
			a = stack.pop()
			stack.append(addOne(a))

		if i == "ḣ": # Take the first item.
			a = stack.pop()
			stack.append(head(a))

		## Arithmetic Dyads

		if i == "*":
			a,b = stack.pop(), stack.pop()
			stack.append(operMul(b,a))

		if i == "%":
			a,b = stack.pop(), stack.pop()
			stack.append(operMod(b,a))

		if i == "+":
			a,b = stack.pop(),stack.pop()
			stack.append(operAdd(b,a))

		if i == "-":
			a,b = stack.pop(),stack.pop()
			stack.append(operSub(b,a))

		if i == "¨": # Inclusive range
			a,b = stack.pop(),stack.pop()
			stack.append(closedRange(b,a))

		if i == "±": # Plus/Minus
			a = stack.pop()
			stack.append(plm(a))

		if i == "L": # One range
			a = stack.pop()
			stack.append(oneRange(a))

		# Set dyads

		if i == "€":
			a,b = stack.pop(), stack.pop()
			stack.append(member(b, a))

		if i == "¢":
			a,b = stack.pop(), stack.pop()
			stack.append(1-member(b, a))

		if i == "§":
			a,b = stack.pop(), stack.pop()
			stack.append(member(a, b))

		if i == "×": # Cartesian product
			a,b = stack.pop(),stack.pop()
			stack.append(lazyProd(a, b))

		if i == "^": # Cartesian power
			# ^ is a generalization of ×.
			a,b = stack.pop(),stack.pop()
			stack.append(cartPow(b,a))

		# Comparison operators
		if i == "=": # Equality between two stuff
			a,b = stack.pop(),stack.pop()
			stack.append(equalQ(b,a))

		# Stack manipulation
		if i == "}": # Roll whole stack into a list.
			stack = [iter(stack)]

		if i == "Ï": # Duplicate the stack
			stack.append(stack[-1])

		# From ZF expressions

		if i == "|": # Map with the, uh, rest of the program?
			source = stack.pop()
			stack.append(apply(source,code[x+1:]))
			skip = parse(x,code[x+1:])
			continue

		if i == ",": # Filter by a condition.
			source = stack.pop()
			stack.append(filtr(source,code[x+1:]))
			skip = parse(x,code[x+1:])
			continue

		if i == "ı": # The opposite of Filter.
			source = stack.pop()
			stack.append(nfiltr(source,code[x+1:]))
			skip = parse(x,code[x+1:])
			continue

	return stack

last_output = codeRun(code,[])[-1]

if isinstance(last_output,Iterable):
	for i in last_output: # Care only for the last item :)
		temp = i
		try:
			for i in temp:
				if isinstance(i, Iterable):
					for j in i:
						print(j,end=" ")
				else:
					print(i,end=" ")
			print()
		except TypeError:
			print(i)
else:
	print(last_output)