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

