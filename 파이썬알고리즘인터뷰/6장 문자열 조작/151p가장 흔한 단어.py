from typing import List
from collections import Counter
import re
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]

print(mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))