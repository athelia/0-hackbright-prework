# 1 - 1
def about_you():
    first_name = input("Tell us your first name: ")
    last_name = input("Tell us your last name: ")
    color = input("What's your favorite color? ")
    pets = input("How many pets do you have? ")
    greeting = "Thanks! Your name is " + first_name + " " + last_name + ", your favorite color is " + color + ", and you have " + pets + " pets."
    return greeting

# 1 - 2
paragraph = """An invitation to dinner was soon afterwards dispatched;
and already had Mrs. Bennet planned the courses that were to do credit
to her housekeeping, when an answer arrived which deferred it all. Mr.
Bingley was obliged to be in town the following day, and, consequently,
unable to accept the honour of their invitation, etc. Mrs. Bennet was
quite disconcerted.
"""
average_rating = 4.56789123

'{:.10}'.format(paragraph) + "..."
'{:.2f}'.format(average_rating)

# 1 - 3
# 
# first_name = "Sally"
# first_name[0] = "C"
# 
# This is invalid because strings are immutable. 
