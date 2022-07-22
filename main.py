import time
print("Enter your username: ")
name = str(input())
print("Welcome,", name, "to Quiz 1.1!")
print("Type 's' to start")
c = input()
right = 0
if c == "S" or c == "s":
    print("Good Luck!")
    print("Q1. Which country has the highest life expectancy?")
    print("A. India")
    print("B. Hong Kong")
    print("C. Japan")
    print("D. USA")
    a = input()
    if a == "B" or a == "b":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q2. Where would you be if you were standing on the Spanish Steps?")
    print("A. Canada")
    print("B. Japan")
    print("C. Rome")
    print("D. USA")
    a = input()
    if a == "C" or a == "c":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q3. Which language has the more native speakers: English or Spanish?")
    print("A. English")
    print("B. Spanish")
    a = input()
    if a == "B" or a == "b":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q4. What is the most common surname in the United States?")
    print("A. Jones")
    print("B. Davis")
    print("C. Miller")
    print("D. Smith")
    a = input()
    if a == "D" or a == "d":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q5. What disease commonly spread on pirate ships?")
    print("A. Scurvy")
    print("B. Jondis")
    print("C. COVID-19")
    print("D. Fever")
    a = input()
    if a == "A" or a == "a":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q6. Who was the Ancient Greek God of the Sun?")
    print("A. Ra")
    print("B. Apollo")
    print("C. Zues")
    print("D. Hera")
    a = input()
    if a == "B" or a == "b":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q7. When was the United Nations established?")
    print("A. 1944")
    print("B. 1851")
    print("C. 1951")
    print("D. 1945")
    a = input()
    if a == "D" or a == "d":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q8. Who has won the most total Academy Awards?")
    print("A. Walt Disney")
    print("B. Marvel Studios")
    print("C. Sony Pictures")
    print("D. None of the above")
    a = input()
    if a == "A" or a == "a":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q9. Who has the most streams in Spotify?")
    print("A. Imagine Dragons")
    print("B. Harry Styles")
    print("C. Drake")
    print("D. ED Sheeran")
    a = input()
    if a == "C" or a == "c":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")

    print("Q10. What is the max length of a TikTok video?")
    print("A. 60 Secs")
    print("B. 1 hour")
    print("C. 30 sec")
    print("D. 1 day")
    a = input()
    if a == "A" or a == "a":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")
    print("OK... That was easy")
    time.sleep(3)
    print("Get Ready for level 2!")
    time.sleep(3)
    print("Level 2 start in...")
    for seconds in range(5, 0, -1):
        print(seconds)
        time.sleep(1)
    print("Q1. Name the component of blood that fights infection?")
    print("A. RBC")
    print("B. WBC")
    print("C. Plasma")
    print("D. None of the above")
    a = input()
    if a == "B" or a == "b":
        print("Correct!")
        right = right + 1
    else:
        print("Wrong :(")
    if right == 1:
        print("You got only", str(right), "answer correct out of 10")
        print("You gotta study hard")
    elif right == 0:
        print("You gotta study hard")
    else:
        print("You got", str(right), "answers correct out of 10")
    q = (right / 11) * 100
    print("That means your accuracy is", str(q) + "%")
    print("Finished with code 0")
    print("Press enter to exit")
    enter = input()
else:
    print("Hah! Loser!")
