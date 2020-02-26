""" Name - Akshay Lavhagale
    HW 01: Testing triangle classification
    The function returns a string that specifies whether the triangle is scalene,
    isosceles, or equilateral, and whether it is a right triangle as well. """


def classify_triangle(side_1, side_2, side_3):
    """Triangle classification method"""
    try:
        side_1 = float(side_1)
        side_2 = float(side_2)
        side_3 = float(side_3)
    except ValueError:
        raise ValueError("The input value is not number")
    else:
        [side_1, side_2, side_3] = sorted([side_1, side_2, side_3])
        if (side_1 + side_2 < side_3 and side_1 + side_3 < side_2 and side_2 + side_3 < side_1) or (
                side_1 or side_2 or side_3) <= 0:
            return "This is not a triangle"
        else:
            if round(((side_1 ** 2) + (side_2 ** 2)), 2) == round((side_3 ** 2), 2):
                if side_1 == side_2 or side_2 == side_3 or side_3 == side_1:
                    return 'Right and Isosceles Triangle'
                else:
                    return 'Right and Scalene Triangle'
            elif side_1 == side_2 == side_3:
                return "Equilateral"
            if side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
                return "Isosceles"
            else:
                return "Scalene"
