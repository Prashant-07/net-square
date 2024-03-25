from datetime import datetime
from object_factory.object_factory import UserObjectFactory
import re

class FareController:
    def __init__(self, ledger_path):
        self.file_path = ledger_path
        self.user_obj_factory = UserObjectFactory()
        self.start_timestamp  = None
        self.end_timeStamp = None
    
    def process_ledger(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    # single line will transformed to list ['14:02:03', 'ALICE99', 'Start']
                    details = line.strip().split()
                    
                    # if the entry isn't valid, it will ignored
                    if not self.validate_entry(details): continue
 
                    # adding the session of user for calculation
                    self.add_user_session(details)
            return {'success': True, 'message': "Processed all the records"}
        
        except FileNotFoundError:
            return {'success': False, 'message': "File not found in the given path"}
        
        except Exception as e:
            return {'success': False, 'message': f"Unable to proceed further due to the exception : {e}"}

    def add_user_session(self, details):
        timestamp_str, user, status = details
        timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

        if self.start_timestamp is None: self.start_timestamp = timestamp
        self.end_timeStamp = timestamp

        user_obj = self.user_obj_factory.get_user_obj(user)

        if status == 'End': user_obj.end_session(timestamp, self.start_timestamp)
        else: user_obj.start_session(timestamp)
        
    def validate_entry(self, details):
        # if the number of params aren't sufficient
        if len(details) != 3: return False

        # here details is denoting one line from file ['14:02:03', 'ALICE99', 'Start']
        timestamp_str, user, status = details   

        # using this pattern to verify the value of timestamp
        timestamp_pattern = r'^([01]?[0-9]|2[0-3]):([0-5]?[0-9]):([0-5]?[0-9])$'

        # if timestamp value isn't matching the pattern 'hh:mm:ss'
        if not timestamp_str or re.match(timestamp_pattern, timestamp_str) is None: return False 
        
        # if the username is not alphanumeric, we will ignore the entry
        if user and not user.isalnum(): return False
        
        # if the status value is not either Start or End
        if status not in ("Start", "End"): return False
        
        return True

    def get_final_billing(self, sorted_usernames = False):
        # object factory is keeping a list of usernames as well, in the same order as provided in log
        usernames = self.user_obj_factory.get_ordered_username_list()
        
        # if we want the result sorted according to usernames lexicographically,
        # if it is false, we will get the results as per the order of log.
        if sorted_usernames: usernames.sort()
        result = []
        for username in usernames:
            user = self.user_obj_factory.get_user_obj(username)

            # processing all the remaining sessions of a user where no End was missing
            user.process_remaining_sessions(self.end_timeStamp)

            # we can change this statement to return the list as well, if the requirements changed.
            result.append(f"{user.name} {user.sessions} {user.total_duration}")
        
        return {"success": True, "data": result}
