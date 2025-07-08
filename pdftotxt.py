import PyPDF2
import os
import sys

def pdf_to_txt(pdf_path, txt_path=None):
    """
    Convert a PDF file to a text file.
    
    Args:
        pdf_path (str): Path to the input PDF file
        txt_path (str, optional): Path for the output text file. 
                                 If None, creates a .txt file with same name as PDF
    
    Returns:
        str: Path to the created text file
    """
    try:
        # Generate output filename if not provided
        if txt_path is None:
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
            txt_path = f"{base_name}.txt"
        
        # Open and read the PDF file
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Extract text from all pages
            text_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text_content += page.extract_text() + "\n"
        
        # Write the extracted text to a text file
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)
        
        print(f"Successfully converted '{pdf_path}' to '{txt_path}'")
        return txt_path
        
    except FileNotFoundError:
        print(f"Error: PDF file '{pdf_path}' not found.")
        return None
    except Exception as e:
        print(f"Error during conversion: {str(e)}")
        return None

def main():
    """
    Main function to handle command line arguments or interactive input.
    """
    if len(sys.argv) > 1:
        # Use command line argument
        pdf_file = sys.argv[1]
    else:
        # Interactive input
        pdf_file = input("Enter the path to the PDF file: ").strip()
    
    # Check if file exists
    if not os.path.exists(pdf_file):
        print(f"Error: File '{pdf_file}' does not exist.")
        return
    
    # Convert PDF to text
    result = pdf_to_txt(pdf_file)
    
    if result:
        print(f"Text file saved in current directory: {os.path.abspath(result)}")

if __name__ == "__main__":
    main()