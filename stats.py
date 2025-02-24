import sys

def count_words(file_text):
        total = 0
        words = file_text.split()
        for word in words:
                total += 1
        return total


def count_characters(file_text):
    lowercase = file_text.lower()
    char_counts = {}
    for char in lowercase:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def generate_report(counted_words, counted_characters):
    filepath = sys.argv[1]
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {filepath}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {counted_words} total words\n"
    report += f"--------- Character Count -------\n"
    
    for char, count in counted_characters.items():
        if char.isalpha():
            report += f"{char}: {count}\n"
    report += "============= END ===============\n"
    return report
