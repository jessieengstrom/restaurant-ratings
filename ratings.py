"""Restaurant rating lister."""

import sys


# put your code here
def create_restaurant_ratings(file_name):

    restaurant = raw_input("What restaurant are you rating? > ")

    while True:
        try:
            user_rating = int(raw_input("What is your rating? > "))
            if user_rating < 1 or user_rating > 5:
                print "Rating should be between 1 and 5"
            else:
                break
        except ValueError:
            print "Please enter an integer only"

    restaurant_ratings = {restaurant: user_rating}
    with open(file_name) as my_file:

        for line in my_file:

            line = line.rstrip()
            rating = line.split(":")
            #print(rating)
            restaurant_ratings[rating[0]] = rating[1]

    new_list = sorted(restaurant_ratings.items())
    for rest, rat in new_list:
        print rest + " is rated at " + str(rat) + "."


create_restaurant_ratings(sys.argv[1])
