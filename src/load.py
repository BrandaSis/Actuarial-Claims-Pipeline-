import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv

from extract import extract_data
from validate import validate_data
from transform import transform_data

import pandas as pd

# Load database credentials
PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")


def get_connection():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def load_insured(conn, insured_df):
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM insured;")

        if cur.fetchone()[0] > 0:
            print("Insured table already contains data. Skipping.")
            return

        with cur.copy("COPY insured (insured_id) FROM STDIN") as copy:
            for (insured_id,) in insured_df.itertuples(
                index=False, name=None
            ):
                copy.write_row((int(insured_id),))

        print(f"Loaded {len(insured_df):,} insured records!")


def load_policy(conn, policy_df):
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM policy;")

        if cur.fetchone()[0] > 0:
            print("Policy table already contains data. Skipping.")
            return

        columns = ", ".join(policy_df.columns)

        with cur.copy(
            f"COPY policy ({columns}) FROM STDIN"
        ) as copy:
            for row in policy_df.itertuples(index=False, name=None):
                copy.write_row(row)

        print(f"Loaded {len(policy_df):,} policy records!")


def load_vehicle_snapshot(conn, vehicle_df):
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM vehicle_snapshot;")

        count = cur.fetchone()[0]

        if count > 0:
            if count != len(vehicle_df):
                raise ValueError("Vehicle table has an unexpected row count.")
            print("Vehicle snapshot already loaded. Skipping.")
            return

        columns = ", ".join(vehicle_df.columns)

        with cur.copy(
            f"COPY vehicle_snapshot ({columns}) FROM STDIN"
        ) as copy:
            for row in vehicle_df.itertuples(index=False, name=None):
                clean_row = tuple(
                    None if pd.isna(value) else value
                    for value in row
                )
                copy.write_row(clean_row)

        print(f"Loaded {len(vehicle_df):,} vehicle records!")


def load_claims(conn, claims_df):
    with conn.cursor() as cur:
        cur.execute("SELECT COUNT(*) FROM claims;")

        count = cur.fetchone()[0]

        if count > 0:
            if count != len(claims_df):
                raise ValueError("Claims table has an unexpected row count.")
            print("Claims table already loaded. Skipping.")
            return

        columns = ", ".join(claims_df.columns)

        with cur.copy(
            f"COPY claims ({columns}) FROM STDIN"
        ) as copy:
            for row in claims_df.itertuples(index=False, name=None):
                clean_row = tuple(
                    None if pd.isna(value) else value
                    for value in row
                )
                copy.write_row(clean_row)

        print(f"Loaded {len(claims_df):,} claims records!")


if __name__ == "__main__":
    df = extract_data()
    df = validate_data(df)
    tables = transform_data(df)

    with get_connection() as conn:
        load_insured(conn, tables["insured"])
        load_policy(conn, tables["policy"])
        load_vehicle_snapshot(conn, tables["vehicle_snapshot"])
        load_claims(conn, tables["claims"])

