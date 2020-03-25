# A dic is a coll whiwh is unordered, changable and indexed. NO dup num

#create dict
person={
  'first_name': 'Tony',
  'last_name': 'Doe',
  'age': 33
}
#use constructor
person2 = dict(first_name='sara',last_name='willy')
print(person, type(person))
print(person2)

#get val
print(person2['first_name'])
print(person2.get('last_name'))

#add key val
person2['phone'] = '55579797987'
print(person2)
#get keys
print(person2.keys())
print(person2.items())

#copy dict
person2 = person.copy()
person2['city'] = 'Aleppo'
print(person2)

#delete item
del(person['age'])
person.pop('phone')

print(person)

#length
print(len(person))
#List of dicrt

people = [
  {
    'name': 'Matha', 'age':444444
  },
  {'name': 'Kevin', 'age': 45}
]
print(people,"its herererere")