# Create three variables called score1, score2, score3
score1 = 10
score2 = 20
score3 = 30

average_score1 = (score1 + score2 + score3) / 3



# Implementing the functional approach

def average_score(num1, num2, num3):
    score =  (num1 + num2 + num3)/3
    return score

average_score2 = average_score(score1, score2, score3)
print(average_score2)