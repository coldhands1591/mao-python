a = 'Hello'
strMultiLine = """
oldhands@Suphats-MacBook-Air data_type
oldhands@Suphats-MacBook-Air data_type
oldhands@Suphats-MacBook-Air data_type
"""
strArray = "Hello" #[H e l l o] array
                    #0 1 2 3 4 => index array
# if "c" not in strArray:
#     print("No 'c' is not present" )
# if "e" in strArray:
#     print("Yes, 'e' is present.")

#print('get length: ' + str(len(strArray)))
# print(strArray[1])
# print(strArray[0]) #=> get data by index
# for item in strArray: #=> get data by for loop
#     if item == 'o':# true or false
#         getO = item
#         print(getO)
    # print(item)

# fluits  = ['Orange','Banana','Cherry'] #=> data list
# for item in fluits:
#     for item2 in item:
#         print(item2)
#     print(item)


#=== Slice String ===
# b = "Hello,World!"
#     #01234567891011 =>index string
# print(b[2:5])#=> b[start index:end index]
# print(b[:5])
# print(b[7:])

#=== Modify String ====
firstName = ' SupHat'
lastName  = 'PHLaengliT '
fullName = firstName+'_'+lastName
# print(firstName.upper())
# print(lastName.lower())
# print(fullName.strip())
newFullName = fullName.strip() #SupHit_PHLiengliT
# print(newFullName.replace('a','i'))
# print(newFullName.split('_')) #=> ['SupHat', 'PHLaengliT']
arrFullName = newFullName.split('_') #=> ['SupHat', 'PHLaengliT']
newFirstName = arrFullName[0]
newLastName = arrFullName[1]

countEFirstName = 0
for item in newFirstName:
    if item == 'e':
        countEFirstName = countEFirstName+1

countELastName = 0
for item in newLastName:
    if item == 'e':
        countELastName = countELastName+1

if countEFirstName > countELastName:
    countResult = countEFirstName - countELastName
    print('FistName more than LastName: '+str(countResult))
elif countEFirstName == countELastName:
    print('FistName equa to LastName: '+str(countELastName))
elif countEFirstName < countELastName:
    countResult  = countELastName - countEFirstName
    print('FistName less than LastName: '+str(countResult))

# print(newLastName)



