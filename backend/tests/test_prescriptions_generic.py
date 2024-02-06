from backend.src.generic_precription import PrescriptionParser
import pytest


@pytest.fixture()
def doc_1_maria():
    document_text = '''Dr John Smith, M.D
    2 Non-Important Street, |
    New York, Phone (000)-111-2222

    Name: Marta Sharapova Date: 5/11/2022 _

    Address: 9 tennis court, new Russia, DC

    Prednisone 20 mg
    Lialda 2.4 gram

    Directions: Prednisone, Taper 5 mg every 3 days,

    Finish in 2.5 weeks . -
    Lialda - take 2 pill everyday for 1 month —

    , ‘Refill: 2_times'''

    return PrescriptionParser(document_text)

def test_get_name(doc_1_maria):
    assert doc_1_maria.get_field('patient_name') == 'Marta Sharapova'
#     record_virat =  doc_2_virat.parse()
#     assert record_virat == {
#         'patient_name': 'Virat Kohli',
#         'patient_address': '2 cricket blvd, New Delhi',
#         'medicines': 'Omeprazole 40 mg',
#         'directions': 'Use two tablets daily for three months',
#         'refills': '3'
#     }

def test_get_address(doc_1_maria):
    assert doc_1_maria.get_field('patient_address') == '9 tennis court, new Russia, DC'
