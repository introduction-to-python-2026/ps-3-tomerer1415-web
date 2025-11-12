def move(my_list, direction):
    # Finds the index of the one in the list
    index_of_one = my_list.index(1)

    # Move the one to the right, if possible
    if direction == 'right':
        if index_of_one < len(my_list) - 1:  # Check if not at the right edge
            my_list[index_of_one] = 0
            my_list[index_of_one + 1] = 1

    # Move the one to the left, if possible
    elif direction == 'left':
        if index_of_one > 0:  # Check if not at the left edge
            my_list[index_of_one] = 0
            my_list[index_of_one - 1] = 1

    return my_list
