new_df = pd.DataFrame({
    'title': reviews.title,
    'quality_price_ratio': reviews.points / reviews.price
})
sorted_df = new_df.sort_values(by='quality_price_ratio', ascending = False)
bargain_wine = sorted_df.title.iloc[0]

# Check your answer
q5.check()
