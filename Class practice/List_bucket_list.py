bucket_list = ["Go to Asia", "get a full body tattoo", "Have a Dalmata", "jump from the sky"]
print(bucket_list) #full list

bucket_list.pop(0) #eliminates the first space
print(bucket_list)

print(bucket_list[1:2]) #returns the space 1 to the 2

a = [1,2,3]
b = [1,2,3]
print(a,b)

a[0] = 123
print(a,b)

c = a
c[0] = 999
print(a,b)