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


# 季平均 (依台灣氣候實務：2-4春, 5-7夏, 8-10秋, 11-1冬)
def calculate_season_average(df):
    season_map = {
        2: 1, 3: 1, 4: 1,     # 2~4月為春季 (代號1)
        5: 2, 6: 2, 7: 2,     # 5~7月為夏季 (代號2)
        8: 3, 9: 3, 10: 3,    # 8~10月為秋季 (代號3)
        11: 4, 12: 4, 1: 4    # 11~1月為冬季 (代號4)
    }
    df["season"] = df["month"].map(season_map)
    season_avg = df.groupby("season")["daily_avg"].mean()
    return season_avg


# 超標天數（PM2.5 > 15）
def calculate_exceed_days(df):

    df["exceed"] = df["daily_avg"] > 15

    exceed_count = df["exceed"].sum()

    return exceed_count