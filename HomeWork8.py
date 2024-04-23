file_name = "SomeText.txt"
with open(file_name, mode='r', encoding='utf8') as file_content:
    for line in file_content:
        print(line)
print(file_content.closed)
