# Install the required library
!pip install fpdf

import csv
from fpdf import FPDF
from google.colab import files
import io  

# Define a class for the PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Automated Report", border=False, ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def add_text(self, text):
        self.set_font("Arial", size=12)
        self.multi_cell(0, 10, text)
        self.ln(5)

# Function to read data from a CSV file
def read_data(file_content):
    try:
        # Decode the file content 
        decoded_content = file_content.decode('utf-8')
        reader = csv.DictReader(io.StringIO(decoded_content))  
        data = [row for row in reader]
        return data
    except UnicodeDecodeError:
        print("Error: Could not decode the file. Please ensure it's a CSV file with UTF-8 encoding.")
        return []  # Return an empty list if decoding fails

# Function to analyze data
def analyze_data(data):
    total_items = len(data)
    total_sales = sum(float(row.get("Sales", 0) or 0) for row in data)  
    average_sales = total_sales / total_items if total_items > 0 else 0

    return {
        "total_items": total_items,
        "total_sales": total_sales,
        "average_sales": average_sales,
    }

# Function to generate a PDF report
def generate_pdf_report(data, analysis, output_path):
    pdf = PDFReport()
    pdf.add_page()

    # Add analysis summary
    pdf.add_section_title("Analysis Summary")
    pdf.add_text(f"Total Items: {analysis['total_items']}")
    pdf.add_text(f"Total Sales: ${analysis['total_sales']:.2f}")
    pdf.add_text(f"Average Sales: ${analysis['average_sales']:.2f}")

    # Add data table
    pdf.add_section_title("Detailed Data")
    pdf.set_font("Arial", size=10)

    # Get the column names from the first row
    if data and isinstance(data[0], dict):  
        column_names = list(data[0].keys())  

        # Create table header with dynamic column names
        for column_name in column_names:
            pdf.cell(40, 10, column_name, border=1)
        pdf.ln()

        # Populate table rows with data
        for row in data:
            for column_name in column_names:
                pdf.cell(40, 10, str(row.get(column_name, "")), border=1)  
            pdf.ln()
    else:
        pdf.add_text("Error: Could not find data to create a table. Please check the CSV file format.")



    # Save the PDF
    pdf.output(output_path)

# Main script
if __name__ == "__main__":
    print("Please upload your CSV file:")
    uploaded = files.upload()

    for file_name, file_content in uploaded.items():
        # Read data and process it
        data = read_data(file_content)
        if data:  
            analysis = analyze_data(data)
            output_file = "report.pdf"
            generate_pdf_report(data, analysis, output_file)
            print(f"Report generated successfully: {output_file}")

            # Provide download link for the generated report
            files.download(output_file)
