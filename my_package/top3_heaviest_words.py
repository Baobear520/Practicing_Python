
from functools import reduce
import string


def top3_heaviest_words(input: str):
    alphabet = list(string.ascii_lowercase)

    chars_map = {
        letter:weight for weight, letter in enumerate(alphabet)
        }
    chars_map.update({"-":0, "'":0})

    words_hashmap = {
        # keys are words with stripped commas
        # values are results of summing all weights in each word
        word.strip(",").lower(): sum(chars_map.get(letter,0) for letter in word) 
        for word in input.split()
        }
    
    print(sorted(words_hashmap.items(),key=lambda item: item[1], reverse=True)[:3])
    

if __name__ == "__main__":
    text = "A quick brown Fox - yeah, that's a thing but hokey-pokey"
    top3_heaviest_words(input=text)
       
