# importing secrets for extra security
import secrets

sg = secrets.SystemRandom()

# 3 digit code 0-9
three = str(sg.randint(0,9)) + str(sg.randint(0,9)) + str(sg.randint(0,9))

# 4 digit code 1-6
four = str(sg.randint(1,6)) + str(sg.randint(1,6)) + str(sg.randint(1,6)) + str(sg.randint(1,6))

print("Super secret 3 digit code is: ")
print(three)
print("Mega ultra secret code with 4 digits is: ")
print(four)
