# README

## Overview

This script reads data from a CSV file and generates PDF reports for each row of data. Each report includes a logo image and a table with the data from the CSV file.

## Prerequisites

* Python 3.x
* Required Python packages (listed in [requirements.txt](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)):
  * pandas
  * reportlab

## Setup

1. **Clone the repository:**

   **git** **clone** **<**repository-ur**l**>

   **cd** **<**repository-director**y**>
2. **Create a virtual environment:**

   **python** **-m** **venv** **venv**
3. **Activate the virtual environment:**

   * On Windows:

     **venv\Scripts\activate**
   * On macOS/Linux:

     **source** **venv/bin/activate**
4. **Install the required packages:**

   **pip** **install** **-r** **requirements.txt**
5. **Place your CSV file and logo image in the same directory as the script:**

   * [data.csv](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)
   * [logo.png](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)

## Usage

1. **Run the script:**

   **python** **app.py**
2. **Output:**

   * The script will generate PDF reports named [report_1.pdf](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html), [report_2.pdf](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html), etc., for each row in the CSV file.

## CSV File Format

The CSV file ([data.csv](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html)) should have the following columns:

* `Sample Date`
* `Results Date`
* `HDL`
* `LDL`
* `Ratio`
* `Triglycerides`

## Customization

* **Logo Path:**
  * Update the [logo_path](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) variable in the script to point to your logo image if it's not named [logo.png](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html).
* **Table Data:**
  * Modify the [table_data](vscode-file://vscode-app/c:/Users/Mitsos_PC/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) list in the script to include or exclude any data fields as needed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
