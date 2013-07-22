###Reference###
1. http://www.slideshare.net/r1chardj0n3s/dont-do-this-24000445#btnNext


1. generator
	* 'generator' object has no attribute '__next__'
	
	```python
	def generate_stuff():
    for _i in range(3):
        yield "spam"

    while True:
        yield "ham"
	generation = generate_stuff().next()
	
	print generation
	print generation
	print generation
	```