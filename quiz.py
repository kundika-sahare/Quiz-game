print("Welcome to my computer quiz!")

playing = input("Do you want to play the quiz? ")

if playing.lower() != "yes":
    quit()
    
print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does API stand for? ")
if answer.lower() == "application program interface":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does AI stand for? ")
if answer.lower() == "artificial intelligence":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")