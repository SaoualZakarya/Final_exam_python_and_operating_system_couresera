# Final_exam_python_and_operating_system_coursera

### This was the final exam for me to got a certificate in coursera under the name " Using Python to Interact with the Operating System specialization "

Log Analysis and Reporting Script

This Python script, ticky_check.py, automates the analysis of system logs from the internal ticketing system (ticky). It efficiently parses syslog.log, extracting critical information and organizing it into structured CSV files for detailed analysis. The script employs regular expressions to identify different log entry types, categorizing them into two reports:

Error Message Ranking Report:
Generates a CSV file (error_message.csv) containing a sorted list of various error messages and their occurrence counts. This report aids in pinpointing common issues within the system.

User Usage Statistics Report:
Produces a CSV file (user_statistics.csv) with user-specific statistics, distinguishing between INFO and ERROR messages. This report provides insights into user engagement patterns and potential problem areas.

Features:

Accurate log parsing using regular expressions for robust analysis.
Output in CSV format, facilitating easy integration with data analysis tools.
Automated categorization of log entries, ensuring precise insights.
Lightweight and easy to use, ideal for quick log analysis tasks.
Highly customizable for adapting to specific log formats and requirements.
How to Use:

Run ticky_check.py to parse syslog.log and generate error_message.csv and user_statistics.csv.
Utilize the generated CSV files for in-depth analysis using spreadsheet applications or data analysis tools.