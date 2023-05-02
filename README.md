# Google Top Trends

A simple Python script to fetch the top 3 trending searches on Google for a specified country using the Google Trends API.

## Requirements

- Python 3.6 or higher
- `requests` library
- `pycountry` library

## Installation

Install the required packages:

```sh
pip install -r requirements.txt
```

## Usage
``` bash
python top_trends.py <COUNTRY_CODE>
```
For example, to fetch the top 3 trends in Canada:
```sh
python top_trends.py CA
```
The script will output the top 3 trending searches in the specified country, separated by commas.

## Note
Please ensure you provide a valid 2-letter ISO 3166-1 alpha-2 country code, or the script will display an error message.
