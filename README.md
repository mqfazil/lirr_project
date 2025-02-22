# LIRR Delay Analysis
Analyzes Long Island Rail Road (LIRR) on-time performance data (2015-2025) to identify average delays by branch.

## Tools
- Python, Pandas, Matplotlib

## Key Findings
- Worst branch: Port Jefferson with 9.5% average delay.
- Visualized via bar chart with labeled delay percentages.

## How to Run
1. Ensure `pandas` and `matplotlib` are installed (`pip install pandas matplotlib`).
2. Place `lirr_otp.csv` in the same directory (download from [NY Data](https://data.ny.gov/Transportation/MTA-LIRR-On-Time-Performance-Beginning-2015/6kq9-5ikh)).
3. Run `python lirr_script.py`.

## Output
- Bar chart with delay percentages.
- Printed worst branch and delay value.
