file_name = 'data/inputData.txt'

with open('data/inputData.txt') as input_data:
    contents = input_data.read()
    print(contents)

print(contents)
print("Reading a inputData.txt file completed")

# writing to the file
with open(file_name, 'a') as file_object:
    file_object.write("I love programing.\n")
