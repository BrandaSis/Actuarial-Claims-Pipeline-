from extract import extract_data


def validate_data(df):
    # Check required columns
    required_columns = [
        "insured_id",
        "year",
        "total_claims",
        "total_incurred",
        "total_premium",
        "total_exposure"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(f"Missing columns: {missing_columns}")

    # Check for missing primary key values
    if df[["insured_id", "year"]].isnull().any().any():
        raise ValueError("Missing primary key values found.")

    # Check for duplicate policy-year records
    duplicates = df.duplicated(
        subset=["insured_id", "year"]
    ).sum()

    if duplicates > 0:
        raise ValueError(f"Found {duplicates} duplicate records.")

    # Check for invalid negative values
    for col in ["total_claims", "total_premium", "total_exposure"]:
        if (df[col] < 0).any():
            raise ValueError(f"Negative values found in {col}.")

    # Report missing values
    missing = df.isnull().sum()
    missing = missing[missing > 0]

    print("Data validation successful!")
    print(f"Rows checked: {len(df)}")
    print(f"Duplicate policy-year records: {duplicates}")
    print("\nColumns with missing values:")
    print(missing if not missing.empty else "None")

    return df


if __name__ == "__main__":
    df = extract_data()
    validate_data(df)
