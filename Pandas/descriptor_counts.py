count_tropical = 0
count_fruity = 0

for i in reviews.description:
    if 'tropical' in i:
        count_tropical += 1

for i in reviews.description:
    if 'fruity' in i:
        count_fruity +=1

new_series = pd.Series([count_tropical,count_fruity], index = ['tropical','fruity'])

descriptor_counts = new_series

# Check your answer
q6.check()
