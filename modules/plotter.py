import matplotlib.pyplot as plt
import os

os.makedirs("results", exist_ok=True)


# 1. 每日趨勢
def plot_daily_pm25(df):

    plt.figure(figsize=(10, 5))
    plt.plot(df["日期"], df["daily_avg"])

    plt.title("Daily PM2.5")
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("results/chart1_daily.png")
    plt.show()
    plt.close()


# 2. 月平均
def plot_monthly_pm25(monthly_avg):

    plt.figure(figsize=(8, 5))
    monthly_avg.plot(kind="bar")

    plt.title("Monthly PM2.5")
    plt.tight_layout()

    plt.savefig("results/chart2_monthly.png")
    plt.show()
    plt.close()


# 3. 季平均
def plot_season_pm25(season_avg):

    plt.figure(figsize=(6, 5))
    season_avg.plot(kind="bar", color="orange")

    plt.title("Season PM2.5")
    plt.tight_layout()

    plt.savefig("results/chart3_season.png")
    plt.show()
    plt.close()


# 4. 超標天數
def plot_exceed_days(count):

    plt.figure(figsize=(4, 4))

    plt.bar(["Exceed Days"], [count], color="red")

    plt.title("PM2.5 Exceed Days")

    plt.savefig("results/chart4_exceed.png")
    plt.show()
    plt.close()