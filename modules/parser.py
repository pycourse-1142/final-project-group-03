import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(
            path,
            encoding='cp950',
            skiprows=2
        )

        print("資料讀取成功")
        return df

    except Exception as e:
        print("讀檔失敗:", e)
        return None