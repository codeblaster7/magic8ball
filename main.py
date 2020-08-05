import random
import time

print("Welcome to Magic 8 Ball!")

responses_1 = ["It is certain", "It is decidedly so...", "Without a doubt",
               "Yes – definitely", "My reply is no", "Don’t count on it",
               "My sources say no"]
responses_2 = ["You will rely on it...", "You will regret", "You should!", "Go for it"]
responses_3 = ["Ask again later", "Better not tell you now", "Cannot predict now",
               "Concentrate and ask again"]

question = input("What's your question? ")

if "will" in question.lower():
    answer = random.choice(responses_1)
    print("Contacting to oracle...")
    time.sleep(2)
    print(f'Magic 8 Ball says "{answer}"')
elif "should i" in question.lower():
    answer = random.choice(responses_2)
    print("Contacting to oracle...")
    time.sleep(2)
    print(f'Magic 8 Ball says "{answer}"')
else:
    answers = [random.choice(responses_3), random.choice(responses_1)]
    answer = random.choice(answers)
    print("Contacting to oracle...")
    time.sleep(2)
    print(f'Magic 8 Ball says "{answer}"')