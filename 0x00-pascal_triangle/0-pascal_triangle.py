#!/usr/bin/python3
'''Module to return Pascal's triangle'''

def pascal_triangle(n):
    '''
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    '''
    if n <= 0:
        return []

    pasTran = []

    for b in range(n):
        # Start the row with 1
        my_List = [1]
        if b > 0:
            last_row = pasTran[-1]
            for j in range(1, b):
                my_List.append(last_row[j - 1] + last_row[j])
            # End the row with 1 if not the first row
            my_List.append(1)
        pasTran.append(my_List)

    return pasTran

