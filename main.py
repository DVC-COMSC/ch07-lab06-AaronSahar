
inputvalues = input('Enter all elements values: ')
numbers1 = inputvalues.split() 
for i in range(len(numbers1)):
	numbers1[i] = int(numbers1[i])
numbers2 = []
while numbers1:
	numbers2.insert(len(numbers2), numbers1.pop())
print ("The original list: ", numbers1)
print ("The new list:", numbers2)