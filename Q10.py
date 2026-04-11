# Q10. Call by Reference — List Mutations
#
# Write the following two functions:
#
#   add_element(lst, element)
#       Appends element to lst in-place. Returns nothing.
#
#   double_elements(lst)
#       Multiplies every element in lst by 2 in-place. Returns nothing.
#
# Then in the main block:
#   1. Create numbers = [1, 2, 3]
#   2. Call add_element(numbers, 4) and print the list  → [1, 2, 3, 4]
#   3. Call double_elements(numbers) and print the list → [2, 4, 6, 8]


def add_element(lst, element):
    # --- YOUR CODE HERE ---
    return 1st.append(element)
    pass


def double_elements(lst):
    # --- YOUR CODE HERE ---
    a=[]
    for i in 1st:
     i=i*2
     a.append(i)
    return a
    pass


if __name__ == "__main__":
    # Demonstrate call by reference
    # --- YOUR CODE HERE ---
    print(add_element([1,2,3],5))
    print(double_elements[1,2,3,5])
    pass
