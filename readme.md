How to Run the program?

1. Go to project directory, run the command: python3 run.py PATH_TO_FILE
   Note: PATH_TO_FILE should be the name of file residing in project directory or fully qualified path to file if it is not in project directory.
2. To run the testcases, run the command: python3 test_code.py
   Included Test Cases:
   1. File Doesn't exists.
   2. Blank File.
   3. Sample log, provided with mail.
   4. A corrupted file, with most of the invalid cases.
   5. A large log.


Components:
1. Bill Calculator: It is class handling the following responsibilities:
   1. To read the file
   2. Validate the entries i.e. if each line is valid or not.
   3. Modify the session data of each user as we are traversing the log.
   4. Provide a method get_final_billing to get all the users billing data.
      
2. Object Factory: Used Factory design pattern here to abstract out the user object creation and distribution.
   It consist of two functionalities
   1. Return the User object if it exists, otherwise create the user object and then return it.
   2. Maintaining the username name in the same order as the log.

3. User: A user class is responsible for managing
   1. The number of sessions.
   2. Total session duration.
   3. Pending sessions, where we have the start record of a session but the corresponding end record isn't present.
      Making use of queue to keep all the pending sessions, if we encounter an end session record for a user, we can simply fetch the least recently added session from the queue or if no such recond exists then consider the start time as start of session.
