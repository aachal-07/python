print("hello world")
name = "ritik"
print(name)
Name  = "jai"
print(Name)
number  = 1000000
print(number)
num = 10.25852585
print(num)
# name = "aachal"  # 01234
# print(name[0:2])
# print(name[4])
# print(type(name))
# num = 100.2
# print(type(num))
# var = True
# print(type(var))

# print(len(name))
# name = "aachal"  # as a string
# name_upper = "AACHAL" # as a string
# print(name.upper()) # upper case
# print(name_upper.lower()) # lower case
# print(name.swapcase())
# print(name.title())

# print(name.replace("aachal", "jai"))

# name = "aachal"
# last_name = "kmt"

# print(name + " " +  last_name)
# output = aachal kmt    ,aachalkmt
# print(name.find("k"))
# print(name.capitalize())


# my name is aachal
# print("My name is ", name, "and my last name is ", last_name) 


# print(3 * name)

# print(f"my name is  {name}  and my last name is  {last_name}")



# print(name.replace("i", "j"))
# print(name.replace("i", "j", 1))



# text =  " hello world "

# # print(text.replace("world", "python"))
# print(text.index("world"))
#### list 


# my_list = [1,2,3,4,5,5,5,5,54,5,5,5,55]
# print(type(my_list))


# my_list1 = [1,"ritik",3,4.2,True,5,5,5,54,5,5,5,55]
# print(type(my_list1))
# print(my_list1)

# print(my_list)
# print(my_list[2])


# my_list = [1,2,3,4,5,5,5,5,54,5,5,5,55]
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
# print(my_list[-4])
# print(my_list[-5])

# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])


# my_list = [1,2,3,4,5,5,5,5,54,5,5,5,55]


# print(my_list[1:5])
# print(my_list[:5])
# print(my_list[1:])
# print(my_list[:])


# print(len(my_list))


# my_list.append(100)
# print(my_list)

# my_list.insert(1,100)
# print(my_list)
# my_list.remove(5)
# print(my_list)
# my_list.pop()
# print(my_list)
# my_list.index(5)
# print(my_list)

# my_num = [5,4,3,2,1]
# my_num.sort()
# my_num.clear()
# print(my_num)




# >>>tuple  and dict , set






# operations on tuple 

# tpl = (1,2,3,4,5)
# print("tpl:-",tpl)

# print("type of tpl:-",type(tpl))
# print("len  of tpl:-",len(tpl))

# print("0 position ka element :-",tpl[0])
# print("1 position ka element :-",tpl[1])
# print("2 position ka element :-",tpl[2])
# print("3 position ka element :-",tpl[3])
# print("4 position ka element :-",tpl[4])
# print("0 position ka element :-",tpl[5])
# print("0 position ka element :-",tpl[6])



# tpl = (1,2,3,4,5)

# 
# print("0 to 2  position ka element :-",tpl[0:2])
# print("1 position ka element :-",tpl[::-1])  



# print("1 position ka element :-",tpl[1:-1])  # anshul   2 , 3 , 4   

# tpl = (1,2,3,4,5)

# print(2 in tpl)
# print(10  in tpl)

# min 
# max
# sum


# print("max of tpl:-",max(tpl))
# print("min of tpl:-",min(tpl))
# print("sum of tpl:-",sum(tpl))



# tpl1 = 1,2,3,54,5,4,4
# print(type(tpl1))
# print(tpl1)



# tuple unpaking
# kapil = 1,2,3 

# a,b,c = kapil
# print("a:-",a)
# print("b:-",b)
# print("c:-",c)

# data list dict tuple





# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..dict 

dct = {
    "name" : "ritik",
    "last_name" : "kmt",
    "age" : 21
}
# print("dict type:-",type(dct))
# print("dct :-",dct)

# print(dct["name"])

# print("name :-",dct["name"])#  >>>>> ritik 
# print("last_name :-",dct["last_name"])# >>>> kmt 
# print("age :-",dct["age"]) #>>>>> 21 



# print("dct keys:-",dct.keys())
# print("dct values:-",dct.values())
# print("dct items:-",dct.items())




dct = {
    "name" : "ritik",
    "last_name" : "kmt",
    "age" : 21
} 

# item adding in dct 

# dct['Gender'] = "Male"   #  # Add new key-value pair
# print(dct)

# updating dct 

# dct['age'] = 22
# print(dct)


# Deleting items 
# del dct['last_name']
# print(dct) 
# dct.pop("last_name")
# print(dct)

# dct.clear()
# print(dct)
# print('name' in dct)
# print('ritik' in dct)


# dct = {
#     "name" : "ritik",
#     "last_name" : "kmt",
#     "age" : 21
# } 

# copy 

# dct1 = dct.copy()
# print(dct1)

# copy_dct=dct.copy()
# print("copy dict ",copy_dct)
# print("original dict ",dct)



#  Merging Dictionaries


# dct1 = {
#     "vikram_name" : "vikram",
  
#     "vikram_age" : 21
# } 

# dct2 = {
#     "kapil_name" : "kapil",
#     "last_name" : "kumar",
#     "kapil_age" : 21
# } 

# dct1.update(dct2)
# print(dct1)


# key = ["a","b","c"]
# default_dict=dict.fromkeys(key, 0)

# print(default_dict) ### >>>>>>>>>>>>>.{'a': 0, 'b': 0, 'c': 0}



# >>>>>>>>>>>>>>>>>>>Set 

# my_set = {1,2,3,4,5,"ritik"}
# print(type(my_set))
# # print(my_set)

# my_set.add(100)
# my_set.add("kapil")
# my_set.add("vijay")

# print(my_set)

# my_set.remove("ritik")
# print("remove element:-",my_set)
# my_set.discard(5)
# print("discard element:-",my_set)

# my_set.pop()
# print("pop element:-",my_set)
# my_set.clear()
# print("clear element:-",my_set)


