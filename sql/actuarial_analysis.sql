-- Portfolio-level actuarial summary

SELECT
    COUNT(*) AS policy_years,
    SUM(c.total_claims) AS total_claims,
    ROUND(SUM(c.total_incurred), 2) AS total_incurred,
    ROUND(SUM(p.total_premium), 2) AS total_premium,
    ROUND(SUM(p.total_exposure), 2) AS total_exposure
FROM policy p
JOIN claims c
    ON p.insured_id = c.insured_id
    AND p.year = c.year;


-- Portfolio-level actuarial metrics

SELECT
    ROUND(
        SUM(c.total_claims)::NUMERIC /
        NULLIF(SUM(p.total_exposure), 0), 4
    ) AS claim_frequency,

    ROUND(
        SUM(c.total_incurred) /
        NULLIF(SUM(c.total_claims), 0), 2
    ) AS claim_severity,

    ROUND(
        100 * SUM(c.total_incurred) /
        NULLIF(SUM(p.total_premium), 0), 2
    ) AS loss_to_premium_pct

FROM policy p
JOIN claims c
    ON p.insured_id = c.insured_id
    AND p.year = c.year;


-- Annual actuarial performance (2022–2024)

SELECT
    p.year,
    COUNT(*) AS policy_years,

    SUM(c.total_claims) AS total_claims,

    ROUND(
        SUM(c.total_claims)::NUMERIC /
        NULLIF(SUM(p.total_exposure), 0), 4
    ) AS claim_frequency,

    ROUND(
        SUM(c.total_incurred) /
        NULLIF(SUM(c.total_claims), 0), 2
    ) AS claim_severity,

    ROUND(
        100 * SUM(c.total_incurred) /
        NULLIF(SUM(p.total_premium), 0), 2
    ) AS loss_to_premium_pct

FROM policy p
JOIN claims c
    ON p.insured_id = c.insured_id
    AND p.year = c.year

GROUP BY p.year
ORDER BY p.year;

-- Actuarial performance by policy type in 2024

SELECT
    p.policy_type,
    COUNT(*) AS policy_years,

    SUM(c.total_claims) AS total_claims,

    ROUND(
        SUM(c.total_claims)::NUMERIC /
        NULLIF(SUM(p.total_exposure), 0), 4
    ) AS claim_frequency,

    ROUND(
        100 * SUM(c.total_incurred) /
        NULLIF(SUM(p.total_premium), 0), 2
    ) AS loss_to_premium_pct

FROM policy p
JOIN claims c
    ON p.insured_id = c.insured_id
    AND p.year = c.year

WHERE p.year = 2024

GROUP BY p.policy_type
ORDER BY loss_to_premium_pct DESC NULLS LAST;

-- COMP_N performance across years

SELECT
    p.year,
    COUNT(*) AS policy_years,

    SUM(c.total_claims) AS total_claims,

    ROUND(
        SUM(c.total_claims)::NUMERIC /
        NULLIF(SUM(p.total_exposure), 0), 4
    ) AS claim_frequency,

    ROUND(
        SUM(c.total_incurred) /
        NULLIF(SUM(c.total_claims), 0), 2
    ) AS claim_severity,

    ROUND(
        100 * SUM(c.total_incurred) /
        NULLIF(SUM(p.total_premium), 0), 2
    ) AS loss_to_premium_pct

FROM policy p
JOIN claims c
    ON p.insured_id = c.insured_id
    AND p.year = c.year

WHERE p.policy_type = 'COMP_N'

GROUP BY p.year
ORDER BY p.year;

-- COMP_N premium and loss per exposure

SELECT
    p.year,

    ROUND(
        SUM(p.total_premium) /
        NULLIF(SUM(p.total_exposure), 0), 2
    ) AS premium_per_exposure,

    ROUND(
        SUM(c.total_incurred) /
        NULLIF(SUM(p.total_exposure), 0), 2
    ) AS incurred_per_exposure

FROM policy p
JOIN claims c
    ON p.insured_id = c.insured_id
    AND p.year = c.year

WHERE p.policy_type = 'COMP_N'

GROUP BY p.year
ORDER BY p.year;
