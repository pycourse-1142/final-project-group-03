import pandas as pd

# 每日平均
def calculate_daily_average(df):

    hour_columns = [f"{i:02d}" for i in range(24)]

    df[hour_columns] = df[hour_columns].apply(
        pd.to_numeric,
        errors='coerce'
    )

    df["daily_avg"] = df[hour_columns].mean(axis=1)

    return df


# 月平均
def calculate_monthly_average(df):

    df["日期"] = pd.to_datetime(df["日期"])
    df["month"] = df["日期"].dt.month

    monthly_avg = df.groupby("month")["daily_avg"].mean()

    return monthly_avg


# 季平均
def calculate_season_average(df):

    df["season"] = (df["month"] % 12 + 3) // 3

    season_avg = df.groupby("season")["daily_avg"].mean()

    return season_avg


# 超標天數（PM2.5 > 15）
def calculate_exceed_days(df):

    df["exceed"] = df["daily_avg"] > 15

    exceed_count = df["exceed"].sum()

    return exceed_count