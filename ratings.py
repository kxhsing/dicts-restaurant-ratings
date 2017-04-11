"""Restaurant rating lister."""

def restaurant_ratings(filename):
    """Get restaurant ratings and store in dictionary sorted
    and print restaurant with rating"""

    lines = open(filename)

    restaurant_dict = {}


    for restaurants in lines:
        restaurants = restaurants.rstrip()
        restaurant, rating = restaurants.split(":")

        restaurant_dict[restaurant] = int(rating)

    # user_input_restaurant()

    # restaurant_dict[user_restaurant_input[0]] = user_restaurant_input[1]

    # sorted_restaurants = sorted(restaurant_dict.items())


    # for restaurant, rating in sorted_restaurants:
    #     print "%s is rated at %s" % (restaurant, rating)

    return restaurant_dict

def user_choice():
    choice = raw_input("Would you like to:\n1. See all ratings\n2. Add new restaurant\n3. quit")



def user_input_restaurant(restaurant_dict):

    user_restaurant = raw_input("Restaurant name? ")

    while True:
        user_restaurant_rating = int(raw_input("Restaurant rating? "))
        if user_restaurant_rating in range(1, 6):
            restaurant_dict[user_restaurant] = user_restaurant_rating

            return restaurant_dict


        else:
            print "Not a valid rating. Please input number"






restaurant_dict = restaurant_ratings("scores.txt")
restaurant_dict = user_input_restaurant(restaurant_dict)
print restaurant_dict











