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

# 3. Premium Information

| Column | Type | Description | Example | Validation |
|---------|------|-------------|---------|------------|
| total_premium | Float | Total insurance premium charged for the policy. | 1,245.80 | >= 0 |
| liability_premium | Float | Portion of the total premium allocated to liability coverage. | 540.25 | >= 0 |
| property_damage_premium | Float | Portion of the premium allocated to property damage coverage. | 210.40 | >= 0 |
| liability_property_injury_premium | Float | Premium allocated to liability coverage for property damage and bodily injury. | 385.75 | >= 0 |
| theft_premium | Float | Portion of the premium allocated to theft coverage. | 82.60 | >= 0 |
| fire_premium | Float | Portion of the premium allocated to fire damage coverage. | 65.30 | >= 0 |
| glass_premium | Float | Portion of the premium allocated to glass damage coverage. | 48.20 | >= 0 |
| legal_protection_premium | Float | Portion of the premium allocated to legal protection coverage. | 32.10 | >= 0 |
| occupants_premium | Float | Portion of the premium allocated to occupant protection coverage. | 27.50 | >= 0 |

# 4. Claims Information 

| Column | Type | Description | Example | Validation |
|---------|------|-------------|---------|------------|
| total_claims | Integer | Total number of claims reported for the policy. | 1 | >= 0 |
| liability_claims | Integer | Number of liability claims reported. | 0 | >= 0 |
| property_claims | Integer | Number of property damage claims reported. | 1 | >= 0 |
| liability_property_injury_claims | Integer | Number of liability claims involving property damage or bodily injury. | 0 | >= 0 |
| theft_claims | Integer | Number of theft claims reported. | 0 | >= 0 |
| fire_claims | Integer | Number of fire damage claims reported. | 0 | >= 0 |
| glass_claims | Integer | Number of glass damage claims reported. | 0 | >= 0 |
| legal_protection_claims | Integer | Number of legal protection claims reported. | 0 | >= 0 |
| occupants_claims | Integer | Number of occupant protection claims reported. | 0 | >= 0 |
| total_incurred | Float | Total monetary amount incurred from all claims. | 2450.75 | >= 0 |
| liability_incurred | Float | Total incurred amount from liability claims. | 0.00 | >= 0 |
| liability_property_incurred | Float | Total incurred amount from liability property damage claims. | 1200.00 | >= 0 |
| liability_injury_incurred | Float | Total incurred amount from liability bodily injury claims. | 0.00 | >= 0 |
| property_incurred | Float | Total incurred amount from property damage claims. | 850.00 | >= 0 |
| theft_incurred | Float | Total incurred amount from theft claims. | 0.00 | >= 0 |
| fire_incurred | Float | Total incurred amount from fire claims. | 0.00 | >= 0 |
| glass_incurred | Float | Total incurred amount from glass claims. | 400.75 | >= 0 |
| legal_protection_incurred | Float | Total incurred amount from legal protection claims. | 0.00 | >= 0 |
| occupants_incurred | Float | Total incurred amount from occupant protection claims. | 0.00 | >= 0 |

# 5. Exposure Information 

| Column | Type | Description | Example | Validation |
|---------|------|-------------|---------|------------|
| total_exposure | Float | Total insured exposure for the policy during the coverage period. | 1.00 | >= 0 |
| liability_exposure | Float | Exposure associated with liability coverage. | 1.00 | >= 0 |

# 6. Code Definitions

| Category | Code | Meaning |
|----------|------|---------|
| Policy Type | TP | Third-Party Liability |
| Policy Type | TPG | Third-Party + Glass |
| Policy Type | CC | Combined Coverage |
| Policy Type | COMP_E | Comprehensive with Excess |
| Policy Type | COMP_N | Comprehensive without Excess |
| Policy Status | A | Active |
| Policy Status | C | Cancelled |
| Business Type | NB | New Business |
| Business Type | P | Policy Renewal |
| Fuel Type | G | Gasoline |
| Fuel Type | D | Diesel |
| Payment Frequency | A | Annual |
| Payment Frequency | S | Semiannual |
| Payment Frequency | Q | Quarterly |
| Payment Frequency | M | Monthly |
| Municipality Type | I | Urban Municipality |
| Municipality Type | II | Intermediate Municipality |
| Municipality Type | III | Rural Municipality |