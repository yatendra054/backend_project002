import pytest
from backend.src.generic_patient_detail import PatientDetailParser

@pytest.fixture()
def doc_1():
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
Migraine'''
    return PatientDetailParser(document_text)
def test_get_details(doc_1):
    # assert doc_1.get_patient_name()=='Kathy Crawford'
    record_1=doc_1.parse()
    assert record_1 == {
        'patient_name':'Kathy Crawford',
        'medical_problem': 'Migraine',
        'patient_phoneNo.':'(737) 988-0851',
        'hepatitis_b_vaccination':'No'

    }