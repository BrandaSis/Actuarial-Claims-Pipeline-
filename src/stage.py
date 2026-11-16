import csv
from pathlib import Path

from psycopg import sql
from load import get_connection

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "raw" / "motor_insurance.csv"


def stage_data():
    # Read all column names from the original CSV
    with open(DATA_PATH, "r", encoding="utf-8-sig", newline="") as file:
        columns = next(csv.reader(file, delimiter=";"))

    with get_connection() as conn:
        with conn.cursor() as cur:
            # Create a separate staging schema
            cur.execute("CREATE SCHEMA IF NOT EXISTS staging;")

            # Define all 47 columns as TEXT for raw storage
            column_definitions = sql.SQL(", ").join(
                sql.SQL("{} TEXT").format(sql.Identifier(col))
                for col in columns
            )

            cur.execute(
                sql.SQL(
                    "CREATE TABLE IF NOT EXISTS "
                    "staging.motor_insurance_raw ({})"
                ).format(column_definitions)
            )

            # Refresh staging data on each run
            cur.execute("TRUNCATE TABLE staging.motor_insurance_raw;")

            # Import the complete CSV
            with open(DATA_PATH, "rb") as file:
                with cur.copy(
                    "COPY staging.motor_insurance_raw "
                    "FROM STDIN WITH "
                    "(FORMAT CSV, HEADER TRUE, DELIMITER ';')"
                ) as copy:
                    while chunk := file.read(1024 * 1024):
                        copy.write(chunk)

            cur.execute(
                "SELECT COUNT(*) FROM staging.motor_insurance_raw;"
            )
            row_count = cur.fetchone()[0]

            print("Staging completed successfully!")
            print(f"Rows: {row_count:,}")
            print(f"Columns: {len(columns)}")


if __name__ == "__main__":
    stage_data()
