"""Restaurant rating lister."""


# put your code here
def create_restaurant_ratings(file_name):

    restaurant_ratings = {}
    with open(file_name) as my_file:

        for line in my_file:

            line = line.rstrip()
            rating = line.split(":")
            #print(rating)
            restaurant_ratings[rating[0]] = rating[1]

    new_list = sorted(restaurant_ratings.items())
    for rest, rat in new_list:
        print rest + " is rated at " + rat + "."




create_restaurant_ratings("scores.txt")
