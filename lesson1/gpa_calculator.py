#class name
class_name = "biology"

# the points per letter grade
a = 4
a_minus = 3.7
b_plus = 3.4
b = 3
b_minus = 2.7
c_plus = 2.4
c = 2
c_minus = 1.7
d_plus = 1.4
d = 1
f = 0

# the credits for each class (you could make them more specific if you want)
credits = 3

# the number of classes we are using
classes_num = 1

# the letter grade for the class
biology = input("what grade did you get in biology (a, a-, b+, etc)?")

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
    # the += operator is the same as: total_points = total_points + points
    # its a shortcut
    total_points += points
elif (biology == 'a-'):
    points = a_minus * credits
    biology = points
    total_points += points
elif (biology == 'b+'):
    points = b_plus * credits
    biology = points
    total_points += points
elif (biology == 'b'):
    points = b * credits
    biology = points
    total_points += points
elif (biology == 'b-'):
    points = b_minus * credits
    biology = points
    total_points += points
elif (biology == 'c+'):
    points = c_plus * credits
    biology = points
    total_points += points
elif (biology == 'c'):
    points = c * credits
    biology = points
    total_points += points
elif (biology == 'c-'):
    points = c_minus * credits
    biology = points
    total_points += points
elif (biology == 'd+'):
    points = d_plus * credits
    biology = points
    total_points += points
elif (biology == 'd'):
    points = d * credits
    biology = points
    total_points += points
else:
    print("I didn't understand that")

# calculate the total credits
total_credits = credits * classes_num

# print out the GPA
print("your GPA is: " + str(total_points / total_credits))
