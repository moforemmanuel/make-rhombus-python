while True:
	n=int(input("Enter odd number greater than 3 : "))
	if n<=3 or n%2==0:
		print("Invalid input...")
	else:
		break

for i in range(1,n-1,2):
	star="*"*i
	drawing=star.center(n)
	print(drawing)

for i in range(n,0,-2):
	star="*"*i
	drawing=star.center(n)
	print(drawing)
	
	
	
