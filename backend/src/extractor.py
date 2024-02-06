from pdf2image import convert_from_path
import pytesseract
import utils
from generic_precription import PrescriptionParser
from generic_patient_detail import PatientDetailParser
POPPLER_path=r"D:\poppler-23.11.0\Library\bin"
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Yatendra Pachori\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

def extract(file_path,file_format):
    pages = convert_from_path(file_path,poppler_path=POPPLER_path)
    document_text = ""
    if len(pages)>0:
        page=pages[0]
        processed_text = utils.processing_image(page)
        text = pytesseract.image_to_string(processed_text, lang='eng')
        document_text +=text
    # return document_text
    if file_format=='prescription':
        extracted_text=PrescriptionParser(document_text).parse()
    elif file_format=='patient':
        extracted_text=PatientDetailParser(document_text).parse()
    else:
        raise Exception(f"Invalid file format:{file_format}")
    return extracted_text

if __name__=='__main__':
    data= extract("D:/Project_Medical/backend/docs/patient_details/pd_2.pdf",'patient')
    print(data)