def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    
    if round(len(arrivals)/2) < (arrivals.index(name) +1) and arrivals.index(name) != (len(arrivals)-1):
        return True
    else:
        return False
        

# Check your answer
q5.check()
