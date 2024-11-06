# NASA APOD Data Analysis

This repository contains code to fetch, analyze, and store data from NASA's Astronomy Picture of the Day (APOD) API. It uses Python, NumPy, and other libraries to perform various operations on the data.

## Prerequisites

Before running the application, ensure that you have the following installed on your system:

- Python 3.x (preferably 3.7 or later)
- `pip` (Python package installer)

You can check if Python and pip are installed by running the following commands in your terminal:

```bash
python --version
pip --version
```

## Setting up the Environment

### Step 1: Clone the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/shuvo-dotcom/NASA-APOD-Data-Analysis
cd NASA-APOD-Data-Analysis
```

### Step 2: Create a Virtual Environment

It's a good practice to use a virtual environment to manage dependencies:

```bash
python -m venv caenv
```

Activate the virtual environment:

- On macOS/Linux:

```bash
source caenv/bin/activate
```

- On Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should include the following libraries:

```
requests
numpy
python-dotenv
pandas
matplotlib
```

### Step 4: Configure Environment Variables

In order to use the NASA APOD API, you will need an API key. Follow the steps below to set it up:

1. Visit [NASA's API Portal](https://api.nasa.gov) and sign up for an API key if you don't already have one.
2. Once you have the API key, create a `.env` file in the root of the repository and add your API key like so:

```
API_KEY=your_nasa_api_key
NASA_APOD_URL=https://api.nasa.gov/planetary/apod
JSON_FILE_NAME=apod_data.json
CSV_FILE_NAME=apod_summary.csv
```

### Step 5: Run the Application

You can now run the application. For example, to fetch data from the APOD API and store it in a JSON file, run:

```bash
python src/__init__.py
```

## Usage

1. **Fetching Data**: The code will fetch the APOD data for the given date range and store the results in a file defined by the `JSON_FILE_NAME` variable (e.g., `apod_data.json`).

2. **Analysis**: After fetching the data, the program will perform various statistical operations like calculating the mean, standard deviation, variance, and median of the data.

3. **Saving Results**: The results will be saved in a JSON file, and a CSV summary (`apod_summary.csv`) will be generated.

## Troubleshooting

- **Error: `AttributeError: 'numpy.random._generator.Generator' object has no attribute 'capsule'`**

  This error occurs when trying to use a `numpy.random.Generator` incorrectly. Make sure you are using the correct version of NumPy and follow the instructions carefully to create the custom generator.

- **Error: `ModuleNotFoundError: No module named 'dotenv'`**

  This error occurs if the `python-dotenv` package is not installed. You can fix it by installing the necessary dependencies using `pip install -r requirements.txt`.

## Contributing

Feel free to fork this repository, make changes, and create a pull request. We welcome contributions from the community.
