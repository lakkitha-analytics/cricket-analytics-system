import pandas as pd
import matplotlib.pyplot as plt

print("Pandas Version:", pd.__version__)
print("Matplotlib Installed Successfully!")

print("Cricket Analytics Project Started!")


import pandas as pd
import matplotlib.pyplot as plt

# Load cricket dataset
df = pd.read_csv("data/batting.csv")

# Display dataset
print("\nCRICKET BATTING DATA")
print(df.to_string(index=False))

print("\nTotal Players:", len(df))
print("Total Runs:", df["Runs"].sum())


import pandas as pd
import matplotlib.pyplot as plt

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

# Display batting analysis
print("\nBATSMAN PERFORMANCE ANALYSIS")

print(
    df[["Player", "Runs", "Batting_Average", "Strike_Rate"]]
    .to_string(index=False)
)

# Highest run scorer
top_scorer = df.loc[df["Runs"].idxmax()]

print("\nHighest Run Scorer:", top_scorer["Player"])
print("Total Runs:", top_scorer["Runs"])