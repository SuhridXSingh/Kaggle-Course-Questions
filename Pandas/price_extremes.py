price_extremes = reviews.groupby('variety').price.agg([min,max])
