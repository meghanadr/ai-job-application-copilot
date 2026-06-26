from pypdf import PdfReader


def extract_text(uploaded_file):
    """
    Extract text from a PDF file.
    """

    reader = PdfReader(uploaded_file)

    resume_text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            resume_text += page_text + "\n"

    return resume_text