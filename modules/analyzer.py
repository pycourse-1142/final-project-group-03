import pandas as pd

# 每日平均：計算各日期 24 小時的 PM2.5 平均值
def calculate_daily_average(df):
    # 建立 00-23 時的欄位名稱列表
    hour_columns = [f"{i:02d}" for i in range(24)]

    # 確保所有小時資料為數值格式，非數值者轉為 NaN
    df[hour_columns] = df[hour_columns].apply(
        pd.to_numeric,
        errors='coerce'
    )

    # 沿著水平方向 (axis=1) 計算 24 小時的平均值，並存入新欄位
    df["daily_avg"] = df[hour_columns].mean(axis=1)

    return df


# 月平均：將資料依月份分組並計算平均值
def calculate_monthly_average(df):
    # 將日期欄位轉換為 datetime 物件，方便提取月份資訊
    df["日期"] = pd.to_datetime(df["日期"])
    df["month"] = df["日期"].dt.month

    # 依據月份進行分組，並計算 daily_avg 的平均值
    monthly_avg = df.groupby("month")["daily_avg"].mean()

    return monthly_avg


# 季平均：根據台灣氣候特性定義季節並計算平均值
def calculate_season_average(df):
    # 定義季節映射規則：1:春季, 2:夏季, 3:秋季, 4:冬季
    season_map = {
        2: 1, 3: 1, 4: 1,     # 2~4月為春季
        5: 2, 6: 2, 7: 2,     # 5~7月為夏季
        8: 3, 9: 3, 10: 3,    # 8~10月為秋季
        11: 4, 12: 4, 1: 4    # 11~1月為冬季
    }
    
    # 建立季節欄位並依據 month 映射
    df["season"] = df["month"].map(season_map)
    
    # 依據季節分組計算平均值
    season_avg = df.groupby("season")["daily_avg"].mean()
    return season_avg


# 超標天數：計算 PM2.5 日平均值超過 15 µg/m³ 的天數
def calculate_exceed_days(df):
    # 建立布林值欄位，判斷是否超過 15
    df["exceed"] = df["daily_avg"] > 15

    # 將 True (符合條件) 的數量加總，即為超標天數
    exceed_count = df["exceed"].sum()

    return exceed_count