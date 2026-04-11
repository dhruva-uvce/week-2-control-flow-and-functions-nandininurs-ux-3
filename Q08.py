# Q08. Sum of Digits (while loop)
#
# Ask the user for a positive integer.
# Print the sum of its digits using a while loop.
#
# Sample Input:   Enter a number: 9876
# Sample Output:  Sum of digits of 9876 = 30

# --- YOUR CODE HERE ---
n=int(input("Enter a number : "))
rem=0
temp=0
while (n>0):
    rem=n%10
    temp=temp+rem
    n=n//10
print(f"sum of digits of {n} = {temp}")
