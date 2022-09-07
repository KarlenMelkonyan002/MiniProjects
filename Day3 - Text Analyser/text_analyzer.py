def word_count(text):
    separators = [",", ".", ":", ";"]
    for char in separators:
        text = text.replace(char, "").lower()
    words = []
    for word in text.split():
        if word not in words:
            words.append(word)
    return len(words)


def letter_count(text):
    separators = [",", ".", ":", ";", " "]
    for char in separators:
        text = text.replace(char, "").lower()
    uniques = []
    for char in text:
        if char not in uniques:
            uniques.append(char)
    return len(uniques)


def sentence_count(text):
    separators = [",", ".", ":", ";"]
    if "." not in text:
        return 1
    separators = [":", "."]
    sentences = 0
    for letter in text:
        if letter in separators:
            sentences += 1
    return sentences


def most_used_word(text):
    counts = {}
    separators = [",", ".", ":", ";"]
    for char in separators:
        text = text.replace(char, "").lower()
    for word in text.split(" "):
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    if max(counts.values()) == 1:
        return 0
    for item in counts.keys():
        if counts[item] == max(counts.values()):
            return item


def most_used_letter(text):
    counts = {}
    separators = [",", ".", ":", ";", " "]
    for char in separators:
        text = text.replace(char, "").lower()
    for letter in text:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    for item in counts.keys():
        if counts[item] == max(counts.values()):
            return item

    file_read = open(filename_r, "r")
    file_write = open(filename_w, "w")
    data = file_read.read().replace("\n", "")
    words, letters, sent, m_word, m_letter = word_count(data), letter_count(
        data), sentence_count(data), most_used_word(data), most_used_letter(data)
    file_write.write(
        f"{words} words, {letters} letters, {sent} sentences, most used word:{m_word}, most used letter:{m_letter} ")
    file_read.close()
    file_read.close()


r_file = input("Input filename that you want to analyze: ")
w_file = input("Input filename where you want to keep result: ")
file_read = open(r_file, "r")
file_write = open(w_file, "w")
data = file_read.read().replace("\n", "")
words, letters, sent, m_word, m_letter = word_count(data), letter_count(
    data), sentence_count(data), most_used_word(data), most_used_letter(data)
file_write.write(
    f"{words} words, {letters} letters, {sent} sentences, most used word:{m_word}, most used letter:{m_letter} ")
file_read.close()
file_read.close()
