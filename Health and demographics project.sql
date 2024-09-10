# Data Cleaning

SELECT *
FROM health_demographics;

CREATE TABLE health_demographics_staging
LIKE health_demographics;

INSERT health_demographics_staging
SELECT *
FROM health_demographics;

SELECT *
FROM health_demographics_staging;

SELECT *,
ROW_NUMBER() OVER(PARTITION BY Country, `Year`, Percentage_expenditure, Total_expenditure, GDP, Population) AS Row_num
FROM health_demographics_staging;

WITH duplicate_cte AS
(
SELECT *,
ROW_NUMBER() OVER(PARTITION BY Country, `Year`, Percentage_expenditure, Total_expenditure, GDP, Population) AS Row_num
FROM health_demographics_staging
)
SELECT *
FROM duplicate_cte
WHERE Row_num > 1;

SELECT *
FROM health_demographics_staging;

ALTER TABLE health_demographics_staging
MODIFY COLUMN Adult_mortality Float,
MODIFY COLUMN Infant_deaths Float,
MODIFY COLUMN Under_five_deaths Float;

SELECT 	*,
		Adult_mortality, (Adult_mortality * 0.1),
		Infant_deaths, (Infant_deaths * 0.1),
		Under_five_deaths, (Under_five_deaths * 0.1)
FROM health_demographics_staging;

UPDATE health_demographics_staging
SET Adult_mortality = Adult_mortality *(0.1),
	Infant_deaths = Infant_deaths *(0.1),
    Under_five_deaths = Under_five_deaths *(0.1);
    
SELECT *
FROM health_demographics_staging;

ALTER TABLE health_demographics_staging
RENAME COLUMN Alcohol to Alcohol_ltrs_percapita,
RENAME COLUMN Hepatitis_B to HepatitisB_immunization_percentage,
RENAME COLUMN Measles to Measles_cases,
RENAME COLUMN BMI to Average_BMI,
RENAME COLUMN Polio to Polio_immunization_percentage,
RENAME COLUMN Diphtheria to Diphtheria_immunization_percentage,
RENAME COLUMN Schooling to Average_schooling_years,
RENAME COLUMN Adult_mortality to Adult_mortality_percentage,
RENAME COLUMN Infant_deaths to Infant_deaths_percentage,
RENAME COLUMN Under_five_deaths to Under_five_deaths_percentage, 
RENAME COLUMN Percentage_expenditure to Total_expenditure_health,
RENAME COLUMN Total_expenditure to Percentage_expenditure_health; 


SELECT *
FROM health_demographics_staging
WHERE  Country IS NULL;

SELECT *
FROM health_demographics_staging;


