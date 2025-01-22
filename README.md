# AUTOMATED-REPORT-GENERATION

*COMPANY:* CodTech IT Solutions

*NAME:* A Jenita Roselin

*INTERN ID:* CT08FYS

*DOMAIN:* Python Programming

*DURATION:* 4 weeks

*MENTOR:* Neela Santhosh Kumar

# *Task Description: Developing a Script for CSV Data Analysis and PDF Report Generation:*

This task involved creating a Python script that read data from a CSV file, analyzing the data, and generating a formatted PDF report using the FPDF library. The goal was to automate the process of data reporting by taking raw data, processing it, and producing a user-friendly output document.

This script turns raw data into useful insights and presents them in a clear way. It used Python programming language to read a CSV file, figure out important numbers, and create a neat PDF report. This makes it perfect for things like checking sales, summarizing inventory, or tracking performance quickly and easily.

*Input Requirements*

The script expects a CSV file as its input. The CSV file should:
  Use UTF-8 encoding.
  Contain column headers.
  Include at least one numeric column for analysis (e.g., a “Sales” column).
Users are to upload the file, which will then read and processed to extract relevant information. Any issues with file decoding or missing columns are handled, with appropriate error messages.

*Features and Functionalities*

The script is composed of:
  Data Reading:
    The uploaded CSV file is read using Python’s csv.DictReader. The script then converts each row into a dictionary for easy data manipulation.
  
  Data Analysis:
    The script calculates key metrics from the dataset:
      Total Items: The total number of rows in the CSV file.
      Total Sales: The sum of all values in the “Sales” column.
      Average Sales: The mean value of the “Sales” column.

  PDF Report Generation:
    The FPDF library was used to create a PDF document with the following sections:
      Header and Footer: A consistent header with the title "Automated Report" and a footer showing the page number.
      Analysis Summary: A concise summary of the calculated metrics.
      Detailed Data Table: A table displaying all rows and columns from the CSV file. Column headers are dynamically generated based on the data.

*Output*

The generated PDF report includes:
  A title and page numbering for a professional appearance.
  An “Analysis Summary” section with calculated metrics.
  A “Detailed Data” section, showcasing the full dataset in tabular format.

If the CSV file contained invalid or missing data, the script includes error messages in the report.

*Libraries Used*

FPDF: For creating the PDF document with sections, text, and tables.
csv: For reading and parsing the CSV file.
io: For handling in-memory file operations.
google.colab.files: For uploading and downloading files in a Google Colab environment.

*Execution Flow*

The script prompts the user to upload a CSV file.
It reads the file, converting its contents into a list of dictionaries.
Data is analyzed to compute total items, total sales, and average sales.
The PDF report is generated with the analysis summary and detailed data table.
The script saves the PDF and provides a download link for the user.

*Output Screenshots*

![Image](https://github.com/user-attachments/assets/d6e2d832-f305-4d65-bfae-40670d436c18)

![Image](https://github.com/user-attachments/assets/78e9c51b-8ad5-4b84-83b7-96450556b798)

![Image](https://github.com/user-attachments/assets/05462712-0d12-48f8-860d-be5b4ce3b91a)

![Image](https://github.com/user-attachments/assets/3953b81d-0cc8-42a2-a7df-edd9cc6faf80)

![Image](https://github.com/user-attachments/assets/7ebe3a50-8b9f-411d-a49e-e1591c70ffa3)

*Conclusion*

This script automates the process of reading data, performing analysis, and creating a well-structured PDF report. It demonstrates the practical application of Python’s libraries in real-world scenarios, streamlining workflows and improving productivity.
