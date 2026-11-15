
-- Actuarial Claims Pipeline
-- PostgreSQL Database Schema

-- Insured
CREATE TABLE insured (
    insured_id BIGINT PRIMARY KEY
);

-- Policy
CREATE TABLE policy (
    insured_id BIGINT NOT NULL,
    year SMALLINT NOT NULL,

    policy_type TEXT,
    policy_status TEXT,
    business_type TEXT,
    driver_age NUMERIC,
    bonus_score NUMERIC,
    total_premium NUMERIC,
    total_exposure NUMERIC,

    PRIMARY KEY (insured_id, year),
    FOREIGN KEY (insured_id)
        REFERENCES insured(insured_id)
);

-- Vehicle Snapshot
CREATE TABLE vehicle_snapshot (
    insured_id BIGINT NOT NULL,
    year SMALLINT NOT NULL,

    vehicle_age NUMERIC,
    vehicle_brand TEXT,
    vehicle_value NUMERIC,
    fuel_type TEXT,
    power_to_weight_ratio NUMERIC,

    PRIMARY KEY (insured_id, year),
    FOREIGN KEY (insured_id, year)
        REFERENCES policy(insured_id, year)
);

-- Claims
CREATE TABLE claims (
    insured_id BIGINT NOT NULL,
    year SMALLINT NOT NULL,

    total_claims INTEGER,
    total_incurred NUMERIC,

    PRIMARY KEY (insured_id, year),
    FOREIGN KEY (insured_id, year)
        REFERENCES policy(insured_id, year)
);
