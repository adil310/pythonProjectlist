        #list and data types#
thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
  #print multiple list#
print(list1)
print(list2)
print(list3)
print(list2)
mylist = ["abc","def","ghi"]
print(type(mylist))
   #list excess from index
thislist = ["mango", "charry", "apple", "orange", "stobarry",]
print(thislist[2:])
print(thislist[3:])
    #uses of index
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["patatoz", "ginger"]
print(mylist)
    #list methods
mylist= ["apple", "ginger","blackpaper",]
tropical = ["flower", "rose", "gulab"]
mylist.append("orrange",)
print(mylist)
mylist.insert(1,"flower")
print(mylist)
mylist.extend(tropical)
print(mylist)
mylist.remove("flower")
print(mylist)
mylist.pop(1)
print(mylist)
         #loops in list
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  #sort of list
  thislist = ["apple","mango","orange","ginger","ananes"]
  thislist.sort()
  print(thislist)