#=== Booleans ====== => True or False

isNumber = True
isNumber2 =  False
# print(isNumber == isNumber2)
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

a = 200
b = 33

# if b > a: # True or False
#     print(' b is greater than b')
# elif(a == b):# True or False
#     print(' b == a')
# elif (a < b):# True or False
#     print('a < b')
# else:
#     print(' do some thing!')

helloStr = "hello" #==> ""(Empty) => False , is not empty => True
newNumber = 15      #==> 0 == False ,is not 0 => True
zeroNumber = 0
isNone  = None #= False
# if(zeroNumber == 0 ): # => True
#     print('number is zero')

def myFunction(): # => Create Function
    return True

def checkMyName(name):
    result = False
    if(name == 'john'):
        result = True

    return result

# if myFunction():
#     print("this is myFunction")

if checkMyName('john'):
    print('Yes , Hello john')
else:
    print('No , Is not john')




print(bool(None))
print(bool('')) #String
print(bool(0))  #Number
print(bool(())) #Tuple
print(bool([])) #List
print(bool({})) #Dictionary 
numberDic = {
    'one':['หนึ่ง',1,'one','๑']
    #Key : Value
} #=> Dictionary
# print(bool(numberDic))