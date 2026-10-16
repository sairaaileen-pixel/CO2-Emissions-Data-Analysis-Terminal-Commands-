
# CO2 Emissions Data Analysis (2022)

## What this project is about
This project is an exploratory first pass at an undocumented climate and energy dataset (`co2_emissions_2022.csv`). As an analyst working for a nonprofit, I needed to check what's actually inside the file using only terminal commands (no Python yet) before trusting it to make community-protection decisions.

## Key Insights
- **Structure:** The dataset is organized in a table (structured CSV), but it has logical mix-ups: it puts real countries right next to continents (like Africa), income groups, and transport sectors like international aviation and shipping.
- **Missing Data:** Running terminal checks showed 36 blank `iso_code` rows and 89 missing `gdp` values.

## My Data Quality Question
Should non-country rows like international aviation (row 122), international shipping (row 127), and missing country rows (76 to 81) be filtered out when calculating emissions for individual countries?

## AI Reflection
Using AI without checking the facts can cause hallucinations or missed data errors. My personal rule to prevent this is: always ask the AI for its sources or references so I can double-check the information myself.
# CO2 Emissions Data Analysis (2022)

## Scenario & Questions
A climate-and-energy nonprofit needs to decide where to direct community-protection and climate-support efforts using a country-level energy and emissions dataset (`data/co2_emissions_2022.csv`) that landed with zero documentation. 

Before building any decisions on top of this data, I set out to answer key questions using terminal commands only:
- What does each column actually hold and what data type is it?
- Is this dataset structured or unstructured?
- Are there missing values or suspicious rows that should make someone cautious?
- What specific question should be asked of the data's source before trusting it?

## Dataset Source
- **Source:** Country-level energy and emissions dataset (`data/co2_emissions_2022.csv`).

## What I Found
Using terminal tools (`head`, `cut`, `grep`), I inspected the raw file and discovered:
- **Structure:** The dataset is structured because it is organized in a table where each data type has its respective column and row. However, it mixes real countries with continents (like Africa), income groups, and transport categories like international aviation and shipping.
- **Column Types:** `country` (String), `iso_code` (String), `year` (Integer), `population` (Integer), `gdp` (Integer), and `co2` (Float).
- **Missing Values:** Running terminal checks revealed 36 blank `iso_code` rows and 89 missing `gdp` values.

## Data Quality Question
Should non-country rows like international aviation (row 122), international shipping (row 127), and missing country rows (76 to 81) be filtered out when calculating emissions for individual countries?

## Reflection & AI-Literacy
- **Risks:** Trusting an AI assistant without checking it yourself can lead to risks like hallucinations or bias/underrepresentation of minorities.

- **My Rule:** Always ask the AI to provide the sources or references so I can check the information myself.
