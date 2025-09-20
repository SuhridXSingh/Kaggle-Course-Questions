# TODO: Edit the function to return the correct bill for different
# values of num_gallons
def get_water_bill(num_gallons):
    if 0<num_gallons<=8000:
        return num_gallons*0.005
    elif 8000<num_gallons<=22000:
        return num_gallons*0.006
    elif 22000<num_gallons<=30000:
        return num_gallons*0.007
    else:
        return num_gallons*0.01

# Check your answer
q3.check()
