
# CO2 Emission Analysis Across Countries (2022)

## Stakeholder & Scenario
A climate-and-energy nonprofit needs to decide where to direct community-protection and climate-support efforts using an undocumented global emissions dataset (`data/co2_emissions_2022.csv`). 

As an analyst working for the nonprofit, I needed to inspect what's actually inside the file before trusting it to make community-protection decisions.

## Questions & Data Quality Questions
Before building any decisions on top of this data, I set out to answer key questions:
- What does each column actually hold and what data type is it?
- Is this dataset structured or unstructured?
- Are there missing values or suspicious rows that should make someone cautious?
- What specific question should be asked of the data's source before trusting it?

Here are my two specific data-quality questions for the source:
1. How were the CO2 emissions numbers collected and estimated for each country to ensure direct measurement reliability?
2. Should non-country rows like international aviation (row 122), international shipping (row 127), and missing country rows (76 to 81) be filtered out when calculating emissions for individual countries?

## Dataset Source
- **Original Source:** OWID CO2 and Greenhouse Gas Emissions data (Our World in Data, based on the Global Carbon Project)[cite: 7].
- **Local File:** Country-level energy and emissions dataset (`data/co2_emissions_2022.csv`).

## Key Insights & What I Found
Using terminal tools (`head`, `cut`, `grep`), I inspected the raw file and discovered:
- **Structure:** The dataset is structured because it is organized in a table (structured CSV) where each data type has its respective column and row. However, it has logical mix-ups: it puts real countries right next to continents (like Africa), income groups, and transport categories like international aviation and shipping.
- **Column Types:** `country` (String), `iso_code` (String), `year` (Integer), `population` (Integer), `gdp` (Integer), and `co2` (Float).
- **Missing Data:** Running terminal checks showed 36 blank `iso_code` rows and 89 missing `gdp` values.

## Reflection & AI-Literacy
- **Risks:** Trusting an AI assistant or unverified data without checking it yourself can lead to risks like hallucinations, missed data errors, or **representation bias** (where certain regions or sub-groups are misrepresented or overlooked due to missing values and aggregated categories).
- **My Rule:** Always ask the AI to provide the sources or references so I can double-check the information myself.

## License
This project uses data licensed under CC BY 4.0 (Our World in Data)[cite: 7]. The repository code and documentation are open source under the MIT License.
