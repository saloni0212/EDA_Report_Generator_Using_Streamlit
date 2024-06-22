# EDA_Report_Generator_Using_Streamlit
The EDA Report Generator is a Python-based application designed to automate the process EDA. Built using Streamlit, a popular open-source framework for creating interactive web applications this tool simplifies and accelerates the process of data exploration, providing users with insightful visualizations and summary statistics with minimal effort.

## Features

- Upload CSV files to analyze your data.
- Generate a detailed Pandas Profiling report.
- Use an example dataset to see the app in action.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/saloni0212/eda-app.git
    cd eda-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Ensure that the `visions` package is installed with a compatible version for `ydata-profiling`:

    ```sh
    pip install visions>=0.7.5,<0.7.7
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run app.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.
