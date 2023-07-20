import csv
import pandas as pd



file = open('merged-1213.csv')

df = pd.read_csv('merged-1213.csv')

csvreader = csv.DictReader(file)

all_teams_list = []

df["HomeWinRate"] = float("nan")
df["AwayWinRate"] = float("nan")



for row in csvreader:
    all_teams_list.append(row['HomeTeam'])
    all_teams_list.append(row['AwayTeam'])

all_teams_list = list(set(all_teams_list))
all_teams_list.sort()

print(all_teams_list)

labels = [
    ("FTHG", "FTAG"),
    ("HTHG", "HTAG"),
    ("HS", "AS"),
    ("HST", "AST"),
    ("HF", "AF"),
    ("HC", "AC"),
    ("HY", "AY"),
    ("HR", "AR"),
]

for team in all_teams_list:
    a = df[(df['HomeTeam'] == team) | (df['AwayTeam'] == team)]
    count = 0
    perf = {
        "Wins": 0,
        "FTHG": 0,
        "HTHG": 0,
        "HS": 0,
        "HST": 0,
        "HF": 0,
        "HC": 0,
        "HY": 0,
        "HR": 0,
    }
    print("team: " + str(team))
    for i, row in a.iterrows():
        if row['HomeTeam'] == team:
            for l in labels:
                df.loc[i,l[0]] = (float("nan") if count == 0 else perf[l[0]] / count)
                perf[l[0]] += row[l[0]]
            df.loc[i,"HomeWinRate"] = (float("nan") if count == 0 else perf["Wins"] / count)
            if row["FTR"] == "H":
                perf["Wins"] += 1
            
        elif row["AwayTeam"] == team:
            for l in labels:
                df.loc[i,l[1]] =  (float("nan") if count == 0 else perf[l[0]] / count)
                perf[l[0]] += row[l[1]]
            df.loc[i,"AwayWinRate"] = (float("nan") if count == 0 else perf["Wins"] / count)
            if row["FTR"] == "A":
                perf["Wins"] += 1
        else:
            raise Exception("away team or home team not found")
        count += 1
#remove rows where average is NAN (we dont have historical data yet)
df = df[df['FTHG'].notna() & df['FTAG'].notna()]

print(df)
df.to_csv("merged-1213-historical.csv")
