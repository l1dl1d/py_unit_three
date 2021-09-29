def function_purpose():
    print("This program computes the surface area of a rectangular prism.")
    print("Please input the length height, and width of the solid")
    return
length = float(input("please enter length:"))
width = float(input("please enter width:"))
height = float(input("please enter height:"))
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
    print("the surface area is", float(surface))

surface_area(length, width, height)