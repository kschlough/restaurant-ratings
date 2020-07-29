def restaurant_ratings(file):
    """Restaurant rating lister."""
    restaurant_file = open(file)
    restaurant_dictionary = {}
    for line in restaurant_file:
        restaurant_list = line.rstrip().split(":")
        restaurant_dictionary[restaurant_list[0]] = restaurant_list[1]
    print("Welcome to the restaurant lister!")
    print("Add your restaurant and rating to view the list.")
    restaurant_name = input("Enter the restaurant name: >> ").title()
    restaurant_score = input("Enter your rating for this restaurant: >> ")
    restaurant_dictionary[restaurant_name] = restaurant_score
    for key,value in sorted(restaurant_dictionary.items()):     
        print(f'{key} is rated at {value}.')
    
    restaurant_file.close()

restaurant_ratings("scores.txt")



# pseudocode
# define our function
# create a blank dictionary
# pass in our file & open it
# for each line in the file:
    # rstrip and split using ":"
    # store each restaurant & rating in the dictionary
    # use .items() to get a list of dictionary entries
    # call sorted() on the list to get alphabetical order
# return/print sorted() dictionary

# call the function (print it if we use a return)
