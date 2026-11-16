from extract import extract_data
from validate import validate_data
from transform import transform_data
from stage import stage_data

from load import (
    get_connection,
    load_insured,
    load_policy,
    load_vehicle_snapshot,
    load_claims
)


def run_pipeline():
    print("Starting Actuarial Claims Pipeline...\n")

    # 1. Extract
    df = extract_data()
    print(f"Extracted {len(df):,} records.")

    # 2. Validate
    df = validate_data(df)

    # 3. Stage all 47 original columns
    stage_data()

    # 4. Transform into database tables
    tables = transform_data(df)
    print("\nTransformation complete.")

    # 5. Load into PostgreSQL
    with get_connection() as conn:
        load_insured(conn, tables["insured"])
        load_policy(conn, tables["policy"])
        load_vehicle_snapshot(conn, tables["vehicle_snapshot"])
        load_claims(conn, tables["claims"])

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
