# Working with the Twitter dataset of offensive and non-offensive tweets

import pandas as pd

# Offensive column is a scale of offensiveness from 0 (not offensive) to 9 (very offensive)
# I'm going to work with just values 1000 of 0 and values of 6-9 (993 strings) to get us a baseline
df = pd.read_csv("../docs/test_dataset.csv")
sample_dfHIGH = df[-100:]
# sample_df6 = df[23792:24156]
sample_dfLOW = df[:100]
sample_df = pd.concat([sample_dfLOW, sample_dfHIGH])

# Data Frame with the Tweets and True Labels
metrics_df = pd.DataFrame()
metrics_df["tweet"] = sample_df["tweet"]
metrics_df["offensive_language"] = sample_df["offensive_language"]
metrics_df["offensive_language"] = metrics_df['offensive_language'].replace(
    {0: 'False', 6: 'True', 7: 'True', 8: 'True', 9: 'True'})
metrics_df = metrics_df.rename(columns={"offensive_language": "Predicted Labels"})

# Running the ML Call
import time
mlstart_time = time.time()
ml = []
from algos.ML_call import *

# Need to only use 3 per minute

count = 0
for tweet in metrics_df["tweet"]:
    if count % 2 == 0 and count!=0:
        print("Sleeping")
        time.sleep(61)
    ret = ml_moderation(tweet)
    if isinstance(ret, bool):
        ml.append("False")
    elif isinstance(ret, tuple):
        ml.append("True")
    count += 1
    print(count)
metrics_df["ML Call"] = ml

ml_accuracy = []
for index, row in metrics_df.iterrows():
    if row["ML Call"] == "True" and row["Predicted Labels"] == "True":
        ml_accuracy.append("True Positive")
    elif row["ML Call"] == "True" and row["Predicted Labels"] == "False":
        ml_accuracy.append("False Positive")
    elif row["ML Call"] == "False" and row["Predicted Labels"] == "False":
        ml_accuracy.append("True Negative")
    else:
        ml_accuracy.append("False Negative")
metrics_df["ML Call Accuracy"] = ml_accuracy
print(metrics_df["ML Call Accuracy"].value_counts())
print(time.time() - mlstart_time)

# Running Basic Hashing
from algos.hashing import *
bhtime = time.time()
basic_hashing = []
for tweet in metrics_df["tweet"]:
    ret = hashing_algo("b", tweet)
    if isinstance(ret, bool):
        basic_hashing.append("False")
    elif isinstance(ret, tuple):
        basic_hashing.append("True")
metrics_df["Basic Hashing"] = basic_hashing

bh_accuracy = []
for index, row in metrics_df.iterrows():
    if row["Basic Hashing"] == "True" and row["Predicted Labels"] == "True":
        bh_accuracy.append("True Positive")
    elif row["Basic Hashing"] == "True" and row["Predicted Labels"] == "False":
        bh_accuracy.append("False Positive")
    elif row["Basic Hashing"] == "False" and row["Predicted Labels"] == "False":
        bh_accuracy.append("True Negative")
    else:
        bh_accuracy.append("False Negative")
metrics_df["Basic Hashing Accuracy"] = bh_accuracy
print(metrics_df["Basic Hashing Accuracy"].value_counts())
print(time.time() - bhtime)

# Running Levenshtein
levenshtein = []
levenshteintime = time.time()
for tweet in metrics_df["tweet"]:
    ret = hashing_algo("l", tweet)
    if isinstance(ret, bool):
        levenshtein.append("False")
    elif isinstance(ret, tuple):
        levenshtein.append("True")
metrics_df["Levenshtein"] = levenshtein

levenshtein_accuracy = []
for index, row in metrics_df.iterrows():
    if row["Levenshtein"] == "True" and row["Predicted Labels"] == "True":
        levenshtein_accuracy.append("True Positive")
    elif row["Levenshtein"] == "True" and row["Predicted Labels"] == "False":
        levenshtein_accuracy.append("False Positive")
    elif row["Levenshtein"] == "False" and row["Predicted Labels"] == "False":
        levenshtein_accuracy.append("True Negative")
    else:
        levenshtein_accuracy.append("False Negative")
metrics_df["Levenshtein Accuracy"] = levenshtein_accuracy
print(metrics_df["Levenshtein Accuracy"].value_counts())
print(time.time() - levenshteintime)

# Running Soundex
soundex = []
soundextime = time.time()
for tweet in metrics_df["tweet"]:
    ret = hashing_algo("s", tweet)
    if isinstance(ret, bool):
        soundex.append("False")
    elif isinstance(ret, tuple):
        soundex.append("True")
metrics_df["Soundex"] = soundex

soundex_accuracy = []
for index, row in metrics_df.iterrows():
    if row["Soundex"] == "True" and row["Predicted Labels"] == "True":
        soundex_accuracy.append("True Positive")
    elif row["Soundex"] == "True" and row["Predicted Labels"] == "False":
        soundex_accuracy.append("False Positive")
    elif row["Soundex"] == "False" and row["Predicted Labels"] == "False":
        soundex_accuracy.append("True Negative")
    else:
        soundex_accuracy.append("False Negative")
metrics_df["Soundex Accuracy"] = soundex_accuracy
print(metrics_df["Soundex Accuracy"].value_counts())
print(time.time() - soundextime)

# Running Soundex and Levenshtein
SL = []
sltime = time.time()
for tweet in metrics_df["tweet"]:
    ret = hashing_algo("sl", tweet)
    if isinstance(ret, bool):
        SL.append("False")
    elif isinstance(ret, tuple):
        SL.append("True")
metrics_df["Soundex and Levenshtein"] = SL

SL_accuracy = []
for index, row in metrics_df.iterrows():
    if row["Soundex and Levenshtein"] == "True" and row["Predicted Labels"] == "True":
        SL_accuracy.append("True Positive")
    elif row["Soundex and Levenshtein"] == "True" and row["Predicted Labels"] == "False":
        SL_accuracy.append("False Positive")
    elif row["Soundex and Levenshtein"] == "False" and row["Predicted Labels"] == "False":
        SL_accuracy.append("True Negative")
    else:
        SL_accuracy.append("False Negative")
metrics_df["Soundex and Levenshtein Accuracy"] = SL_accuracy
print(metrics_df["Soundex and Levenshtein Accuracy"].value_counts())
print(time.time() - sltime)

# Running All Methods
all = []
alltime = time.time()
for tweet in metrics_df["tweet"]:
    ret = hashing_algo("a", tweet)
    if isinstance(ret, bool):
        all.append("False")
    elif isinstance(ret, tuple):
        all.append("True")
metrics_df["All"] = all

all_accuracy = []
for index, row in metrics_df.iterrows():
    if row["All"] == "True" and row["Predicted Labels"] == "True":
        all_accuracy.append("True Positive")
    elif row["All"] == "True" and row["Predicted Labels"] == "False":
        all_accuracy.append("False Positive")
    elif row["All"] == "False" and row["Predicted Labels"] == "False":
        all_accuracy.append("True Negative")
    else:
        all_accuracy.append("False Negative")
metrics_df["All Methods Accuracy"] = all_accuracy
print(metrics_df["All Methods Accuracy"].value_counts())
print(time.time() - alltime)

metrics_df.to_csv('out.csv')
