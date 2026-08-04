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
|--------|------|-------------|---------|------------|
| insured_id | Integer | Unique identifier assigned to each insured policyholder. The same policyholder may appear in multiple years of the dataset. | 12584 | Required; must not be NULL |
| year | Integer | Calendar year associated with the insurance policy record. | 2023 | Must be between 2022 and 2024 |
| policy_type | String | Type of insurance coverage purchased by the policyholder. | COMP_E | Must match a valid policy type code |
| policy_status | String | Current status of the insurance policy. | A | Must match a valid status code |
| business_type | String | Indicates whether the policy is a new policy or a renewal. | NB | Must match a valid business type code |
| payment_frequency | String | Frequency at which the insurance premium is paid. | A | Must match a valid payment frequency code |
| bonus_score | String | Bonus-Malus classification that reflects the insured's claim history and influences premium calculation. | G | Required; must not be NULL |