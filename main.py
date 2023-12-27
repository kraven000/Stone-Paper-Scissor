import random as ran

def comp():
    return ran.randint(1,3)


def win_lose(user,comp):
    '''Zero means computer won and 1 means user won and 2 means tie'''
    if user==1 and comp==2:
        return 0
    elif user==2 and comp==3:
        return 0
    elif user==3 and comp==1:
        return 0
    elif user==comp:
        return 2
    else:
        return 1


def check(user,comp):
    if user==1:
        print("User Choice:- Stone")
    if user==2:
        print("User Choice:- Paper")
    if user==3:
        print("User Choice:- Scissor")
    if comp==1:
        print("Computer Choice:- Stone")
    if comp==2:
        print("Computer Choice:- Paper")
    if comp==3:
        print("Computer Choice:- Scissor")
    print()


if __name__=="__main__":
    win = 0
    lose = 0
    tie = 0
    print("Welcome to stone paper scissor game.\nFor stone enter 1\nFor paper enter 2\nFor scissor enter 3")
    for i in range(5):
        user = int(input("Enter:- "))
        computer = comp()
        step = win_lose(user=user,comp=computer)
        if step==0:
            check(user=user,comp=computer)
            print("You Lose, Computer Won\n")
            print()
            lose += 1
        elif step==1:
            check(user=user,comp=computer)
            print("You Won, Computer Lose\n")
            print()
            win += 1
        elif step==2:
            check(user=user,comp=computer)
            print("Tie, You both Have same thinking\n")
            print()
            tie += 1
    else:
        if win>lose:
            print("You won the match\n")
        elif win<lose:
            print("You lose the match\n")
        elif win==lose:
            print("You Tied the Match\n")

        print(f"Round Won:- {win}\nRound Lose:- {lose}\nRound Tied:- {tie}")