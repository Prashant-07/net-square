# from unittest.mock import patch
from bill_calculator.bill_calculator import FareController
import unittest

class TestBillCalculator(unittest.TestCase):
    def test_non_existing_file(self):
        expected_response = {'success': False, 'message': "File not found in the given path"}
        response = FareController("non-existent-file.txt").process_ledger()
        self.assertEqual(response, expected_response)
    
    def test_empty_file(self):
        expected_response = {'success': True, 'message': "Processed all the records"}
        self.assertEqual(FareController("test_files/blank.txt").process_ledger(), expected_response)
    
    def test_ledger_processing_on_valid_file(self):
        expected_response = {'success': True, 'message': "Processed all the records"}
        self.assertEqual(FareController("test_files/sample_log.txt").process_ledger(), expected_response)
    
    def test_billing_response_on_sample_logs(self):
        expected_response = {'success': True, 'data': ['ALICE99 4 240', 'CHARLIE 3 38', 'JJJJJJJ 1 159', 'sss4544 1 0']}
        obj = FareController("test_files/sample_log.txt")
        obj.process_ledger()
        billing_response = obj.get_final_billing()
        self.assertEqual(billing_response, expected_response)

    def test_billing_response_on_corrupted_logs(self):
        expected_response = {'success': True, 'data': ['ALICE99 4 240', 'CHARLIE 3 38', 'JJJJJJJ 1 159', 'sss4544 1 0']}
        obj = FareController("test_files/corrupted.txt")
        obj.process_ledger()
        billing_response = obj.get_final_billing()
        self.assertEqual(billing_response, expected_response)
    
    # def test_program_on_bigger_payloads(self):
    #     obj = FareController("test_files/large_sample_log.txt")
    #     obj.process_ledger()
    #     billing_response = obj.get_final_billing() or {}
    #     self.assertEqual(billing_response.get('success'), True)

if __name__ == '__main__':
    unittest.main()

