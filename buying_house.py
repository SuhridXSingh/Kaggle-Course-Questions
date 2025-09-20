# TODO: Complete the function
def get_expected_cost(beds, baths, has_basement):
    if has_basement == True:
        value= 80000 +(30000*beds)+(10000*baths)+40000
        return value
    else:
        value= 80000 +(30000*beds)+(10000*baths)
        return value

# Check your answer 
q3.check()
