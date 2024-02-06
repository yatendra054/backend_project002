import re
from backend.src.generic_parser import MedicalDocParser

class PrescriptionParser(MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)
    def parse(self):
        return {
            "patient_name":self.get_field('patient_name'),
            "patient_address":self.get_field('patient_address'),
            # "direction":self.get_direction(),
            "directions":self.get_field('directions'),
            "Phone_number":self.get_field('Phone_number')
        }

    def get_field(self,field_name):
        pattern_dic={
            'patient_name':{'pattern':'Name:(.*) .?','flags':0},
            'patient_address': {'pattern': 'Address:(.*)', 'flags': 0},
            'directions': {'pattern': 'Directions:(.*)Refill', 'flags': re.DOTALL},
            'Phone_number': {'pattern': '\(\d{3}\)-\d{3}-\d{4}', 'flags': 0}
        }
        pattern_object=pattern_dic.get(field_name)
        if pattern_object:
            matches=re.findall(pattern_object['pattern'],self.text,pattern_object['flags'])
            if len(matches)>0:
                return matches[0].strip()

if __name__ == '__main__':
     document_text ='''Dr John Smith, M.D
2 Non-Important Street,
New Yark, Phone (000)-121-2222

Name: Virat Kohli ate 2/05/2022

Address: 2 cricket bivd, New Delhi

Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times'''
     par = PrescriptionParser(document_text)
     print(par.parse())