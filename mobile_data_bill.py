# TODO: Edit the function to return the correct bill for different
# values of GB
def get_phone_bill(gb):
    if gb<=15:
        return 100
    else:
        cost= 100 + (gb-15)*100
        return cost

# Check your answer
q4.check()
