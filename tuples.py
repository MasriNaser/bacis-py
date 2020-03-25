# A tuple is a collection which is ordered and unchangeable. Allows duplicate numbers.

fruits = ('Apples', 'Oranges','Grapes')

#use constractor
fruits2 = tuple=(('Apples', 'Oranges','Grapes'))

 #single value needs trailing comma
fruits3 = ('kiwi')
print(fruits3)

# cant change value
# fruits2[0]= 'pears'

# A Set is a coll which unordered and unindexed. No duplicate number

#create set
fruits_set = {'App','Orange','Mango'}
print('App' in fruits_set)

#Add to set
fruits_set.add('test')
print(fruits_set)

#remove from set

fruits_set.remove('test')
print(fruits_set)

#clear set
fruits_set.clear()
print(fruits_set)

#delete
del fruits
print(fruits2)