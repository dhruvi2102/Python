food_list=["Noodles","Bhaji Pav","Panipuri","Manchurian","Puff","Pizza","Dabeli","Vadapav"]

print(food_list)

'''print(food_list[0])
print(food_list[7])
print(food_list[0:4]) #print from 0 to 3
print(food_list[4:8])  
print(food_list[-1])   #print from back 
print(food_list[3:])   #print all after 3
print(food_list[:5])   #print all before 5
print(food_list[0::2])'''   #print skipping 1

'''print(len(food_list))

for items in food_list:
    print(items)

if "Pizza" in food_list:
    print("Yes")
else :
    print("Sorry..Please try something else")'''  

#-----------------Inbuilt Methods of List--------------  

'''print(food_list.index("Pizza"))
food_list.append("Hotdog")
food_list.insert(4,"Sabzi")
food_list.remove("Pizza")
food_list.pop()
food_list.pop(5)
food_list.sort()
food_list.reverse()
food_list.clear()
del food_list
print(food_list)'''

restaurant_list=["Honest","Pizza Hut","Tea Post","Octant Pizza","Mc Donald's","Starbucks","Domino's"]

print(restaurant_list)

#print(food_list+restaurant_list)

food_list.extend(restaurant_list)
print(food_list)


