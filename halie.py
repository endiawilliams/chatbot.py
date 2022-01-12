import nltk
from nltk.tokenize import word_tokenize

# noun, plural noun, proper noun, plural proper noun
noun_codes = ["NN", "NNS", "NNP", "NNPS"]

def id_pos(user_response):
    output = nltk.pos_tag(word_tokenize(user_response))

    noun_exists = False

    for (word, pos) in output:
        if pos in noun_codes:
            noun_exists = True
            print(word + " is the first noun of the sentence.")
            break
        if pos == "PRP":
            noun_exists = True
            print(word + " is the first personal pronoun of the sentence.")
            break

    if noun_exists == False:
        print("No nouns or personal pronouns were found.")

print("Hi, I'm HALIE! Nice to meet you.")

user_response = input()

while user_response != "Goodbye.":
    id_pos(user_response)
    user_response = input()

print("Bye.")