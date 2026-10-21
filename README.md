# Sales Data Analyzer Dashboard

## Overview

The Sales Data Analyzer Dashboard is a Python-based project that analyzes sales data and presents useful business insights through an interactive dashboard.

## Features

- Load sales data from an Excel file.
- Process and analyze sales records using Python and Pandas.
- Explore sales performance and trends.
- Visualize sales insights through an interactive dashboard.
- Use SQL queries and MySQL connectivity for data retrieval and analysis.

## Technologies Used

- Python
- Pandas
- Streamlit
- MySQL
- SQL
- Microsoft Excel

## Project Structure

```text
sales-data-analyzer-dashboard/
├── app.py
├── data/
│   └── sales_data.xlsx
├── analysis.py
├── load_data.py
├── queries.sql
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project directory:

   ```bash
   cd sales-data-analyzer-dashboard
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment on Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Dashboard

Run the following command from the project root directory:

```bash
streamlit run app.py
```

## Dataset

The project uses a sales dataset stored in the `data/` directory for data processing and analysis.

## Author

Sri Harini S
