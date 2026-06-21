import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/comments.csv")

# Parse datetime
df['date'] = pd.to_datetime(df['date'])
df['hour'] = df['date'].dt.hour
df['day'] = df['date'].dt.day_name()

# Engagement metrics (example: comments per follower if column exists)
if 'followers' in df.columns:
    df['comments_per_follower'] = df['comments'] / df['followers']

# Analyze posting times
engagement_by_hour = df.groupby('hour').size()
engagement_by_day = df.groupby('day').size()

# Save plots
plt.figure(figsize=(8,5))
engagement_by_hour.plot(kind='bar', color='skyblue')
plt.title("Engagement by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Comments")
plt.savefig("../plots/engagement_by_time.png")
plt.close()

plt.figure(figsize=(8,5))
engagement_by_day.plot(kind='bar', color='green')
plt.title("Engagement by Day of Week")
plt.xlabel("Day")
plt.ylabel("Number of Comments")
plt.savefig("../plots/engagement_by_day.png")
plt.close()

print("✅ Analysis complete. Plots saved in /plots folder.")
