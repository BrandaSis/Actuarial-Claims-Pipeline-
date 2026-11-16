from pathlib import Path
import pandas as pd

# Locate the raw insurance dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "motor_insurance.csv"


def extract_data():
    df = pd.read_csv(DATA_PATH, sep=";")
    return df


if __name__ == "__main__":
    df = extract_data()
    print("Dataset loaded successfully!")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
