import re
import random


def do_n_gram(doc: str, n: int) -> tuple[list[tuple[str, int]], list[str]]:
    text = doc

    # 定義正則表達式模式，用來匹配標點符號
    pattern = r'[^\w\s]'

    # 使用re.sub()函數去除標點符號
    text = re.sub(pattern, '', text)
    text = re.sub("\n", " ", text)

    words = text.split()

    n = n
    freq = {}
    for i in range(len(words) - (n-1)):
        n_gram = " ".join(words[i:i+n]).lower()
        freq[n_gram] = freq.get(n_gram, 0) + 1
        
    freq = sorted(freq.items(), key=lambda word_count: word_count[1], reverse=True)
    
    return freq, words


def make_prediction(n_gram_freq: list[tuple[str, int]], start_word: str, n_words: int) -> list[str]:
    prediction = [start_word]
    word = start_word
    for _ in range(n_words):
        word = next((word_pairs.split()[1] for (word_pairs, _) in n_gram_freq if word_pairs.split()[0] == word), None)

        if not word:
            break
        else:
            prediction.append(word)
    
    return prediction


def main() -> None:
    with open("article.txt", "r", encoding="utf-8-sig") as f:
        text = f.read()
        n_gram_freq, words = do_n_gram(text, 2)
        start_word = random.choice(words).lower()
        print(make_prediction(n_gram_freq, start_word, 10))


if __name__ == "__main__":
    main()    