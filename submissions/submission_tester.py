import pandas as pd

def get_recommendations(df: pd.DataFrame, brand_name: str):
    """
    Test submission logic: 
    Finds medicines with the same ingredients but lower price.
    """
    # 1. Get details of the searched brand
    original_med = df[df['brand_name'].str.lower() == brand_name.lower()]
    
    if original_med.empty:
        return None
    
    # Get the key characteristics
    ingredient = original_med.iloc[0]['primary_ingredient']
    strength = original_med.iloc[0]['primary_strength']
    original_price = original_med.iloc[0]['price_inr']
    
    # 2. Find alternatives (Same ingredient & strength, but cheaper)
    alternatives = df[
        (df['primary_ingredient'] == ingredient) & 
        (df['primary_strength'] == strength) & 
        (df['price_inr'] < original_price) &
        (df['brand_name'].str.lower() != brand_name.lower())
    ]
    
    # 3. Sort by price (Cheapest first)
    return alternatives.sort_values(by='price_inr').head(5)