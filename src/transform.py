from extract import extract_data
from validate import validate_data


def transform_data(df):

    # Insured table
    insured = df[
        ["insured_id"]
    ].drop_duplicates().copy()

    # Policy table
    policy = df[
        [
            "insured_id",
            "year",
            "policy_type",
            "policy_status",
            "business_type",
            "driver_age",
            "bonus_score",
            "total_premium",
            "total_exposure"
        ]
    ].copy()

    # Vehicle snapshot table
    vehicle_snapshot = df[
        [
            "insured_id",
            "year",
            "vehicle_age",
            "vehicle_brand",
            "vehicle_value",
            "fuel_type",
            "power_to_weight_ratio"
        ]
    ].copy()

    # Claims table
    claims = df[
        [
            "insured_id",
            "year",
            "total_claims",
            "total_incurred"
        ]
    ].copy()

    return {
        "insured": insured,
        "policy": policy,
        "vehicle_snapshot": vehicle_snapshot,
        "claims": claims
    }


if __name__ == "__main__":
    df = extract_data()
    df = validate_data(df)

    tables = transform_data(df)

    print("\nTransformation successful!")

    for name, table in tables.items():
        print(f"{name}: {len(table):,} rows, "
              f"{len(table.columns)} columns")
