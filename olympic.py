import numpy as np
countries = ["Country A", "Country B", "Country C", "Country D", "Country E"]
games = ["2012", "2016", "2020", "2024"]
medals = np.array([
    [8, 8, 10, 14],
    [6, 9, 12, 15],
    [7, 7, 11, 13],
    [5, 8, 9, 12],
    [4, 6, 10, 11]
])
 
print("--- Olympic Medal Data Matrix ---")
print(medals)
print("\n" + "="*40 + "\n")
total_per_country = np.sum(medals, axis=1)
 
avg_per_country = np.mean(medals, axis=1)
 
print("--- Country Statistics ---")
for i, country in enumerate(countries):
    print(f"{country} -> Total Gold: {total_per_country[i]}, Average/Game: {avg_per_country[i]:.2f}")
print("\n" + "="*40 + "\n")
 
# ---------------------------------------------------------
# 3. Rank Countries
# ---------------------------------------------------------
# Sort in descending order based on total medals
# argsort returns indices that would sort an array; [::-1] reverses it for descending order
rankings = np.argsort(total_per_country)[::-1]
 
print("--- Country Rankings (By Total Gold) ---")
for rank, idx in enumerate(rankings, 1):
    print(f"Rank {rank}: {countries[idx]} with {total_per_country[idx]} total gold medals")
print("\n" + "="*40 + "\n")
 
# ---------------------------------------------------------
# 4. Analyse Growth Rates
# ---------------------------------------------------------
# Calculate the change from the first game (2012) to the last game (2024)
growth_rate = ((medals[:, -1] - medals[:, 0]) / medals[:, 0]) * 100
 
print("--- Performance Growth Rate (2012 to 2024) ---")
for i, country in enumerate(countries):
    print(f"{country}: {growth_rate[i]:+.2f}% change in gold medals")
print("\n" + "="*40 + "\n")
 
# ---------------------------------------------------------
# 5. Predict Next Games Using Weighted Average
# ---------------------------------------------------------
# Define weights that prioritize recent performance (must sum up to 1)
# 2012: 10%, 2016: 20%, 2020: 30%, 2024: 40%
weights = np.array([0.1, 0.2, 0.3, 0.4])
 
# Compute the weighted average for each country
# np.average allows specifying weights along an axis
predicted_medals = np.average(medals, axis=1, weights=weights)
 
print("--- Predicted Gold Medals for the Next Games ---")
for i, country in enumerate(countries):
    # Rounded to the nearest whole medal for realistic predictions
    print(f"{country}: Predicted ~{round(predicted_medals[i])} Gold Medals (Exact: {predicted_medals[i]:.2f})")