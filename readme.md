# Automated PDF Report Generator

This project automates the creation of personalized PDF reports by extracting data from a CSV file. It utilizes the `pandas` library for data manipulation and `reportlab` for generating PDF documents.

## Table of Contents

- [Automated PDF Report Generator](#automated-pdf-report-generator)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data Format](#data-format)
    - [Patient Information](#patient-information)
    - [Examination Information](#examination-information)
    - [Sample `data.csv` Format](#sample-datacsv-format)
  - [Customization](#customization)
  - [Example](#example)

## Features

* Generates individualized PDF reports for each patient record in the CSV file.
* Includes a customizable logo in the reports.
* Displays patient information and examination results in a structured format.
* Supports up to 6 examinations per report (modifiable in the script).

## Requirements

* Python 3.x
* Libraries:
  * `pandas`
  * `reportlab`

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/pdf-report-generator.git
cd pdf-report-generator
```

2. **Install the required packages:**

```python
pip install pandas reportlab
```

## Usage

1. **Prepare your data:**

   * Create a `data.csv` file with the required data fields (see [Data Format](#data-format) for details).
   * Place your logo image in the project directory and ensure it's named `LOGO.PNG`. If it's named differently or located elsewhere, update the `logo_path` variable in the script accordingly.
2. **Run the script:**

```python
app.py 
```

* The script will generate PDF reports named `report_1.pdf`, `report_2.pdf`, etc., corresponding to each row in your `data.csv` file.

## Data Format

The `data.csv` file should contain the following columns:

### Patient Information

* `Patient Name`
* `Gender`
* `Date of Birth`
* `Report Date`
* `Execution ID`
* `Sample Date`

### Examination Information

For each examination (up to 6), include:

* `LOINC Code 1`, `Exam Name 1`, `Result 1`, `Unit 1`, `Reference Values 1`, `Method 1`
* `LOINC Code 2`, `Exam Name 2`, `Result 2`, `Unit 2`, `Reference Values 2`, `Method 2`
* ...
* `LOINC Code 6`, `Exam Name 6`, `Result 6`, `Unit 6`, `Reference Values 6`, `Method 6`

**Note:** If a patient has fewer than 6 examinations, leave the unused columns blank but ensure all headers are present.

### Sample `data.csv` Format

```csv
Patient Name,Gender,Date of Birth,Report Date,Execution ID,Sample Date,LOINC Code 1,Exam Name 1,Result 1,Unit 1,Reference Values 1,Method 1,LOINC Code 2,Exam Name 2,Result 2,Unit 2,Reference Values 2,Method 2,LOINC Code 3,Exam Name 3,Result 3,Unit 3,Reference Values 3,Method 3,LOINC Code 4,Exam Name 4,Result 4,Unit 4,Reference Values 4,Method 4,LOINC Code 5,Exam Name 5,Result 5,Unit 5,Reference Values 5,Method 5,LOINC Code 6,Exam Name 6,Result 6,Unit 6,Reference Values 6,Method 6
John Doe,Male,1980-01-01,2023-10-01,123456,2023-09-30,2345-7,Complete Blood Count,Normal,,Normal Range,Hematology,3456-8,Blood Sugar,90,mg/dL,70-99,Enzymatic,,,,,,,,,,,,,,,,,,,,,
Jane Smith,Female,1990-05-15,2023-10-01,789012,2023-09-30,4567-8,Cholesterol,180,mg/dL,<200,Chemical Analysis,,,,,,,,,,,,,,,,,,,,,,,,,
```

## Customization

* **Adjusting the Number of Examinations:**

  * The script currently supports up to 6 examinations per patient.
  * To modify this, change the range in the following loop:

    ```python
    for i in range(1, 7):  # Adjust the range as needed
        # Examination data processing
    ```
* **Changing the Logo:**

  * Replace `LOGO.PNG` with your own logo image.
  * Update the `logo_path` variable in the script if the file name or location changes.

  ```python
  logo_path = 'your_logo.png'  # Update with your logo's file name
  ```
* **Modifying Report Styles:**

  * The report's appearance is defined using `TableStyle` and `getSampleStyleSheet`.
  * Customize fonts, colors, and layouts by editing these styles in the script.

## Example

1. **Create `data.csv`:**

   ```csv
   Patient Name,Gender,Date of Birth,Report Date,Execution ID,Sample Date,LOINC Code 1,Exam Name 1,Result 1,Unit 1,Reference Values 1,Method 1
   Alice Johnson,Female,1985-07-22,2023-10-05,654321,2023-10-04,7890-1,Vitamin D,30,ng/mL,20-50,Immunoassay
   ```
2. **Place Logo Image:**

   * Save your logo as `LOGO.PNG` in the project directory.
3. **Run the Script:**

```bash
python report_generator.py
```

1. **Output:**
   * `report_1.pdf` is generated, containing Alice Johnson's report with the logo, patient information, and examination results.
