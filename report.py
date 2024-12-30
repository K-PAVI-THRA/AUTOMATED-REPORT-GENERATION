import pandas as pd
from fpdf import FPDF

# Function to read and analyze data
def read_and_analyze_data(file_path):
    # Read data from CSV file
    df = pd.read_csv(file_path)
    
    # Analyze data
    total_sales = df['Sales'].sum()
    average_sales = df['Sales'].mean()
    max_sales = df.loc[df['Sales'].idxmax()]
    min_sales = df.loc[df['Sales'].idxmin()]
    
    # Prepare analysis results
    analysis_results = {
        "Total Sales": total_sales,
        "Average Sales": average_sales,
        "Highest Sales": max_sales['Name'] + " ($" + str(max_sales['Sales']) + ")",
        "Lowest Sales": min_sales['Name'] + " ($" + str(min_sales['Sales']) + ")"
    }
    
    return df, analysis_results

# Function to generate PDF report
def generate_pdf_report(analysis_results, df, output_file):
    # Create PDF instance
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title of the report
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Sales Data Report", ln=True, align="C")
    
    # Add a line break
    pdf.ln(10)
    
    # Add analysis summary
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt=f"Total Sales: ${analysis_results['Total Sales']}", ln=True)
    pdf.cell(200, 10, txt=f"Average Sales: ${analysis_results['Average Sales']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Highest Sales: {analysis_results['Highest Sales']}", ln=True)
    pdf.cell(200, 10, txt=f"Lowest Sales: {analysis_results['Lowest Sales']}", ln=True)
    
    # Add a line break
    pdf.ln(10)
    
    # Add detailed table of the sales data
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(50, 10, txt="Name", border=1, align="C")
    pdf.cell(50, 10, txt="Sales", border=1, align="C")
    pdf.cell(50, 10, txt="Region", border=1, align="C")
    pdf.cell(50, 10, txt="Date", border=1, align="C")
    pdf.ln()
    
    pdf.set_font('Arial', '', 12)
    for index, row in df.iterrows():
        pdf.cell(50, 10, txt=row['Name'], border=1, align="C")
        pdf.cell(50, 10, txt=str(row['Sales']), border=1, align="C")
        pdf.cell(50, 10, txt=row['Region'], border=1, align="C")
        pdf.cell(50, 10, txt=row['Date'], border=1, align="C")
        pdf.ln()
    
    # Output PDF to file
    pdf.output(output_file)

# Main function to execute the script
if __name__ == "__main__":
    # File path for CSV input and output PDF
    input_file = "sales_data.csv"
    output_pdf = "sales_report.pdf"
    
    # Read and analyze data
    df, analysis_results = read_and_analyze_data(input_file)
    
    # Generate the PDF report
    generate_pdf_report(analysis_results, df, output_pdf)
    
    print(f"Report generated successfully: {output_pdf}")
