def flatten_list(nested_list):
    """
    Flattens a nested list into a single list of integers.

    Args:
        nested_list: the input nested list

    Returns:
        a flat list containing all integers from the nested structure
    """
    # hint: isinstance()

    # i solved this one as in sum_of_digits question , same idea but using python trick str(list)
    # Not perfect complexity!
    wanted = []
    list_as_str = str(nested_list)
    for object in list_as_str :
        if ord(object)>=48 and ord(object)<=57:wanted.append(ord(object)-48)
    return wanted







    
    return 


if __name__ == '__main__':
    nested_list = [
        1,
        [2, 3],
        [4, [5, 6]],
        7
    ]

    flat_list = flatten_list(nested_list)

    print(f"Flattened list: {flat_list}")  # Should be [1, 2, 3, 4, 5, 6, 7]