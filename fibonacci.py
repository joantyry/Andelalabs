def fibonacci(n):
	if n==0 or n==1:
		return n
	elif n > 1:
		return (fibonacci(n-1)+ fibonacci(n-2)) 
	else:
	 return "enter a valid number"	
 	