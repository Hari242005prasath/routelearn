import PyPDF2
import streamlit as st
from langchain_experimental.llms import ChatLlamaAPI
from llamaapi import LlamaAPI

# Configure GenerativeAI (replace with your API key)
llama = LlamaAPI("LL-QoWL9fXItXVpIn4aeAJrWF5ktefdgE5y6iBvV0sIbEgpd62qyKGbTi1fKkFfDnZh")
model = ChatLlamaAPI(client=llama)


def extract_text_from_pdf(file_path):
    """Extracts text from a PDF file, handling potential access errors."""
    try:
        with open(file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text
    except (FileNotFoundError, PermissionError) as e:
        st.error(f"Error: {e}. Please check the file path and permissions.")
        return ""


def create_study_plan(file_path_1, file_path_2):
    """Extracts text from two PDF files, then starts conversation with LLM."""
    extracted_text_1 = extract_text_from_pdf(file_path_1)
    extracted_text_2 = extract_text_from_pdf(file_path_2)

    calendar_part = extracted_text_1.split("Syllabus Content", 1) if "Syllabus Content" in extracted_text_1 else (
        extracted_text_1, "")
    syllabus_part = extracted_text_2

    convo = model.invoke(
        f"Academic Calendar Content \n {calendar_part} Syllabus Content\n {syllabus_part} Generate a study plan by analyzing the files. Provide a detailed schedule for each day with date and time, including specific chapter topics to cover and prioritizing important topics.")
    return convo.content


def main():
    st.title("Generate Study Plan from Two PDFs")
    st.write("Upload two PDFs - one for the academic calendar and one for the syllabus - and get a study plan generated.")

    file_path_1 = st.file_uploader("Upload Academic Calendar PDF", type="pdf")
    file_path_2 = st.file_uploader("Upload Syllabus PDF", type="pdf")

    if file_path_1 and file_path_2:
        study_plan = create_study_plan(file_path_1, file_path_2)
        st.subheader("Generated Study Plan:")
        st.write(study_plan)


if __name__ == "__main__":
    main()
