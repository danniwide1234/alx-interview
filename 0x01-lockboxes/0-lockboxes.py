#!/usr/bin/python3
"""
Solution to lockboxes problem
"""


def canUnlockAll(boxes):
    """
    Determines whether a series of locked boxes can be opened
    based on keys that can be attained.
    Solution to the lockboxes problem
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for z in range(1, len(boxes) - 1):
        boxes_checked = False
        for index1 in range(len(boxes)):
            boxes_checked = z in boxes[index1] and z != index1
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True