import pandas as pd
from fpdf import FPDF
import os

# Create a sample CSV file if it doesn't exist
sample_file = "sales_data.csv"
if not os.path.exists(sample_file):
    sample_data = """Product,Sales
Apples,1200
Bananas,800
Cherries,1500
Dates,600
Elderberries,950
"""
    with open(sample_file, "w") as f:
        f.write(sample_data)
    print(f"Sample data file '{sample_file}' created.")

# Read data from the CSV file
data = pd.read_csv(sample_file)

# Analyze the data
total_sales = data['Sales'].sum()
average_sales = data['Sales'].mean()
top_product_row = data.loc[data['Sales'].idxmax()]
top_product = top_product_row['Product']

# Generate a formatted PDF report using FPDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 18)
pdf.cell(200, 10, txt="Company Sales Report", ln=True, align="C")

pdf.set_font("Arial", size=12)
pdf.ln(10)
pdf.multi_cell(0, 10, f"Total Sales: {total_sales}")
pdf.multi_cell(0, 10, f"Average Sales: {average_sales:.2f}")
pdf.multi_cell(0, 10, f"Top Product: {top_product}")

pdf.ln(10)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "Sales Breakdown:", ln=True)

pdf.set_font("Arial", size=11)
for index, row in data.iterrows():
    pdf.multi_cell(0, 8, f"{row['Product']}: {row['Sales']}")

pdf.ln(10)
pdf.set_font("Arial", 'I', 10)
pdf.multi_cell(0, 8, "Report generated automatically using Python and FPDF.")

# Save the PDF
output_file = "sales_report.pdf"
pdf.output(output_file)
print(f"Report generated successfully as {output_file}")
