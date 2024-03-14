print("Welcome to Barbados Quiz")

playing = input("Are you ready to play? ")

if playing.lower != "yes":
    quit()

print("Okay!")
score=0

answer = input("How big is Barbados? (in mi^2) ")
if answer.lower == "166":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("On what day is Independence celebrated (Month Day) ")
if answer.lower == "November 30`":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("What kind of bird is on Barbados' Coast of Arms? ")
if answer.lower == "pelican":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("what is the National Flower Barbados? ")
if answer.lower == "pride of barbados":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("What is the official language of Barbados? ")
if answer.lower == "english":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("What is the capital of Barbados? ")
if answer.lower == "Bridgetown":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("How many parishes does Barbados have? ")
if answer.lower == "11":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("What is the National Bird of Barbados? ")
if answer.lower == "pelican":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("What is the offical motto of Barbados? ")
if answer.lower == "pride and industry":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

answer = input("What is the official religion of Barbados? ")
if answer.lower == "christianity":
    print('Correct!')
    score += 1
else: 
    print('Incorrect')

print ("you got " + str(score) +" questions correct!")
