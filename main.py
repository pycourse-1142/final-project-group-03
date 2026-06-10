import pandas as pd
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

# 1. 讀取資料（內部包含品質控制判斷）
df = load_data("data/即時值查詢.csv")

if df is not None:
    # 轉換日期格式
    df["日期"] = pd.to_datetime(df["日期"])

    # 2. 計算與繪製每日平均
    df = calculate_daily_average(df)
    print("\n--- 每日平均資料 (前五行) ---")
    print(df[["日期", "daily_avg"]].head())
    print("正在繪製：每日趨勢圖...")
    plot_daily_pm25(df)

    # 3. 計算與繪製月平均
    monthly_avg = calculate_monthly_average(df)
    print("\n--- 月平均資料 ---")
    print(monthly_avg)
    print("正在繪製：月平均圖...")
    plot_monthly_pm25(monthly_avg)

    # 4. 計算與繪製季平均
    season_avg = calculate_season_average(df)
    print("\n--- 季平均資料 ---")
    print(season_avg)
    print("正在繪製：季平均圖...")
    plot_season_pm25(season_avg)

    # 5. 計算與繪製超標天數
    exceed_days = calculate_exceed_days(df)
    print("\n--- 超標天數統計 ---")
    print(f"總超標天數：{exceed_days} 天")
    print("正在繪製：超標天數圖...")
    plot_exceed_days(exceed_days)
    
 
    print("\n======================= 📊 花蓮 PM2.5 純數據分析報告 =======================")
    total_days = len(df)
    exceed_rate = (exceed_days / total_days) * 100
    avg_all = df["daily_avg"].mean()
    
    print(f"【總體監測指標】")
    print(f" * 數據觀測總天數：{total_days} 天")
    print(f" * 全期總平均濃度：{avg_all:.2f} µg/m³")
    print(f" * 符合法規安全天數：{total_days - exceed_days} 天")
    print(f" * 法規達標率：{100 - exceed_rate:.2f} %")
    print(f" * 總超標天數：{exceed_days} 天")
    print(f" * 全期超標率：{exceed_rate:.2f} %")
    
    print(f"\n【月平均濃度統計】")
    for m in monthly_avg.sort_values(ascending=False).index:
        print(f" * {m:02d} 月平均值：{monthly_avg.loc[m]:.2f} µg/m³")
        
    print(f"\n【季節平均濃度統計 (台灣氣候劃分)】")
    # 將 Pandas Series 轉為標準 Python 字典，徹底避開索引位置判斷的警告地雷
    # 將 Pandas Series 轉為標準 Python 字典，並強制把型別洗成純數字
    season_dict = {int(k): v for k, v in season_avg.items()}
    print(f" * 春季 (02-04月) 平均值：{season_dict.get(1, 0):.2f} µg/m³")
    print(f" * 夏季 (05-07月) 平均值：{season_dict.get(2, 0):.2f} µg/m³")
    print(f" * 秋季 (08-10月) 平均值：{season_dict.get(3, 0):.2f} µg/m³")
    print(f" * 冬季 (11-01月) 平均值：{season_dict.get(4, 0):.2f} µg/m³")
    print("============================================================================")
    
    print("\n🎉 數據處理與圖表繪製已全部完成。")