
import sys
import re
import operator
import csv

errors = {}
per_user = {}

error_pattern = r"ERROR"
info_pattern = r"INFO"
username_pattern = r"\((\w+)\)"
error_message_pattern = r"ERROR (.+)\("

with open(sys.argv[1]) as f:
    for line in f:
        match_error = re.search(error_pattern, line)
        match_info = re.search(info_pattern, line)
        search_username = re.search(username_pattern, line)
        search_error_message = re.search(error_message_pattern,line)

        if match_error and search_username:
            username = search_username.group(1).strip()
            error_message = search_error_message.group(1).strip()
            if error_message in errors :
              errors[error_message] = errors.get(error_message, 0) + 1
            else :
               errors[error_message] = 1

            # Check if username already exists in per_user dictionary
            if username in per_user:
                per_user[username]["ERROR"] = per_user[username].get("ERROR", 0) + 1
            else:
                per_user[username] = {"ERROR": 1, "INFO": 0}

        if match_info and search_username:
            username = search_username.group(1).strip()
            # Check if username already exists in per_user dictionary
            if username in per_user:
                per_user[username]["INFO"] = per_user[username].get("INFO", 0) + 1
            else:
                per_user[username] = {"ERROR": 0, "INFO": 1}

error = sorted(errors.items(), key = operator.itemgetter(1), reverse=True)
user = sorted(per_user.items(), key=lambda x: x[0])
error.insert(0, ("Error", "Count"))
user = [ (k[0],(k[1]["ERROR"]),(k[1]["INFO"])) for k in user] 
user.insert(0, ("Username", "INFO", "ERROR"))
print(error)
print("this is siparator")
print(user)

with open('error_message.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(error)

with open('user_statistics.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(user)
