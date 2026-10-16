import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

data = {

"Instagram": [12400, 15300, 13800, 16200, 18900, 24100, 21500],

"YouTube": [8900, 9200, 11400, 10800, 13200, 17600, 16100],

"Twitter": [6700, 7800, 6900, 8400, 9100, 7200, 6500],

"TikTok": [19200, 21400, 18700, 22800, 27300, 31500, 28900]

}

# Display totals

print("WEEKLY SOCIAL MEDIA REPORT")

for name, posts in data.items():
    print(name, "Total:", sum(posts))
fig, ax = plt.subplots(2, 2, figsize=(12, 8))

fig.suptitle("Social Media Trends Dashboard")

# 1. Daily trends

for name, posts in data.items():
    ax[0, 0].plot(days, posts, marker="o", label=name)

ax[0, 0].set_title("Daily Trends")

ax[0, 0].legend(fontsize=8)

# 2. Weekly totals

ax[0, 1].bar(data.keys(), [sum(v) for v in data.values()])

ax[0, 1].set_title("Weekly Totals")

# 3. Weekday vs weekend averages

names = list(data.keys())

weekday = [sum(v[:5]) / 5 for v in data.values()]

weekend = [sum(v[5:]) / 2 for v in data.values()]

x = range(len(names))

ax[1, 0].bar(x, weekday, width=0.4, label="Weekday")

ax[1, 0].bar([i + 0.4 for i in x], weekend, width=0.4, label="Weekend")

ax[1, 0].set_xticks([i + 0.2 for i in x])

ax[1, 0].set_xticklabels(names)

ax[1, 0].set_title("Weekday vs Weekend")

ax[1, 0].legend()

# 4. TikTok vs Instagram

ax[1, 1].fill_between(days, data["TikTok"], alpha=0.4, label="TikTok")

ax[1, 1].fill_between(days, data["Instagram"], alpha=0.4, label="Instagram")

ax[1, 1].set_title("TikTok vs Instagram")

ax[1, 1].legend()

plt.tight_layout()

plt.savefig("social_media_dashboard.png")

plt.show()

# Key insights

totals = {name: sum(v) for name, v in data.items()}

print("\nTop Platform:", max(totals, key=totals.get))

print("TikTok Peak Day:", days[data["TikTok"].index(max(data["TikTok"]))])

print("Least Active:", min(totals, key=totals.get))