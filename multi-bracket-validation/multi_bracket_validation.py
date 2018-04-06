def multi_bracket_validation(user_input):
    """
    Validates if brackets have a matching pair
    """
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    brackets = {opening[0]: closing[0],
                    opening[1]: closing[1],
                    opening[2]: closing[2]}
    arr = []

    for item in user_input:
        if item in opening:
            arr.append(brackets[item])
        elif item in closing:
            if not arr or item != arr.pop():
                return False
    return not arr


"""
Recursion example code from Adam
"""
# MAP = dict(zip('[({', '])}'))


# def recursion(it, opener=None):
#     for c in it:
#         if c in MAP.keys():
#             if not recursion(it, c):
#                 return False
#         if opener is not None and MAP[opener] == c:
#             return True
#         if c in MAP.values():
#             return False
#     return True if opener is None else False


# def multi_bracket_validation(input):
#     """
#     Test input string for matching brackets.

#     Valid input look as follows:
#     - `[[[[]]]]`
#     - `[][]{}`
#     - `{()}({})`

#     Invalid inputs could be as follows:
#     - `(()}`
#     - `}}`
#     - `][`
#     """
#     return recursion(iter(input))
