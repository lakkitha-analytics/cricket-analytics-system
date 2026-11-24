import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cricket dataset
df = pd.read_csv("data/batting.csv")

# Calculate dismissals
df["Dismissals"] = df["Innings"] - df["NotOuts"]

# Calculate batting average
df["Batting_Average"] = (
    df["Runs"] / df["Dismissals"].replace(0, float("nan"))
).round(2)

# Calculate strike rate
df["Strike_Rate"] = (
    df["Runs"] / df["Balls"].replace(0, float("nan")) * 100
).round(2)

# Display batting data
print("\nCRICKET BATTING DATA")
print(df.to_string(index=False))

print("\nBATSMAN PERFORMANCE ANALYSIS")

print(
    df[["Player", "Runs", "Batting_Average", "Strike_Rate"]]
    .to_string(index=False)
)

# Highest run scorer
top_scorer = df.loc[df["Runs"].idxmax()]

print("\nHighest Run Scorer:", top_scorer["Player"])
print("Total Runs:", top_scorer["Runs"])

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Chart 1 - Top Run Scorers
plt.figure(figsize=(10, 5))
plt.bar(df["Player"], df["Runs"])
plt.title("Top Run Scorers")
plt.xlabel("Players")
plt.ylabel("Total Runs")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/top_run_scorers.png")
plt.show()
plt.close()

# Chart 2 - Batting Average
plt.figure(figsize=(10, 5))
plt.bar(df["Player"], df["Batting_Average"])
plt.title("Batting Average Comparison")
plt.xlabel("Players")
plt.ylabel("Batting Average")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/batting_average.png")
plt.show()
plt.close()

# Chart 3 - Strike Rate
plt.figure(figsize=(10, 5))
plt.bar(df["Player"], df["Strike_Rate"])
plt.title("Strike Rate Comparison")
plt.xlabel("Players")
plt.ylabel("Strike Rate")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/strike_rate.png")
plt.show()
plt.close()

print("\nCricket Analytics Completed Successfully!")
print("Charts saved in the charts folder.")