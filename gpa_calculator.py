
# the points per letter grade
a = 4
a_minus = 3.7

# the credits for each class (you could make them more specific if you want)
credits = 3

# the number of classes we are using
classes_num = 1

# the letter grade for the class
biology = raw_input("what grade did you get in biology (a, a-, b+, etc)?")

# keep track of the total number of points from every class operation
total_points = 0

# declaring this variable outside of the if loop so that it can be used later
# if it were only inside the if loop then what happens if biology != 'a'? We 
# wouldn't be able to use it.
biology_points = 0
if (biology == 'a'):
    # store the result of this operation because we are going to use it twice
    points = a * credits
    biology = points
    # there is a += operator that is the same as: total_points = total_points + points
    # its a shortcut
    total_points += points
else:
    print "I didn't understand that"

# calculate the total credits
total_credits = credits * classes_num

# print out the GPA
print "your GPA is: " + str(total_points / total_credits)
