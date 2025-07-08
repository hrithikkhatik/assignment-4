take_input=input("Enter text to write to the file: Hello,python! ")

with open("output.txt","w") as file:
    file.write(take_input)
print("Data successfully written to output.txt.")
print()



more_input=input("Enter additional next to append: Learning file handling in python.")
with open("output.txt","a") as file:
    file.write(more_input)
print("Data successfully appended")
print()


input=input("Final content of output.txt:")
with open("output.txt","a") as file:
    file.write(input)
print("Hello,python!")
print("learning file handling in python.")
with open("output.txt","r") as file:
    print(file.read())








