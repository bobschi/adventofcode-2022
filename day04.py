def do_assigments_fully_overlap(assignment_a: set[int], assignment_b: set[int]) -> bool:
    """
    Return True if one assigment is fully contained in the other, False if not.
    """
    return assignment_a <= assignment_b or assignment_b <= assignment_a
