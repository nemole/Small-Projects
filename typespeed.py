import time
import random
word = ""

for i in range(15):
    num = random.randint(97, 122)
    word = word + chr(num)

first = time.perf_counter()
print("Type: " + word)
while True:
    answer = input("Type the word: ")
    if answer == word:
        break

t = str(time.perf_counter() - first)
print("You typed the word in " + t + " seconds")


