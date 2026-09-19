# Energy Waste Analyzer for Labs

A Streamlit-based web application that analyzes electricity usage in laboratory equipment and helps identify energy waste through interactive charts and cost analysis.

## Features

- Calculate energy consumption (kWh)
- Estimate electricity cost
- Visualize usage with Plotly charts
- Analyze computers, fans, and lights
- Simple and interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly

## Project Structure

EnergyWasteAnalyzerForLabs/
├── app.py
├── requirements.txt
├── assets/
├── data/
├── images/
└── utils/

## How to Run

1. Install the required libraries:

```bash
pip install -r requirements.txt
```

2. Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.