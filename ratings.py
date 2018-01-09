"""Restaurant rating lister."""

import sys


# put your code here
def main_function(file_name):
    restaurant_ratings = create_restaurant_ratings(file_name)
    while True:
        print """
                 1. Let me see all of the restaurant ratings
                 2. I want to add a new restaurant
                 3. I want to quit        
              """

        user_choice = raw_input("What is your choice? > ")

        if user_choice == "1":
            print_restaurant(restaurant_ratings)

        elif user_choice == "2":
            get_user_input(restaurant_ratings)
    
        elif user_choice == '3':
            break


def create_restaurant_ratings(file_name):
    restaurant_ratings = {}
    with open(file_name) as my_file:
        for line in my_file:
            line = line.rstrip()
            rest, rating = line.split(":")
            restaurant_ratings[rest] = rating
    return restaurant_ratings


def print_restaurant(restaurant_ratings):
    for rest, rat in sorted(restaurant_ratings.items()):
        print "{name} is rated at {score}.".format(name=rest, score=rat)
        # print "{} is rated at {}.".format(rest, rat)


def get_user_input(restaurant_ratings):
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
    restaurant_ratings[restaurant] = user_rating


main_function(sys.argv[1])
