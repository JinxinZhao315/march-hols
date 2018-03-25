name = input("What is your name? ")

# If length of name is greater than 20,
# print something
if len(name)>20:
    print('Wow aristocracy')


age = input("What is your age? ")

if int(age)<10:
    print('Smol')
elif 10<int(age)<20:
    print('Big boi')
else:
    print('Big big boi')
# If age is less than 10, print "Smol"
# ELse if age is between 10 and 20, print "Big boi"
# Else, print "Big big boi"



coolness = input("Rate your coolness out of 100.0")

# If coolness is more than 100.0, just print some error

if float(coolness)>100.0:
    coolness_str = 'Cool Beyond Assessment'
    print(coolness_str)
elif float(coolness)>75.0:
    coolness_str = 'Admiringly Cool'
    print(coolness_str)
elif float(coolness)>50.0:
    coolness_str = 'Moderately Cool'
    print(coolness_str)
elif float(coolness)>25.0:
    coolness_str = 'Lame'
    print(coolness_str)
else:
    coolness_str = 'Lacking Confidence'
    print(coolness_str)

# Now print a string like
# My name is Arnold Tan, I am 69 and I'm Really Cool

print("My name is {}, I am {} and I am {}".format(name,age,coolness_str))


