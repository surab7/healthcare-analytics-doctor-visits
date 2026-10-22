# Healthcare Analytics for Doctor Visits

A student data analytics project exploring patterns associated with doctor visits using a dataset of 5,190 records and 13 columns.

## Project objective
Explore how doctor visits vary across patient characteristics, illness burden, chronic-condition indicators, and healthcare-support indicators. This is descriptive analysis; it does not establish causation or provide medical advice.

## Dataset
- **File:** `data/healthcare_doctor_visits.csv`
- **Rows:** 5,190
- **Columns:** 13
- **Target column:** `visits` — number of doctor visits during the period covered by the dataset.
- `Unnamed: 0` is a record identifier and should not be treated as a health measurement.
- See `data/Dataset_Explanation.docx` for the supplied column guide.

> **Privacy and licensing:** Before making this repository public, confirm that you are allowed to redistribute the dataset and its documentation. Do not upload any personally identifiable or confidential health information. If redistribution is not permitted, remove the CSV and guide from the public repository and explain how authorized users can obtain the data.

## Key findings from the supplied dataset
- 5,190 records and 13 columns were analyzed.
- 4,141 records (about 79.8%) have `visits = 0`; 20.2% have one or more visits.
- Mean visits per record: about 0.302.
- Average visits rise with reported illness count in the observed data: approximately 0.08 for 0 illnesses and 0.81 for 5 illnesses.
- These are descriptive associations. Differences may reflect multiple factors and should not be interpreted as causal effects.

## Tools
- Python
- pandas
- matplotlib
- Jupyter Notebook

## Run the analysis
1. Install Python 3.10+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
4. Open `notebooks/healthcare_doctor_visits_analysis.ipynb` and run the cells.

## Repository structure
```text
healthcare-analytics-doctor-visits/
├── README.md
├── requirements.txt
├── TIRTC_DIY_Healthcare_Analytics_Completed.pptx
├── data/
│   ├── healthcare_doctor_visits.csv
│   └── Dataset_Explanation.docx
└── notebooks/
    └── healthcare_doctor_visits_analysis.ipynb
```

## Limitations
- The dataset documentation describes the fields, but does not fully specify the sampling design or observation period.
- `age` is stored as a numeric/decimal value; confirm the original coding before interpreting it as years.
- Results are descriptive and do not establish cause and effect.
- This project is for learning and portfolio demonstration, not clinical decision-making.
