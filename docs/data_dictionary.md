# Data Dictionary

## Project 

Acturial Claims Pipeline

## Purpose

Defines each field in the Motor Insurance dataset used throughout the project. This serves as the reference for data validation, database design, ETL development, and reporting. 

---

## Dataset Information 

- Source: Motor Insurance Portfolio Dataset (2022-2024)
- https://data.mendeley.com/datasets/sw4jmdb2sm/1
- Record: 354,140
- Columns: 47
- File Format: CSV

---

## Contents

1. Policy Information
2. Driver & Vehicle Information
3. Premium Information 
4. Claims Information
5. Exposure Information
6. Code Definitions

--- 

# 1. Policy Information

| Column | Type | Description | Example | Validation | 
|---------|------|-------------|---------|------------|
| insured_id | Integer | Unique identifier assigned to each insured policyholder. The same policyholder may appear in multiple years of the dataset. | 12584 | Required; must not be NULL |
| year | Integer | Calendar year associated with the insurance policy record. | 2023 | Must be between 2022 and 2024 |
| policy_type | String | Type of insurance coverage purchased by the policyholder. | COMP_E | Must match a valid policy type code |
| policy_status | String | Current status of the insurance policy. | A | Must match a valid status code |
| business_type | String | Indicates whether the policy is a new policy or a renewal. | NB | Must match a valid business type code |
| payment_frequency | String | Frequency at which the insurance premium is paid. | A | Must match a valid payment frequency code |
| bonus_score | String | Bonus-Malus classification that reflects the insured's claim history and influences premium calculation. | G | Required; must not be NULL |

# 2. Driver & Vehicle Information

| Column | Type | Description | Example | Validation |
|---------|------|-------------|---------|------------|
| driver_age | Integer | Age of the primary driver at the time of the policy. | 38 | Must be greater than or equal to 16 |
| vehicle_age | Float | Age of the insured vehicle in years. | 7 | Must be greater than or equal to 0 |
| age_driving_licence | Float | Number of years the driver has held a valid driver's license. | 18 | Must be greater than or equal to 0 |
| fuel_type | String | Fuel type of the insured vehicle. | G | Must match a valid fuel type code |
| vehicle_value | Float | Declared insured value of the vehicle. | 18,500 | Must be greater than or equal to 0 |
| seats | Integer | Number of seats in the insured vehicle. | 5 | Must be greater than 0 |
| power_to_weight_ratio | Float | Vehicle power-to-weight ratio used as a measure of performance. | 12.3 | Must be greater than 0 |
| vehicle_brand | String | Manufacturer or brand of the insured vehicle. | RENAULT | Required; must not be NULL |
| municipality_type | String | Classification of the municipality where the insured vehicle is registered. | I | Must match a valid municipality code |
| circulation_area | String | Geographic circulation area classification assigned to the vehicle. | U | Must match a valid circulation area code |