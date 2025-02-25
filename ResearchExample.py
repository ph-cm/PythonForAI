#Example: Research paper summarizer and keyword extractor
    #lib requirements:
    # annotated-types==0.7.0
    # anyio==4.4.0
    # certifi==2024.8.30
    # distro==1.9.0
    # h11==0.14.0
    # httpcore==1.0.5
    # httpx==0.27.2
    # idna==3.8
    # jiter==0.5.0
    # openai==1.43.1
    # pydantic==2.9.0
    # pydantic_core==2.23.2
    # PyMuPDF==1.24.10
    # PyMuPDFb==1.24.10
    # setuptools==72.1.0
    # sniffio==1.3.1
    # tqdm==4.66.5
    # typing_extensions==4.12.2
    # tzdata==2024.1
    # wheel==0.43.0
    # Create an .txt file that has this versions and do the pip install of that file

import fitz #PyMuPDF allow us to extract PDFs
import openai
import sys

#Set up my OpenAI API key
openai.api_key = "key-open-ai"
#function to read the first page of a PDF
def extract_abstract(pdf_path):
    #Open the PDF file and grab text from the 1rs page
    with fitz.open(pdf_path) as pdf:
        first_page = pdf[0]
        text = first_page.get_text("text")
    
    #Extract the abstract assuming the abstract starts with "Abstract")
    #find where abstract starts
    start_idx = text.lower().find('abstract')
    
    #end abstract at introduction if it exists on 1st page
    if 'introduction' in text.lower():
        end_idx = text.lower().find('introduction')
    else:
        end_idx = None
    
    #extract abstract text
    abstract = text[start_idx:end_idx].strip()
    
    #if abstract appears on 1st page return it, if not return none
    if start_idx != -1:
        return abstract
    else:
        return None
    
#Function to summarize the abstract and generate keywords using OpenAI API
def summarize_and_generate_keywords(abstract):
    #Use OpenAI Chat completions API to summarize and generate keywords
    prompt = f"Summarize the following pape abstract and generate (no more than 5) keywords:\n\n{abstract}"
    
    #Make API call
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system", "content":"You are a helpful assistant."},
            {"role":"user", "content": prompt}
        ],
        temperature=0.25
    )
    
    #extract response
    summary = response.choices[0].message.content
    return summary

#Bring all together
#Get the PDF path from the command-line args
pdf_path = sys.argv[1]

#Extract abstract from the PDF
abstract = extract_abstract(pdf_path)

#if abstract exists on first page summary
if abstract:
    #Summarize and generate keywords
    summary = summarize_and_generate_keywords(abstract)
    
    print(summary)
else:
    print("Abstract not found on the first page")
