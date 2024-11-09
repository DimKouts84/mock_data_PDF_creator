import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Spacer
from reportlab.lib import colors
from reportlab.lib.units import inch
import os
# Read data from CSV file
data = pd.read_csv('data.csv')

# Path to logo image
logo_path = 'logo.png' # Replace with your logo image path

# Check if logo image exists
if not os.path.isfile(logo_path):
    print(f"Logo image not found at {logo_path}")
    exit(1)

# Iterate over each row in the DataFrame
for index, row in data.iterrows():
    # Create PDF document
    
    filename = f'report_{index + 1}.pdf'
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    
    
    # Add logo image
    im = Image(logo_path, width=2*inch, height=2*inch)
    elements.append(im)
    elements.append(Spacer(1, 0.25*inch))
    
    
    # Prepare table data
    table_data = [
        ['Sample Date', str(row['Sample Date'])],
        ['Results Date', str(row['Results Date'])],
        ['HDL', str(row['HDL'])],
        ['LDL', str(row['LDL'])],
        ['Ratio', str(row['Ratio'])],
        ['Triglycerides', str(row['Triglycerides'])]
    ]
    
    # Create Table
    table = Table(table_data, colWidths=[2*inch, 4*inch])
    
    # Add style to table
    style = TableStyle([
        ('GRID', (0,0), (-1,-1), 1, colors.black),
        ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
        ('FONTSIZE', (0,0), (-1,-1), 12),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
    ])
    table.setStyle(style)
    elements.append(table)
    
    # Build PDF
    doc.build(elements)

    print(f"Created {filename}")