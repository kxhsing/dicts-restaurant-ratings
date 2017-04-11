"""Restaurant rating lister."""

def restaurant_ratings(filename):
    """Get restaurant ratings and store in dictionary sorted
    and print restaurant with rating"""

    lines = open(filename)

    restaurant_dict = {}


    for restaurants in lines:
        restaurants = restaurants.rstrip()
        restaurant, rating = restaurants.split(":")

        restaurant_dict[restaurant] = rating

    user_restaurant = raw_input("Restaurant name? ")
    user_restaurant_rating = raw_input("Restaurant rating? ")

    restaurant_dict[user_restaurant] = user_restaurant_rating

    sorted_restaurants = sorted(restaurant_dict.items())


    for restaurant, rating in sorted_restaurants:
        print "%s is rated at %s" % (restaurant, rating)

restaurant_ratings("scores.txt")













