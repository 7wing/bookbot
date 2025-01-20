def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        word_count = count_words(file_contents)
        char_count = count_characters(file_contents)
        sorted_char_count = sorted(char_count.items(), key=sort_on, reverse=True)
        # print(word_count)
        # print(char_count)
        report = generate_report(word_count, dict(sorted_char_count))
        print(report) 


def count_words(file_contents):
    total = 0
    words = file_contents.split()
    for word in words:
        total += 1
    return total

def count_characters(file_contents):
    lowercase = file_contents.lower()
    char_counts = {}
    for char in lowercase:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item[1]

def generate_report(word_count, char_count):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{word_count}  words found in the document\n" 
    for char, count in char_count.items():
        if char.isalpha():
            report += f"The '{char}' character was found {count} times\n"
    report += "--- End report ---"
    return report


main()