student_scores = [150,123,123,143,167,173,187,186,176,156,199,100,134,175,134,153,163,143,132,125]
high_score = 0
for marks in student_scores:
    if marks > high_score:
        high_score = marks

print(high_score)

total =  0
for i in range(1,101):
    total += i
print(total)

