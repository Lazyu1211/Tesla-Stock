import pandas as pd

PATH = "/Users/junyuwu/Tesla_stock/components/TSLA.csv"
df = pd.read_csv(PATH)

def get_data():
    df["diff_close_adj"] = abs(df["Close"] - df["Adj Close"])
    df["range_high_low"] = round(df["High"] - df["Low"],2)
    df["change_open_close"] = round(df["Open"] - df["Close"],2)
    return df

def get_dropdown_list():
    df["year"] = df["Date"].str.split("-")
    df["year"] = df["year"].str.get(0)
    by_year_volume = df.groupby("year")["Volume"].sum()
    year_list = list(by_year_volume.index.tolist())
    return year_list

def get_year_volume():
    df["year"] = df["Date"].str.split("-")
    df["year"] = df["year"].str.get(0)
    by_year_volume = df.groupby("year")["Volume"].sum().to_frame()
    by_year_volume.reset_index(inplace=True)
    return by_year_volume

def get_year_change():
    df["diff_close_adj"] = abs(df["Close"] - df["Adj Close"])
    df["range_high_low"] = round(df["High"] - df["Low"],2)
    df["change_open_close"] = round(df["Open"] - df["Close"],2)
    by_year_change = df.groupby("year")["change_open_close"].sum().to_frame()
    by_year_change.reset_index(inplace=True)
    return by_year_change

def get_year_range():
    df["diff_close_adj"] = abs(df["Close"] - df["Adj Close"])
    df["range_high_low"] = round(df["High"] - df["Low"],2)
    df["change_open_close"] = round(df["Open"] - df["Close"],2)
    by_year_range = df.groupby("year")["range_high_low"].sum().to_frame()
    by_year_range.reset_index(inplace=True)
    return by_year_range

def get_adj_close():
    df["year"] = df["Date"].str.split("-")
    df["year"] = df["year"].str.get(0)
    by_adj = df.groupby("year")["Adj Close"].sum().to_frame()
    by_adj.reset_index(inplace=True)
    return by_adj

