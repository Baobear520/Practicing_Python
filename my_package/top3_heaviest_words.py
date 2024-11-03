
from functools import reduce
import string


def top3_heaviest_words(input: str):
    alphabet = list(string.ascii_lowercase)

    chars_map = {
        letter:weight for weight, letter in enumerate(alphabet)
        }
    chars_map.update({"-":0, "'":0})

    words_list = set([word.strip(",").lower() for word in input.split()])
    print(words_list)

    weight_map = {}
    for word in words_list:
        weight = sum(chars_map.get(letter) for letter in word)
        weight_map.update({word: weight})
        print(f"{word} weighs {weight}")
        print(weight_map)
    

if __name__ == "__main__":
    text = "A quick brown Fox - yeah, that's a thing but hokey-pokey"
    top3_heaviest_words(input=text)
       
