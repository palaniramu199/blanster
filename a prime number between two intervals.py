for num in range(1,10):
	for dist in range(2,50):
		if num%dist==0:
			break
		else:
			print(num,end='\t')
			break
		
