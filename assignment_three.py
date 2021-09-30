def function_purpose():
    """
    Khalid. Last modified on 9/30/2021. Purpose of the program is to calculate the surface area of rectangular prisms.
    :return:
    """
    print("This program computes the surface area of a rectangular prism.")
    print("Please input the length height, and width of the solid")
def get_length():
    length = float(input("please enter length:"))
    return length
def get_width():
    width = float(input("please enter width:"))
    return width
def get_height():
    height = float(input("please enter height:"))
    return height
def area(l, w):
    """
    this functions calculates the area of a rectangle
    :param l: this tells length
    :param w: this tells width
    :return: area of a rectangle
    """
    return l*w

def surface_area(l, w, h):
    """
    the function calculates the total surface area
    :param l: this tells the length
    :param w: this tells the width
    :param h: this tells the height
    :return: total surface area
    """
    top_bottom = area(l, w)*2
    left_right = h*l*2
    front_back = h*w*2
    surface = float(top_bottom)+float(left_right)+float(front_back)
    return surface
def main():
    function_purpose()
    width = get_width()
    height = get_height()
    length = get_length()
    print("the surface area is",surface_area(length, width, height) )

if __name__ == '__main__':
    main()