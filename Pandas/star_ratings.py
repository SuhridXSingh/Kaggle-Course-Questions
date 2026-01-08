def get_stars(row):
    if row.country == 'canada':
        return 3

    if row.points >= 95 :
        return 3

    elif row.points >= 85:
        return 2

    else:
        return 1


star_ratings = reviews.apply(get_stars, axis = 'columns')

# Check your answer
q7.check()
