"""Restaurant rating lister."""

def restaurant_ratings(filename):
    lines = open(filename)

    restaurant_dict = {}


    for restaurants in lines:

        restaurants = restaurants.rstrip()
        restaurant = restaurants.split(":")

        restaurant_dict[restaurant[0]] = restaurant[1]

    sorted_restaurants = sorted(restaurant_dict.items())
    #print sorted_restaurants

    for restaurant, ratings in sorted_restaurants:
        print "%s is rated at %s" % (restaurant, ratings)














