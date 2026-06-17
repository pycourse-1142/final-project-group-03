import pandas as pd

def load_data(path):
    """
    載入並清洗 CSV 數據，專門處理環境監測資料格式。
    """
    try:
        # 讀取 CSV，指定繁體中文編碼 (cp950) 並跳過前兩行無效說明列
        df = pd.read_csv(
            path,
            encoding='cp950',
            skiprows=2
        )
        print("【系統通知】資料讀取成功")
        
        # 定義 24 小時的欄位名稱 (即 "00" 到 "23")
        hour_columns = [f"{i:02d}" for i in range(24)]
        
        # 1. 檢查必要的欄位是否存在，避免後續處理發生 Key Error
        if "日期" not in df.columns or "測項" not in df.columns:
            print("❌ 錯誤：CSV 檔案格式不符，缺少 '日期' 或 '測項' 欄位")
            return None
            
        # 2. 篩選出測項為 "PM2.5" 的資料，排除其他污染指標
        initial_count = len(df)
        df = df[df["測項"] == "PM2.5"]
        
        # 3. 將 24 小時的所有數值列強制轉換為浮點數
        # errors='coerce' 處理方式：遇到無法轉換的字串（如儀器維修代碼 "NR"、"x"）會直接轉為 NaN (空值)
        df[hour_columns] = df[hour_columns].apply(pd.to_numeric, errors='coerce')
        
        # 4. 資料清洗：剔除整行 24 小時皆為空值的無效紀錄
        df = df.dropna(subset=hour_columns, how='all')
        cleaned_count = len(df)
        
        print(f"【品質控制】成功過濾 PM2.5 數據。原始筆數: {initial_count} 行，有效筆數: {cleaned_count} 行。")
        print("【品質控制】已完成無效值（非數字與儀器維修紀錄）清理。")
        
        return df

    except Exception as e:
        # 捕捉檔案路徑錯誤或讀取過程中的例外狀況
        print(f"❌ 讀檔或資料清洗失敗: {e}")
        return None