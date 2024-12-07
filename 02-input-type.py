#input
#type

a = 1
b = 2
print('Total numbers is {}:'.format(a+b))

#print - standart output
data = input('Please enter somethings : ')
print('Your input is : ',data)
print(type(data)) #Output: <class 'str'>

#str + str = string concatenation (joining)
data = input('Enter a number : ') #input() always returns string
print(data + data)
print(type(data))

#string to other type, type conversion (casting)
data = input('Please enter somthing : ')
data = int(data) #String ကို integer or number type အဖြစ်ပြောင်း
print('Your input is : ', data)
print(type(data)) #Output: <class'int'>