# Streamlit PDF to Markdown  - GitHub Repository 
The Streamlit pdf to markdown project is designed to take one or more pdfs and transform them into a corresponding set of markdown files.

It assists users in preparing files for ingestion in Retrieval-Augmented Generation (RAG) workflows.

- This is currently an OCR-free approach.  
- Tables are handled reasonably well, though improvements will be made.  It is important to check the output manually to confirm there weren't any errors introduced.
- Images are excluded both from the final markdown file output and are not saved locally to the file.

This project will likely form part of a pipeline based approach to handle different types of pdfs in the future.

![image](https://github.com/headstrongpete/pdfmd/blob/main/pdfmarkdown.png)

This README provides step-by-step instructions for setting up and using the project on your local machine.

## Table of Contents
- [Branches](#Branches)
- [Installation](#Installation)
- [Usage](#Usage)
- [Issues](#Issues)
- [License](#License)

## Branches

### Main Branch

The [main](https://github.com/headstrongpete/pdfmd) branch of project is designed to run entirely on your local machine. This version of project doesn't rely on external API calls and offers greater control over your data. If you're looking for a self-contained solution, the `main` branch is the way to go.

### Cloud Branch
-TDB-

## Installation

To get started with the pdfmd project, you'll need to follow these installation steps:

1. Create a virtual environment and activate on your local machine to isolate the project's dependencies.  

Mac:
   ```bash
   python -m venv pdfmd-env
   source pdfmd-env/bin/activate
   ```
   
Windows:
   ```bash
   python -m venv pdfmd-env
   source venv/Scripts/activate
   ```

2. Navigate to the project directory, and clone the project repository.

   ```bash
   git clone https://github.com/headstrongpete/pdfmd.git
   ```

3. Install the required Python packages using `pip`.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Open your terminal and run the following command to start the project application:
   ```bash
   streamlit run app.py
   ```

2. You can now select an individual file or multiple files to convert as well as the folder location where you would like the newly transformed files to be saved.
3. Select Convert to initiate the transformation process.


## Issues

If you encounter any issues, have suggestions, or want to report a bug, please visit the [Issues](https://github.com/headstrongpete/pdfmd/issues) section of the project repository and create a new issue. Provide detailed information about the problem you're facing, and I'll do my best to assist you.

## License

This project is licensed under the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). For details, see the [LICENSE](LICENSE) file..

