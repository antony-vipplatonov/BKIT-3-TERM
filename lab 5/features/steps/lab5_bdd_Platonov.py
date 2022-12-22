from behave import Given, When, Then
import sys

sys.path.append("../../../lab 2/lab_python_oop")

from rectangle import Rectangle
from circle import Circle
from square import Square


@Given('rectangle with sides of "{first}" and "{second}", color is "{color}"')
def step_impl(context, first, second, color):
    global shape
    try:
        shape = Rectangle(color, int(first), int(second))
        return True
    except:
        return False


@Given('circle with radius of "{radius}", color is "{color}"')
def step_impl(context, radius, color):
    global shape
    try:
        shape = Circle(color, int(radius))
        return True
    except:
        return False


@Given('square with side of "{side}", color is "{color}"')
def step_impl(context, side, color):
    global shape
    try:
        shape = Square(color, int(side))
        return True
    except:
        return False


@When('we try to get properties')
def step_impl(context):
    if shape.square():
        if shape.get_figure_type():
            if shape.fc.colorproperty:
                return True
    return False


@Then('we get square of "{square}", color is "{color}"')
def step_impl(context, square, color):
    if shape.square() == square:
        if shape.fc.colorproperty == color:
                return True
    return False
