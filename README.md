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
appnope==0.1.4
asttokens==2.4.1
attrs==24.2.0
certifi==2024.8.30
charset-normalizer==3.4.0
comm==0.2.2
contourpy==1.3.0
cycler==0.12.1
debugpy==1.8.7
decorator==5.1.1
executing==2.1.0
fastjsonschema==2.20.0
fonttools==4.54.1
idna==3.10
ipykernel==6.29.5
ipython==8.29.0
jedi==0.19.1
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
jupyter_client==8.6.3
jupyter_core==5.7.2
kiwisolver==1.4.7
matplotlib==3.9.2
matplotlib-inline==0.1.7
nbformat==5.10.4
nest-asyncio==1.6.0
numpy==2.1.3
packaging==24.1
pandas==2.2.3
parso==0.8.4
patsy==0.5.6
pexpect==4.9.0
pillow==11.0.0
platformdirs==4.3.6
plotly==5.24.1
prompt_toolkit==3.0.48
psutil==6.1.0
ptyprocess==0.7.0
pure_eval==0.2.3
Pygments==2.18.0
pyparsing==3.2.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.2
pyzmq==26.2.0
referencing==0.35.1
requests==2.32.3
rpds-py==0.21.0
scipy==1.14.1
seaborn==0.13.2
six==1.16.0
stack-data==0.6.3
statsmodels==0.14.4
tenacity==9.0.0
tornado==6.4.1
traitlets==5.14.3
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
wcwidth==0.2.13

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
