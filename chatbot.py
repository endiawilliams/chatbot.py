import nltk

print("Hi, I'm chatbot.py! Nice to meet you.")

user_response = input()

while user_response != "Goodbye.":
    print("Tell me more.")
    user_response = input()

print("Bye.")