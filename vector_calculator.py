import numpy as np


def main():
    results_list = []
    while True:
        op_type = input("Press p for projection vector calculator, n for normal vector calculator (x to exit):")
        if op_type.lower() == "n":
            res = 0
            custom_dimension = int(input("Vector space dimension? "))
            custom_amount = int(input("Amount of vectors? "))
            if custom_amount == 1:
                res = singular_calculate(vectors(custom_dimension, 1))
                print(res)
            else:
                res = multiple_calculate(vectors(custom_dimension, custom_amount))
                print(res)
            results_list.append(res)
            inp = input(
                "Press x to quit, h to get result history, any other key to continue: ")
            if inp == "h".lower():
                results_list.append(handle_results(results_list))
                print(results_list[-1])
                if input("Continue? x to quit: ") == "x".lower():
                    exit()
            elif inp == "x".lower():
                exit()
            else:
                continue
        elif op_type.lower() == "p":
            print(proj(proj_vectors(int(input("Vector dimension: ")))))
        elif op_type.lower() == "x":
            exit()
        else:
            continue


def vectors(dimension=int, amount=int):
    # function that returns a numpy array (vector) in accordance to 2 params:
    # dimension = the amount of components in a vector
    # amount = the amount of vectors in total
    vector_collection = []
    for i_vector in range(amount):
        # adds each vector to vector_collection
        vector = []
        for component in range(dimension):
            # adds components per vector
            vector.append(
                int(input(f"({i_vector+1}'s) component v_{component+1}?: ")))
        vector_collection.append(np.array(vector))
    if len(vector_collection) == 1:
        return vector_collection[0]
    else:
        return vector_collection


def multiple_calculate(vector=list):
    # gets called if multiple vectors are involved
    if len(vector) == 2:
        operation = str(input("Operation (+, -, .): "))
        if operation == ".":
            return np.sum(np.multiply.reduce(vector))
        else:
            match operation:
                case "+":
                    return np.add(vector[0], vector[1])
                case "-":
                    return np.subtract(vector[0], vector[1])
    else:
        operation = str(input("Operation (+, -): "))
        match operation:
            case "+":
                return np.add.reduce(vector)
            case "-":
                return np.subtract.reduce(vector)


def singular_calculate(vector):
    # gets called if user defines only one vector
    operation = str(input("Scalar operation (*): "))
    match operation:
        case "*":
            n = int(input("Multiply with: "))
            return n * vector


def handle_results(list=list):
    # accessing the list of results, performing operations based on index
    i = 0
    result_dict = {}
    for result in list:
        i += 1
        print(f"Result {i}: {result}")
        result_dict[i] = result
    print(result_dict)
    if str(input("Calculate results with each other? y for yes: ")) == "y".lower():
        selected = input(
            "Select the results to work with via their respective numbers (e.g 1, 3, 5...): ").split(",")
        selected_b = [eval(i) for i in selected]
        to_handle = []
        for key in result_dict.keys():
            for number_value in selected_b:
                if key == number_value:
                    to_handle.append(np.array(result_dict[key]))
        if len(to_handle) == 1:
            return singular_calculate(to_handle)
        else:
            return multiple_calculate(to_handle)
    else:
        return None

def proj_vectors(dimension):
    v_list = []
    for i in range(2):
        vector = []
        for i in range(dimension):
            vector.append(int(input(f"Component {i+1}: ")))
        v_list.append(np.array(vector))
    return v_list


def proj(list):
    dividend = np.dot(list[0], list[1])
    divisor = np.dot(list[0], list[0])
    scalar_value = dividend / divisor
    return scalar_value * list[0]


main()
