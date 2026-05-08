def ft_count_harvest_recursive():
	a = int(input("Days until harvest: "))
	
	def count_days(i):
		if i > a:
			print("Harvest time!")
		else:
			print(f"Day {i}")
			count_days(i + 1)

	count_days(1)