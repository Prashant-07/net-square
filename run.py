from bill_calculator.bill_calculator import FareController
import sys

if __name__ == '__main__':
    if len(sys.argv) <= 1: 
        print("Please provide the filename as an arguement")
        sys.exit()
    file_path = sys.argv[1]
    fare_controller = FareController(file_path)
    res = fare_controller.process_ledger() or {}
    if res.get('success'):
        response = fare_controller.get_final_billing()
        # for session in response.get('data'): print(session)
    else:
        print(res.get('message'))