def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # To keep track of unlocked boxes
    unlocked[0] = True  # Box 0 is initially unlocked
    keys = boxes[0]  # Keys from box 0
    stack = [0]  # Start with box 0 in the stack
    
    # Go through the boxes to unlock them using DFS-like approach
    while stack:
        current_box = stack.pop()  # Take the last opened box
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:  # If key is valid and the box is locked
                unlocked[key] = True  # Unlock the box
                stack.append(key)  # Add this box to stack for further exploration
    
    # If all boxes are unlocked, all entries in unlocked should be True
    return all(unlocked)

