best_rating_per_price = reviews.groupby("price").points.max()

# Check your answer
q2.check()
