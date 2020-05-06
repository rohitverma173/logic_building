
# access user input and print type of input


''''
#Test-1: raw input
# this acccept input only in one line. what if user input is in multiline ??

user_input = input("Enter any input, will print welcome message: ")
print("Welcome message\n" + user_input)
'''

'''
#Test-2: raw input with multiple line. we have to write logic because there is no in-builit method available

lines = []
while True:
    line = input()
    print(len(line))
    if line:
        lines.append(line)
    else:
        break
text = "\n".join(lines)
print(text)
'''


