import streamlit as st
import pathlib
import pymupdf4llm
from pathlib import Path
import os

# Function to convert a single PDF file to Markdown
def convert_pdf_to_md(pdf_path, output_path):
    md_text_list = pymupdf4llm.to_markdown(pdf_path, page_chunks=True)
    md_text = "\n".join(item['text'] for item in md_text_list if 'text' in item)
    output_file = Path(output_path) / (Path(pdf_path).stem + ".md")
    output_file.write_bytes(md_text.encode())

# Streamlit app
st.set_page_config(
    layout='centered',
    page_title='Just Good enough PDF to Markdown Utility',
    menu_items={
        'about': '''**🏆 Just Good enough PDF to Markdown Utility -  v24.10.03**        
       Hand rolled by Peter Squires, unimaginably improved by ChatGPT 4.o

        streamlit / pathlib / pymupdf4llm   
        '''
    }
)

st.title("PDF to Markdown Converter")

option = st.selectbox(
    "Select conversion mode:",
    ("Select Individual PDF", "Select Folder of PDFs")
)

if option == "Select Individual PDF":
    pdf_file = st.file_uploader("Choose a PDF file", type="pdf")
    if pdf_file:
        output_dir = st.text_input("Enter the output directory:", value=str(Path.home()))
        if st.button("Convert"):
            pdf_path = Path(pdf_file.name)
            pdf_path.write_bytes(pdf_file.read())  # Save the uploaded file
            convert_pdf_to_md(pdf_path, output_dir)
            st.success(f"Converted {pdf_file.name} to Markdown successfully!")
elif option == "Select Folder of PDFs":
    folder_path = st.text_input("Enter the folder path containing PDFs:")
    output_dir = st.text_input("Enter the output directory:", value=str(Path.home()))
    if st.button("Convert All PDFs"):
        pdf_files = list(Path(folder_path).glob("*.pdf"))
        if not pdf_files:
            st.error("No PDF files found in the specified folder.")
        else:
            for pdf_file in pdf_files:
                convert_pdf_to_md(pdf_file, output_dir)
            st.success("Converted all PDFs in the folder to Markdown successfully!")

# Run the Streamlit app with: streamlit run app.py