def numbers():
    with open('numbers.txt', 'r') as file:
        content = file.read()
        print(content.replace(',', '\n'))


if __name__ == "__main__":
    numbers()
