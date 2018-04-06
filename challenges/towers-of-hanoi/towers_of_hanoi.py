
def towers_of_hanoi(n):
    """
    Main function adds tower to source
    """
    source = []
    helper = []
    target = []
    for i in reversed(range(1, n + 1)):
        source.append(i)
    count = recursion(n, source, target, helper)
    return (count, target, helper, source)


def recursion(n, source, target, helper):
    """
    Helper function for recursion
    """
    count = 0
    if n >= 1:
        first = recursion(n - 1, source, helper, target)
        target.append(source.pop())
        count += 1
        second = recursion(n - 1, helper, target, source)
        count += first + second
    return count
