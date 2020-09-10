#functions
def print_separator():
    print('----------')

#instructions
print ('Hello World!')

# variables
name = 'Kenny'
age = 33
total = 99.87
found = False

print(name)
print(age)
print(total)

print_separator()

# math operations
print(age - 10)
print(age + 10)
print(2*3)
print(10/5)
print(33%2)

print_separator()


#if statements
user_age = 79
if(user_age < 80):
    print('You are still young')
    print("Don't worry too much!")
elif(user_age == 80):
    print("You are on the borderline")
else:
    print("Sorry, you are getting old!")