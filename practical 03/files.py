NAMES = "names.txt"
#1
file_object = open("names.txt ", "w")
get_name = input("Enter your name: ")
print(get_name,file=file_object)
file_object.close()


#2
in_file = open("names.txt ")
text = in_file.read()
in_file.close()
print(text)

#3
with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
result = num1 + num2
print(result)


#4
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        num = int(line.strip())
        total += num
print(total)
