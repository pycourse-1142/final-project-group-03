import matplotlib.pyplot as plt
import os

# 設定中文字型（防止圖表出現方塊豆腐字）
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # 微軟正黑體
plt.rcParams['axes.unicode_minus'] = False  # 正常顯示負號

# 建立結果資料夾
os.makedirs("results", exist_ok=True)


# 1. 每日趨勢圖
def plot_daily_pm25(df):
    plt.figure(figsize=(10, 5))
    
    # 確保移除日期或數據有空值的狀況
    clean_df = df.dropna(subset=["日期", "daily_avg"])
    plt.plot(clean_df["日期"], clean_df["daily_avg"])

    plt.title("每日 PM2.5 趨勢圖")
    plt.xlabel("日期")
    plt.ylabel("PM2.5 平均值")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("results/chart1_daily.png")
    plt.close()


# 2. 月平均圖
def plot_monthly_pm25(monthly_avg):
    plt.figure(figsize=(8, 5))
    monthly_avg.plot(kind="bar", color="skyblue")

    plt.title("月份 PM2.5 平均值")
    plt.xlabel("月份")
    plt.ylabel("PM2.5 平均值")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig("results/chart2_monthly.png")
    plt.close()

# 3. 季平均圖
def plot_season_pm25(season_avg):
    plt.figure(figsize=(6, 5))
    
    # 【關鍵修復】：複製一份資料來畫圖，絕對不要改到外面的原始資料！
    plot_data = season_avg.copy()
    
    # 這裡的文字順便配合台灣氣候劃分修正
    season_labels = {1: "春季 (2-4月)", 2: "夏季 (5-7月)", 3: "秋季 (8-10月)", 4: "冬季 (11-1月)"}
    plot_data.index = plot_data.index.map(season_labels)
    
    plot_data.plot(kind="bar", color="orange")

    plt.title("季節 PM2.5 平均值")
    plt.xlabel("季節")
    plt.ylabel("PM2.5 平均值")
    plt.xticks(rotation=0)
    plt.tight_layout()

    plt.savefig("results/chart3_season.png")
    plt.close()
# 4. 超標天數圖 (一目了然對照版)
def plot_exceed_days(count):
    plt.figure(figsize=(6, 5))

    exceed = int(count)       # 超標天數 (28天)
    normal = 731 - exceed     # 未超標天數 (總共731天)

    # 給它兩個類別，兩根柱子
    categories = ['正常天數\n(<= 15 µg/m³)', '超標天數\n(> 15 µg/m³)']
    values = [normal, exceed]
    colors = ['#2ecc71', '#e74c3c'] # 正常用綠色，超標用紅色

    # 畫出長條圖，寬度設為 0.5 讓它留白
    bars = plt.bar(categories, values, color=colors, width=0.5)

    plt.title("花蓮 PM2.5 數據分佈天數統計", fontsize=14, fontweight='bold', pad=15)
    plt.ylabel("天數 (天)", fontsize=12)
    
    # 讓 Y 軸上限留一點空間給數字標籤
    plt.ylim(0, 800)

    # 自動在兩根柱子上方加上正確的數字
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 15,
                 f'{int(height)} 天',
                 ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig("results/chart4_exceed.png")
    plt.close()