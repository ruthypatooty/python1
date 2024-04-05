print("My First Official Python thing!!!")
playing = input("Start game?\n")

if playing.lower() != "yes":
    quit()

print("Let's play!!")
score = 0

answer = input("What is a colorless liquid called? ")

if answer.lower() == "water":
    print("Correct!")
    score +=1
else:
    print("Incorrect!!!!!!")

answer = input("What meal is after breakfast? ")

if answer.lower() == "lunch":
    print("Correct!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("What day is after Tuesday? ")

if answer.lower() == "wednesday":
    print("Correct!")
    score +=1
else:
    print("Incorrect!!!")

answer = input("What is the synonym of fast? ")

if answer.lower() == "quick":
    print("Correct!")
    score +=1
else:
    print("Incorrect!!!")

print("Your raw score is "+str(score))
print("Percentage is "+str((score/4)*100)+"%")