import re
from backend.src.generic_parser import MedicalDocParser

class PatientDetailParser (MedicalDocParser):
    def __init__(self,text):
        MedicalDocParser.__init__(self,text)

    def parse(self):
        return{
            "patient_name":self.get_patient_name(),
            "hepatitis_b_vaccination":self.get_hepatitis_b_vaccination(),
            "medical_problem":self.get_medical_problem(),
            "patient_phoneNo.":self.get_patient_phoneNo()
        }
    def get_patient_name(self):
        pattern='Patient Information(.*?)\(\d{3}\)'
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        name=''
        if matches:
            name=self.remove_noise(matches[0])
        return name
    def remove_noise(self,name):
        name = name.replace('Birth Date', '').strip()
        date_pattern = '((Jan|Feb|March|April|May|June|July|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
        date_matches = re.findall(date_pattern, name)
        if date_matches:
            date = date_matches[0][0]
            name = name.replace(date, '').strip()
        return name
    def get_hepatitis_b_vaccination(self):
        pattern='Have you had the Hepatitis B vaccination\?.*(Yes|No)'
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        if matches:
            return matches[0].strip()
    def get_medical_problem(self):
        pattern='List any Medical Problems .*?:(.*)'
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        if matches:
            return matches[0].strip()
    def get_patient_phoneNo(self):
        pattern='Patient Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
        matches=re.findall(pattern,self.text,flags=re.DOTALL)
        if matches:
            return matches[0][-1]




if __name__ == '__main__':
      document_text='''47/12/2020

Patient Medical Record

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight
9264 Ash Dr 95
New York City, 10005 .
United States Height:
190
In Case of Emergency
m _ a _
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone
Genera! Medical History
. : a ee

Chicken Pox (Varicella):

IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):
Migraine
'''
      par=PatientDetailParser(document_text)
      print(par.parse())