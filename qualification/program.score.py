


#=============================================================================


INPUT_FILES = [
    "qualification/input/a.txt",
    "qualification/input/b.txt",
    "qualification/input/c.txt",
    "qualification/input/d.txt",
    "qualification/input/e.txt",
    "qualification/input/f.txt"
]


OUTPUT_FILES = [
    "qualification/output/a.out",
    "qualification/output/b.out",
    "qualification/output/c.out",
    "qualification/output/d.out",
    "qualification/output/e.out",
    "qualification/output/f.out"
]


#=============================================================================


def file_to_array(input_file):
    """Turns the input space-separated-file into a 2D array over line and space"""

    with open(input_file) as csv_file:
        csv_text = csv_file.read()

    array = csv_text.split("\n")
    for i in range(0, len(array)):
        array[i] = array[i].strip().split(" ")

    array = array[:-1]

    return array


def array_to_file(array, output_file):
    """Turns the output 2D array into a space-separated-file"""

    array_str = []

    for line in array:
        line_str = ""
        for word in line:
            line_str += str(word) + " "

        line_str = line_str.strip() + "\n"
        array_str.append(line_str)


    with open(output_file, "w") as output_file:
        output_file.writelines(array_str)


#=============================================================================


def parse(array):
    time = int(array[0][0])
    nb_intersections = int(array[0][1])
    nb_streets = int(array[0][2])
    nb_cars = int(array[0][3])
    nb_score_per_car = int(array[0][4])
    
    streets = array[1:1+nb_streets] 
    
    for i in range(0, len(streets)):
        streets[i] = [int(streets[i][0]), int(streets[i][1]), streets[i][2], int(streets[i][3])]
                      
    paths = array[1+nb_streets:]
    
    for i in range(0, len(paths)):
        paths[i][0] = int(paths[i][0])
        

    return time, nb_intersections, nb_streets, nb_cars, nb_score_per_car, streets, paths
    

def algo(array):
    
    time, nb_intersections, nb_streets, nb_cars, nb_score_per_car, streets, paths = parse(array)
    # The number of intersections with schedules
    # the id of the intersction
    # the number of streets which are defined for the intersection
    # For each street up to number of defined streets 
    #   => The name of the street 

    print(parse(array))
    
    return 0

def calculate_score(result,input,pizza_list):
    nb_intersections = result[0][0]
    array = result[1:]
    score = 0
    next_intersection = 2
    for i in range(nb_intersections):
        for j in range(result[next_intersection]):
            result[next_intersection]
    for i in range(len(array)):
        ingredients_set = set()
        nb_pizzas = array[i][0]
        tmp_res = array[i][1:]
        for pizza_nb in tmp_res:
            pizza = pizza_list[pizza_nb]
            for ingredient in pizza:
                ingredients_set.add(ingredient)
        score += len(ingredients_set)**2
    return score

def main(input_file, output_file):
    array = file_to_array(input_file)

    result = algo(array)

    # array_to_file(result, output_file)


main(INPUT_FILES[0], OUTPUT_FILES[0])
