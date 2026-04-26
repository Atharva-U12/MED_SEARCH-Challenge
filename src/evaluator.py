import os
import time
import pandas as pd
import importlib.util

def load_and_preprocess():
    # Standardizing cleaning for everyone
    try:
        csv_path = os.path.join("data", "MED_SEARCH.csv")
        df = pd.read_csv(csv_path)
        df = df[df["is_discontinued"] == False]
        df = df[df["primary_strength"].notna()]
        
        for col in ["primary_ingredient", "primary_strength", "dosage_form"]:
            df[col] = df[col].astype(str).str.strip().str.lower()
        
        df["brand_name"] = df["brand_name"].str.strip()
        df.reset_index(drop=True, inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def run_evaluation(file_path, df):
    # Dynamic import allows teammates to name files however they want
    spec = importlib.util.spec_from_file_location("sub", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Test cases: Replace with real brand names from your Medsearch.csv
    test_brands = ["Crocin", "Taxim-O"] 
    total_score = 0
    start = time.perf_counter()
    
    try:
        for brand in test_brands:
            res = module.get_recommendations(df, brand)
            if res is not None and not res.empty:
                orig_p = df[df["brand_name"] == brand]["price_inr"].iloc[0]
                # Reward finding cheaper options
                if res.iloc[0]["price_inr"] < orig_p:
                    total_score += 50 
    except Exception:
        total_score = 0

    end = time.perf_counter()
    return total_score, round(end - start, 6)

if __name__ == "__main__":
    clean_df = load_and_preprocess()
    leaderboard_data = []
    
    sub_folder = "submissions"
    for filename in os.listdir(sub_folder):
        # Only evaluate files starting with 'submission_' and ignore the template
        if filename.startswith("submission_") and filename != "submission_template.py":
            user = filename.replace("submission_", "").replace(".py", "")
            score, speed = run_evaluation(os.path.join(sub_folder, filename), clean_df)
            leaderboard_data.append([user, score, speed])

    # Generate the Leaderboard
    lb_df = pd.DataFrame(leaderboard_data, columns=["Participant", "Score", "Execution Time (s)"])
    lb_df = lb_df.sort_values(by=["Score", "Execution Time (s)"], ascending=[False, True])
    
    with open("leaderboard.md", "w", encoding="utf-8") as f:
        f.write("# 🏆 MedSearch Competition Leaderboard\n\n")
        f.write(lb_df.to_markdown(index=False))