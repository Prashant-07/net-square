from collections import deque

class User:
    def __init__(self, name, sessions = 0, total_duration = 0):
        self.name = name
        self.sessions = sessions
        self.total_duration = total_duration
        self.pending_sessions = deque()

    def process_remaining_sessions(self, end_timestamp):
        while self.pending_sessions:
            start_time = self.pending_sessions.popleft()
            self.sessions += 1
            self.total_duration += (end_timestamp - start_time).seconds

    def start_session(self, cur_timestamp):
        self.pending_sessions.append(cur_timestamp)
    
    def end_session(self, cur_timestamp, first_timestamp):
        if self.pending_sessions: 
            start_time = self.pending_sessions.popleft()
            session_duration = (cur_timestamp - start_time).seconds
        else:
            session_duration = (cur_timestamp - first_timestamp).seconds

        self.sessions += 1
        self.total_duration += session_duration