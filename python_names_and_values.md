###Reference###
1. http://nedbatchelder.com/text/names.html
2. http://python.net/~mwh/hacks/objectthink.html

###Facts###
1. Names refer to values.
2. Many names can refer to one value.

	```python
	# Now x and y both refer to the same value.
	# We have only one 23, and x and y both refer to it.
	x = 23
	y = x
	```
3. Values live until nothing references them.
4. Assignment never copies data.
5. Changes in a value are visible through all of its names.
6. 2 types of values:
	* immutable 
		* Immutable values include numbers, strings, frozensets, and tuples.
		* Immutable means that the value can never change, instead when you think you are changing the value, you are really making new values from old ones.
	* mutable 
		* Almost everything else is mutable, including lists, dicts, and user-defined objects. 
		* Mutable means that the value has methods that can change the value in-place.
	
	```python
	def foo(v, testList=[]):
		testL.append(v)
		return testL
	
	def foo1(k, v, testDict={}):
		testD[k] = v
		return testD
	
	def foo3(v, testSet=set()):
		testSet.add(v)
		return testSet
		
	print foo(4)
	print foo(5)	
	print foo1('a', 1)
	print foo1('b', 2)
	print foo3(2)
	print foo3(4)
	```
	Output
	```python
	[4]
	[4, 5]
	{'a': 1}
	{'a': 1, 'b': 2}
	set([2])
	set([2, 4])
	```

7. 	References can be more than just names.
	* names look like this:
	![](/images/names.png)
	* bindings look like this:
	![](/images/bindings.png)
	* objects look like this:
	![](/images/objects.png)
	
	```python
	d = {'a': 1, 'b':2}
	testL = d.values()
	```
	![](/images/dict.png)
	
	```python
	L = range(2)
	copiedL = L[:]
	L[0] = 1
	s = 1
	print L[0] is s is L[1]
	```
	Output
	```python
	True
	```
	![](/images/dict2.png)
	
	```python
	# Each of these left-hand sides is a reference
	# attributes of objects and entries in lists or dictionaries are also references
	my_obj.attr = 23
	my_dict[key] = 24
	my_list[index] = 25
	my_obj.attr[key][index].attr = "etc, etc"
		
	# d['a'], d.values()[0], v1, and v2 are just different references (names) 
	# for the same value 1.
	d = {'a': 1}
	v1 = d['a']
	v2 = d.values()[0]
	print v1 is v2
	
	# list is mutable, used as value of dict
	d = {'a': [1, 2]}
	v1 = d['a']
	v2 = d.values()[0]
	
	from copy import copy
	v3 = copy(d).values()[0]
	
	from copy import deepcopy
	v4 = deepcopy(d).values()[0]
	
	print v1 is v2
	print v1 is v3
	print v1 is v4
	```
	Output
	```python
	True
	True
	True
	False
	```
8. Lots of things are assignment
	```python
	# Each of these lines is an assignment to the name X, and makes 
	# the name X refer to a value.
	X = ...
	for X in ...
	[... for X in ...]
	(... for X in ...)
	{... for X in ...}
	class X(...):
	def X(...):
	def fn(X): ... ; fn(12)
	with ... as X:
	except ... as X:
	import X
	from ... import X
	import ... as X
	from ... import ... as X
	```
9. Any name can refer to any value at any time.
	* A name can refer to an integer, and then to a string, and then to a function, and then to a module.
10. Names have no type, values have no scope.
	* When we say that a function has a local variable, we mean that the name is scoped to the function: you can't use the name outside the function, and when the function returns, the name is destroyed. But as we've seen, if the name's value has other references, it will live on beyond the function call. It is a local name, not a local value.
11. Values can't be deleted, only names can.
12. Advice by a Pythonista:
	* prefer "names", "bindings" and "objects" to "variable" in a python context
	* __In general, whenever possible, python returns references to the same objects it already had around, rather than copying__
	```python
	testL = range(10)
	testL2 = copy.deepcopy(testL)
	
	print testL[0] is testL2[0]
	```
	Output
	```python
	True
	```
	

###Roundup###
1. __names__ refer to __values__.
2. One value could have mutiple references.
3. References are not just __names__.
4. __values__ can't be deleted, only __names__ can.
5. __names__ have no type, __values__ have no scope.
6. Any name can refer to any value at any time.
7. Assignment never copies data.
8. Changes in a __value__ are visible through all of its __names__.
		
