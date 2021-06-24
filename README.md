# Variable Length Argument Lists
#### Using '*' & '**' when defining & calling functions

https://programmersought.com/article/28282498587/

**Note:** Using *args/**kwargs in both the definition of a function and also when calling that function is confusing AF

#### tl;dr

| Function Def      | Function Call  | How args are handled in the function
|-------------------|----------------|------------------------------
| def f(*tuple):    | f(a1,a2,...)   | for i in tuple
| def f(**dict):    | f(k1='v2',...) | for k,v in dict.items()
| def f(a1,...,aN): | f(*list)       | same as formal positional args
| def f(a1,...,aN): | f(**dict)      | same as formal keyword args

-----
### Used in Function Definition

#### * - postional args in call -> tuple in func

Converts any positional arguments in the function call into items of a tuple in the function

	def funct(*name_tuple):
		for i in name_tuple:
			do something
	
	func(item1, item2, ...)

#### ** - kwargs in call -> dict in func

Converts any kwargs in the function call into key-value pairs of a dictionary in the function

	def funct(**name_dict):
		for k, v in name_dict.items():
			do something
	
	func(kwarg1='v1', kwarg2='v2', ...)

-----
### Used in Function Calls

#### * - list/tuple name in call -> positional args in func

Converts the items in a list or tuple in the function call into positional arguments in the function

	def f1(a,b,c):
		print(a)

	my_list = [1,2,3]

	f1(*my_list)

#### ** - dict name in call -> kwargs in func

Converts the key-value pairs of a dictionary in a function call into kwargs in the function
	
	def f2(name,age,sex):
		print(name)

	d = {"name":'mr',"age":22,"sex":'boy'}

	f2(**d)

-----
### Used in both Function Definition & Function Calls
#### Here be dragons ...

First parameter into a plurality of transfer parameters, function parameters and turn into a tuple

	def func1(*a):
		print(a)
	
	func1(*list)							

First parameter into a plurality of key-value pairs turn in the function parameters and turn into a dictionary

	def func2(**b):
		print(b)
		
	func2(**dict)					# 

-----
### syntactical differences between function parameters and lists/tuples/dictionaries

#### kwarg vs K/V pair

| Kwarg         | K/V pair
|---------------|--------------
| `year="2020"` | `'year': "2020"`

#### positional args vs list

| positional args | list
|-----------------|--------------
| `func(1, b, 3)` | `[1, b, 3]`

-----
### Order of using formal args, *args & **kwargs

For example, use all three of these in a function definition

	func(fargs, *args, **kwargs)

-----
### monkey patching

modifying some code at runtime. Consider that you have a class with a function called `get_info` which calls an API and returns the response data. If we want to test it we can replace the API call with some test data. For instance:

	import someclass

	def get_info(self, *args):
		return "Test data"

	someclass.get_info = get_info
