# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
s=int(input("Enter your score : "))
if(s>100 or s<0):
    print("Invalid Score")
else:
    if(s>=90 and s<=100):
        print("Grade: A")
    if(s>=80 and s<90):
        print("Grade: B")
    if(s>=70 and s<80):
        print("Grade: C")
    if(s>=60 and s<70):
        print("Grade: D")
    if(s<60):
        print("Grade: F")
