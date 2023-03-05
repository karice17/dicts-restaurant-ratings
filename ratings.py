"""Restaurant rating lister."""


 #define funtion
 
def read_file(filename):
    '''read text file and return list of lines'''

    text = open(filename)

    #read lines
    #sample data "Donut You Want Me Baby:1"
    return text.readlines()  # ["Penne For Your Thoughts:4", "Ramen On Empty:3", ...]
    

def create_rest_ratings_dict(read_file):
    ''' take list from read_file function and create dictonary of results'''

    ratings_dict = {}  
    # {"Penne For Your Thoughts": "4"}
    for line in read_file:
        line_split = line.split(":") 
        ratings_dict[line_split[0]] = line_split[1] 
    
    return ratings_dict 

def alphabetize_rest_ratings(ratings_dict):
    '''Alphabetize the dictionary from function create_rest_ratings_dict'''

    restaurants_sorted = sorted(ratings_dict.keys())

    
    for restaurant in restaurants_sorted:
        print(f"{restaurant} is rated at {ratings_dict[restaurant]}")


ratings_dictionary = create_rest_ratings_dict(read_file("scores.txt"))

alphabetize_rest_ratings(ratings_dictionary)
