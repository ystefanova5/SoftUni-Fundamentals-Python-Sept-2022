first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")
winner = 0
if "1" == first_line[0] == first_line[1] == first_line[2] or \
        "1" == second_line[0] == second_line[1] == second_line[2] or \
        "1" == third_line[0] == third_line[1] == third_line[2] or \
        "1" == first_line[0] == second_line[0] == third_line[0] or \
        "1" == first_line[1] == second_line[1] == third_line[1] or \
        "1" == first_line[2] == second_line[2] == third_line[2] or \
        "1" == first_line[0] == second_line[1] == third_line[2] or \
        "1" == first_line[2] == second_line[1] == third_line[0]:
    winner = "1"
elif "2" == first_line[0] == first_line[1] == first_line[2] or \
        "2" == second_line[0] == second_line[1] == second_line[2] or \
        "2" == third_line[0] == third_line[1] == third_line[2] or \
        "2" == first_line[0] == second_line[0] == third_line[0] or \
        "2" == first_line[1] == second_line[1] == third_line[1] or \
        "2" == first_line[2] == second_line[2] == third_line[2] or \
        "2" == first_line[0] == second_line[1] == third_line[2] or \
        "2" == first_line[2] == second_line[1] == third_line[0]:
    winner = "2"
if winner == "1":
    print("First player won")
elif winner == "2":
    print("Second player won")
else:
    print("Draw!")


################################################   Task Description   ################################################
# 5. Tic-Tac-Toe
# You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
# Legend:
#         • 0 - empty space
#         • 1 - first player move
#         • 2 - second player move
# Find out who the winner is. If the first player wins, print "First player won". 
# If the second player wins, print "Second player won". Otherwise, print "Draw!".
