from modules.parser import load_data
from modules.analyzer import (
    calculate_daily_average,
    calculate_monthly_average,
    calculate_season_average,
    calculate_exceed_days
)
from modules.plotter import (
    plot_daily_pm25,
    plot_monthly_pm25,
    plot_season_pm25,
    plot_exceed_days
)

# 1. 讀資料
df = load_data("data/即時值查詢.csv")

if df is not None:

    # 2. 每日平均
    df = calculate_daily_average(df)

    print(df[["日期", "daily_avg"]].head())

    plot_daily_pm25(df)

    # 3. 月平均
    monthly_avg = calculate_monthly_average(df)
    print(monthly_avg)
    plot_monthly_pm25(monthly_avg)

    # 4. 季平均
    season_avg = calculate_season_average(df)
    print(season_avg)
    plot_season_pm25(season_avg)

    # 5. 超標天數
    exceed_days = calculate_exceed_days(df)
    print("超標天數：", exceed_days)
    plot_exceed_days(exceed_days)