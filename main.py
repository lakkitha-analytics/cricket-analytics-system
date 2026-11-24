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

# BOWLING PERFORMANCE ANALYSIS

bowl = pd.read_csv("data/bowling.csv")

# Calculate Bowling Average
bowl["Bowling_Average"] = (
    bowl["Runs_Conceded"] / bowl["Wickets"]
).round(2)

# Calculate Economy Rate
bowl["Economy_Rate"] = (
    bowl["Runs_Conceded"] / bowl["Overs"]
).round(2)

# Calculate Bowling Strike Rate
bowl["Bowling_Strike_Rate"] = (
    bowl["Balls"] / bowl["Wickets"]
).round(2)

# Display bowling analysis
print("\nBOWLING PERFORMANCE ANALYSIS")

print(
    bowl[[
        "Player",
        "Wickets",
        "Bowling_Average",
        "Economy_Rate",
        "Bowling_Strike_Rate"
    ]].to_string(index=False)
)

# Best bowler
best_bowler = bowl.loc[bowl["Wickets"].idxmax()]

print("\nBest Bowler:", best_bowler["Player"])
print("Total Wickets:", best_bowler["Wickets"])

# Total wickets
print("Total Wickets by All Bowlers:", bowl["Wickets"].sum())

# BOWLING PERFORMANCE VISUALIZATION

# Chart 1 - Total Wickets
plt.figure(figsize=(10, 5))
plt.bar(bowl["Player"], bowl["Wickets"])
plt.title("Total Wickets by Bowlers")
plt.xlabel("Players")
plt.ylabel("Wickets")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/total_wickets.png")
plt.show()
plt.close()


# Chart 2 - Bowling Average
plt.figure(figsize=(10, 5))
plt.bar(bowl["Player"], bowl["Bowling_Average"])
plt.title("Bowling Average Comparison")
plt.xlabel("Players")
plt.ylabel("Bowling Average")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/bowling_average.png")
plt.show()
plt.close()


# Chart 3 - Economy Rate
plt.figure(figsize=(10, 5))
plt.bar(bowl["Player"], bowl["Economy_Rate"])
plt.title("Bowling Economy Rate Comparison")
plt.xlabel("Players")
plt.ylabel("Economy Rate")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig("charts/economy_rate.png")
plt.show()
plt.close()

print("\nBowling Charts Created Successfully!")