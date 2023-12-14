with open("./german.txt", "r") as my_file:
    data = my_file.readlines()
    

words = [line.split()[0] for line in data]

with open("./output.txt", "w") as output_file:
    for word in words:
        output_file.write(f"{word}\n")
    