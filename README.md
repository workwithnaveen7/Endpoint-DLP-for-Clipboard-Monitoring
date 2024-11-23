# Endpoint DLP for Clipboard Monitoring

The Endpoint Data Loss Prevention (DLP) for Clipboard Monitoring project is designed to enhance cybersecurity by monitoring clipboard activities for sensitive data. This tool helps prevent accidental data leakage by detecting and managing sensitive information copied to the clipboard. It offers real-time notifications, immediate clipboard clearing, logging of detected sensitive data to MySQL database storage for easier management and review.

## Features
• Monitors the clipboard continuously.  
• Detects sensitive data types including:  
    o Aadhaar number  
    o PAN number  
    o Phone number  
    o Email address  
    o Bank account number  
    o Driving license number  
• Clears the clipboard if sensitive data is detected.  
• Sends desktop notifications when sensitive data is detected.  
• Logs the sensitive data with timestamp to MySQL database for further review.  
• Integrated login system using Tkinter to ensure that only authorized users can access the program.

As an endpoint DLP solution, this tool protects individual workstations, which are often the weakest link in a company’s security infrastructure. By securing endpoints, the overall security posture of the company is improved.


## Tech Stack
• Programming Language – Python  
• MySQL: Used to store logs of sensitive data, allowing for easier data management and reporting.

### Python Libraries used:
• pyperclip: Used for clipboard operations, enabling the program to access and modify clipboard content.  
• plyer: Provides cross-platform desktop notifications to alert users in real-time.  
• re: Utilized for regular expression-based detection of sensitive data patterns.  
• datetime: Used for timestamping logs to track when sensitive data is detected.  
• Tkinter: used for creating the login interface and authentication system.

## Conclusion
Using the Endpoint DLP for Clipboard Monitoring project can significantly improve data loss prevention efforts in any organization. It provides real-time detection and management of sensitive data, enhances user awareness, ensures compliance, and strengthens endpoint security, making it an invaluable tool in the fight against data breaches and accidental data leaks.

## Working:

### User Authentication
![DLP 1 login](https://github.com/user-attachments/assets/2aed25a3-fbef-469d-bfeb-88e86ac15f93)

### Notifying user that sensitive content is detected
![DLP 2 notify](https://github.com/user-attachments/assets/3107838f-71f6-45d6-b253-2e4b822d16b4)

### Clearing the clipboard 
![DLP 3 data clear](https://github.com/user-attachments/assets/517b25cd-f526-4e40-ae37-bc17375ca032)

### Logging the data in MySQL database for review
![DLP 4 logging](https://github.com/user-attachments/assets/a015edf4-fa8b-4449-9b00-6424886277a4)



