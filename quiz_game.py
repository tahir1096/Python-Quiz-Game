print("Hello, & Welcome to the Quiz! ")
play = input("Can we start playing quiz? ")
if play.lower() != "yes":
    quit()
def game():
    print("Okay let's play: ")
    score = 0
    answer1 = input ("Whats does CPU stands for? ")
    if answer1.lower() == "Central Processing Unit".lower():
        score = score + 1

    answer2 = input("What does GPU stand for? ")
    if answer2.lower() == "Graphics Processing Unit".lower():
        score = score + 1

    answer3 = input("What does RAM stand for? ")
    if answer3.lower() == "Random Access Memory".lower():
        score = score + 1

    answer4 = input("What does ROM stand for? ")
    if answer4.lower() == "Read Only Memory".lower():
        score = score + 1

    answer5 = input("What does HTTP stand for? ")
    if answer5.lower() == "HyperText Transfer Protocol".lower():
        score = score + 1

    answer6 = input("What does HTML stand for? ")
    if answer6.lower() == "HyperText Markup Language".lower():
        score = score + 1

    answer7 = input("What does CSS stand for? ")
    if answer7.lower() == "Cascading Style Sheets".lower():
        score = score + 1

    answer8 = input("What does USB stand for? ")
    if answer8.lower() == "Universal Serial Bus".lower():
        score = score + 1

    answer9 = input("What does IP stand for? ")
    if answer9.lower() == "Internet Protocol".lower():
        score = score + 1

    answer10 = input("What does DNS stand for? ")
    if answer10.lower() == "Domain Name System".lower():
        score = score + 1
    if score == 0:
        print("Your total score is:", score, "/10 ☹")
        print(f"Percentage : ({(score/10)*100}%)")
    if  1 < score <=5:
        print("Your total score is:", score, "/10 😐")
        print(f"Percentage : ({(score/10)*100}%)")
    if 5 < score <= 10:
        print("Your total score is:", score, "/10 😍")
        print(f"Percentage : ({(score/10)*100}%)")
game()
re_play = input("Do you want to play again? ")
if re_play.lower() == "yes".lower():
    game()
