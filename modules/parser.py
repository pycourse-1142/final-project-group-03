import pandas as pd

def load_data(path):
    try:
        df = pd.read_csv(
            path,
            encoding='cp950',
            skiprows=2
        )
        print("【系統通知】資料讀取成功")
        
        # --- 新增的防禦性資料品質檢查與清理 ---
        hour_columns = [f"{i:02d}" for i in range(24)]
        
        # 1. 檢查必要的欄位是否存在
        if "日期" not in df.columns or "測項" not in df.columns:
            print("❌ 錯誤：CSV 檔案格式不符，缺少 '日期' 或 '測項' 欄位")
            return None
            
        # 2. 篩選出只有 PM2.5 的資料 (防禦性過濾)
        initial_count = len(df)
        df = df[df["測項"] == "PM2.5"]
        
        # 3. 把 24 小時的數值強制轉換成數字，無法轉換的（如儀器維修字串）變成 NaN 空值
        df[hour_columns] = df[hour_columns].apply(pd.to_numeric, errors='coerce')
        
        # 4. 判斷是否有整行 24 小時全部都是空值的無效列，將其剔除
        df = df.dropna(subset=hour_columns, how='all')
        cleaned_count = len(df)
        
        print(f"【品質控制】成功過濾 PM2.5 數據。原始筆數: {initial_count} 行，有效筆數: {cleaned_count} 行。")
        print("【品質控制】已完成無效值（非數字與儀器維修紀錄）清理。")
        
        return df

    except Exception as e:
        print(f"❌ 讀檔或資料清洗失敗: {e}")
        return None