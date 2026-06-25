import re
from collections import Counter

def count_words_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read().lower()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    return Counter(words)