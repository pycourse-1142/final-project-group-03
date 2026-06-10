import matplotlib.pyplot as plt
import os

# 設定中文字型
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# 建立結果資料夾
os.makedirs("results", exist_ok=True)


# 1. 每日趨勢圖
def plot_daily_pm25(df):
    plt.figure(figsize=(10, 5))

    clean_df = df.dropna(subset=["日期", "daily_avg"])

    plt.plot(clean_df["日期"], clean_df["daily_avg"])

    plt.title("每日 PM2.5 趨勢圖")
    plt.xlabel("日期")
    plt.ylabel("PM2.5 平均值")
    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig("results/chart1_daily.png")
    plt.show()
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
    plt.show()
    plt.close()


# 3. 季平均圖
def plot_season_pm25(season_avg):
    plt.figure(figsize=(6, 5))

    plot_data = season_avg.copy()

    season_labels = {
        1: "春季\n(2-4月)",
        2: "夏季\n(5-7月)",
        3: "秋季\n(8-10月)",
        4: "冬季\n(11-1月)"
    }

    plot_data.index = plot_data.index.map(season_labels)

    plot_data.plot(kind="bar", color="orange")

    plt.title("季節 PM2.5 平均值")
    plt.xlabel("季節")
    plt.ylabel("PM2.5 平均值")

    plt.xticks(rotation=0)

    plt.tight_layout()

    plt.savefig("results/chart3_season.png")
    plt.show()
    plt.close()


# 4. 超標天數圖
def plot_exceed_days(exceed_days, total_days):
    plt.figure(figsize=(7, 5))

    normal_days = total_days - exceed_days

    categories = [
        '正常天數\n(≤15 µg/m³)',
        '超標天數\n(>15 µg/m³)'
    ]

    values = [
        normal_days,
        exceed_days
    ]

    colors = [
        '#2ecc71',
        '#e74c3c'
    ]

    bars = plt.bar(
        categories,
        values,
        color=colors,
        width=0.5
    )

    plt.title("花蓮 PM2.5 超標統計")
    plt.ylabel("天數")

    plt.ylim(0, max(values) * 1.2)

    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + max(values) * 0.02,
            f"{int(height)} 天",
            ha='center'
        )

    plt.tight_layout()

    plt.savefig("results/chart4_exceed.png")
    plt.show()
    plt.close()