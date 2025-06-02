def count_squares(rect_width, rect_height, square_side):

    if square_side <= 0:
        return 0
    return (rect_width // square_side) * (rect_height // square_side)

print(count_squares(10, 5, 2))







