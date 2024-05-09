import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user,computer):
        return "you won!"
    if is_win(computer,user):
        return "you lost"
    # r > s, s > p, p > r

def is_win(player,opponent):
    # RETURN TRUE IF PLAYER WINS
    if (player == 'r' and opponent == 's') \
        or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
            return True


print(play())