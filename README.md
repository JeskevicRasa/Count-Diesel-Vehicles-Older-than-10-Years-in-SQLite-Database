# Autopark Selection Task

This project contains a Python script that connects to an SQLite database and selects diesel vehicles that are older than 10 years. The script calculates the total count of such vehicles and displays the result.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

- Python 3.x installed
- CSV file containing data of vehicles registered in Lithuania from an open data source: https://www.regitra.lt/lt/paslaugos/duomenu-teikimas/atviri-duomenys-1/transporto-priemones-3


## Installation

1. Clone this GitHub repository to your local machine.
2. Navigate to the project directory.

## Usage

1. Update the `csv_file` variable in the script (`csv_to_db.py`) with the correct path to csv file.

2. Run the `csv_to_db.py` Python file. Database will be created.

3. Run the `selection.py` file.

4. The script will connect to the database, execute the query, and display the total count of diesel vehicles older than 10 years.




