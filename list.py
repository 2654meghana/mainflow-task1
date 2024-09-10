
#Create a list
my_list = [1,2,3,4,5]
#Adding an element to the list
my_list.append(6)
#Removing an element from the list 
my_list.remove(3)
#modifying an element in the list 
my_list[0] = 10
print("Update List:",my_list)
#Creating a dictionary
my_dict = {'name': 'Jhon','age':24,'city':'Delhi'}
#Adding
my_dict['gender'] = 'male'
#Removing
del my_dict['age']
#Modifying
my_dict['city'] = 'mumbai'
print("Update Dictionary:" , my_dict)
#Creating a set
my_set = {1,2,3,4,5}
#Adding
my_set.add(6)
#Removing
my_set.remove(3)
#Modifying
my_set.discard(1)
my_set.add(10)
print("updated set:",my_set)
