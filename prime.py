a=int(input(""))
for i in range(2, int(a/2)):
	if a % i  == 0:
		print("yes")
		break
else:
	print("no")
