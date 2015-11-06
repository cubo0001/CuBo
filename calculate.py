uthor__ = 'mk'
def calculate(x, y, operator):
    """
    simple calculate function with 4 main operator
    in this function I ask you to use if else instead of switch case
    :param x: the first number
    :param y: the second number
    :param operator: i define that it's a integer from 1 to 4: 1 is add, 2 is minus, 3 is multi and 4 is divide
    :return: result when after calculating x y with sign
    """


    # add
    if operator == 1:
        return x + y
    # tung
    #Multi


    return 0
def main_function():
    """
    free edit this function as main method, but you have to commit change of this function to github
    :return:
    """

    print(calculate(5, 2, 1))

    print (calculate(4,3,3))




main_function()
