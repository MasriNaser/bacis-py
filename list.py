# A list

numbers = [1,2,3,4,5,6,7,8,99]
fruits= ['apples', 'kiwi', "oranges",'pears','grappes']
#use a constractor

numbers2 = list((1,2,3,4,5,6,7,8,99))

print(numbers,numbers2)

#get value from a list
x = fruits[1]
print(x)

#get lenth
print(len(fruits))

#append to list
fruits.append('Mango')
print(fruits)

#remove
y = fruits.remove('kiwi')
print(y)

#insert into pos
fruits.insert(0, "any")
print(fruits)

#remove with pop
fruits.pop(2)

#reverse list
fruits.reverse()

# change value
fruits[0] = 'kaka'
print(fruits)