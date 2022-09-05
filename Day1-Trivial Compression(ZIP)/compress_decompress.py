def compress(text):
    dic = {}
    compressed = ""
    for letter in text:
        if letter in dic:
            dic[letter] += 1
        else:
            dic[letter] = 1
    for letter in text:
        if dic[letter]:
            compressed += letter
            compressed += str(dic[letter])
            dic[letter] = 0
    return compressed


def decompress(text):
    decompressed = ""
    for i in range(len(text)):
        curr = text[i]
        tmp = ""
        if i + 1 != len(text) and text[i + 1].isalpha():
            tmp += text[i + 1]
        while i + 1 != len(text) and (not text[i + 1].isalpha()):
            tmp += text[i + 1]
            i += 1
        if tmp.isnumeric():
            ctr = int(tmp)

            while ctr:
                decompressed += curr
                ctr -= 1
        elif curr.isalpha():
            decompressed += curr

    return decompressed


def file_compress(filename):
    with open(filename, "r") as file:
        data = file.read().replace("\n", "")
        return compress(data)


def file_decompress(filename):
    with open(filename, "r") as file:
        data = file.read().replace("\n", "")
        return decompress(data)


choice = input("You want compress or decompress your file, write your option here please: ")
file_name = input("Input your file name: ")
if choice == "compress":
    print(f"There is your compressed: {file_compress(file_name)}")
else:
    print(f"There is your decompressed: {file_decompress(file_name)}")
