top_oceania_wines = reviews.loc[((reviews.country == "Australia") | (reviews.country == "New Zealand")) & (reviews.points >= 95)]

# Check your answer
q9.check()
top_oceania_wines
