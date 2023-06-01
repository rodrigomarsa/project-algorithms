def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    counter = 0
    for initial, end in permanence_period:
        if not isinstance(initial, int) or not isinstance(end, int):
            return None
        elif target_time in range(initial, end + 1):
            counter += 1
    return counter
