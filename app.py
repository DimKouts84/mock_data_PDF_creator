import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
import os

# Load data from CSV
data = pd.read_csv('data.csv')

# Path to logo image
logo_path = 'LOGO.PNG'  # Replace with the path to your logo image

# Check if logo image exists
if not os.path.isfile(logo_path):
    print(f"Logo image not found at {logo_path}")
    exit(1)

# Define report style
styles = getSampleStyleSheet()

# Iterate over each row in the DataFrame to create individual reports
for index, row in data.iterrows():
    # Create PDF document
    filename = f'report_{index + 1}.pdf'
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Add logo
    im = Image(logo_path, width=2*inch, height=2*inch)
    
    # Add Patient and Report Information
    report_info = [
        ["Patient Name:", row['Patient Name']],
        ["Gender:", row['Gender']],
        ["Date of Birth:", row['Date of Birth']],
        ["Report Date:", row['Report Date']],
        ["Execution ID:", row['Execution ID']],
        ["Sample Date:", row['Sample Date']]
    ]
    report_table = Table(report_info, colWidths=[2*inch, 3*inch])
    report_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 9),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))

    # Combine logo and report_info into a single table
    combined_table = Table([[im, report_table]], colWidths=[2*inch, 5*inch])
    combined_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (0, 0), 'CENTER'),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (1, 0), (1, 0), 'CENTER'),
        ('ALIGN', (0, 0), (0, 0), 'CENTER')
        
    ]))

    elements.append(combined_table)
    elements.append(Spacer(0.5, 0.20*inch))

    # Add Examination Information
    exam_info = [
        ["LOINC Code", "Exam Name", "Result", "Unit", "Reference Values", "Method"]
    ]
    
    # Add each exam as a row in the exam_info table
    for i in range(1, 7):  # Assuming up to 5 exams per report, adjust as needed
        exam_info.append([
            row[f'LOINC Code {i}'],
            row[f'Exam Name {i}'],
            row[f'Result {i}'],
            row[f'Unit {i}'],
            row[f'Reference Values {i}'],
            row[f'Method {i}']
        ])

    exam_table = Table(exam_info, colWidths=[0.85*inch, 2.1*inch, 0.85*inch, 0.65*inch, 1.50*inch, 1.05*inch])
    exam_table.setStyle(TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightblue),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ALIGN', (0,0), (-1,-1), 'LEFT')
    ]))
    elements.append(exam_table)

    # Build PDF
    doc.build(elements)
    print(f"Created {filename}")
