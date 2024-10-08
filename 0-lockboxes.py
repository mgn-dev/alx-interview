def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track whether each box can be unlocked
    unlocked[0] = True  # The first box is unlocked
    keys = boxes[0]  # Start with keys from the first box

    # Use a stack to keep track of boxes to explore
    stack = keys.copy()

    while stack:
        key = stack.pop()
        # If the key corresponds to a valid box and it is not already unlocked
        if key < n and not unlocked[key]:
            unlocked[key] = True  # Unlock the box
            # Add the keys found in this box to the stack
            stack.extend(boxes[key])

    # Check if all boxes are unlocked
    return all(unlocked)


# Example usage:
boxes_example = [[1], [2], [3], []]
print(canUnlockAll(boxes_example))  # Output: True
