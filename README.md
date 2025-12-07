{"id":"58214","variant":"standard","title":"README – Selenium Automation Project"}
Selenium Automation Testing Project (Python)

Author: Shalin  
Role: PHP Developer + Automation QA  
Date: December 2025 
-------------------------------------------------

Overview

This project is created to demonstrate my skills in:

- Manual Testing Fundamentals  
- Creating Test Cases  
- Selenium Automation using Python  
- Web Application Testing  
- Basic Test Framework Structure  
- Positive and Negative Test Scenarios  

The main purpose of this project is to automate the **Login functionality** of a web application and validate both **successful and unsuccessful login attempts**.

-------------------------------------------------

Tools & Technologies Used

- Language: Python  
- Automation Tool: Selenium WebDriver  
- IDE: VS Code / Notepad++  
- Browser: Google Chrome  
- Version Control: Git & GitHub  
- OS: Windows  

-------------------------------------------------

Test Website Used

For practice purposes, I used a safe demo site:

https://www.saucedemo.com/

Test Credentials:
Username: standard_user  
Password: secret_sauce  

-------------------------------------------------

Features Automated

1. Valid Login Test
   - Enters correct username and password
   - Clicks login button
   - Verifies dashboard page is loaded

2. Invalid Login Test
   - Enters correct username and wrong password
   - Clicks login button
   - Verifies error message / login failure

3. Basic Assertion
   - Checks current URL after login
   - Displays PASS or FAIL in console

-------------------------------------------------

Project Structure

Selenium_Project/
│
├── tests/
│   ├── login_test.py
│
├── screenshots/
│   ├── (Screenshots saved on failure – future scope)
│
├── data/
│   ├── (For future test data files)
│
└── README.md

-------------------------------------------------

How to Run the Project

1. Make sure Python and Selenium are installed:
   python --version
   pip install selenium

2. Place chromedriver in system PATH

3. Go to project folder:
   cd Selenium_Project/tests

4. Run the script:
   python login_test.py

Expected Result:
Browser will open → Login automatically → Show PASS/FAIL → Close browser.

-------------------------------------------------

What I Learned

- Writing manual test cases
- Understanding test case components (Pre-condition, Steps, Expected result)
- Automating browser actions
- Using Selenium for real-time testing
- Using GitHub for project hosting

-------------------------------------------------

Future Improvements

- Add Page Object Model (POM)
- Add PyTest framework
- Add Reports (Allure / HTML reports)
- Add screenshot on failure
- Add more test scenarios (Add to cart, Checkout, Logout)

-------------------------------------------------

About Me

I am currently working as a PHP Developer and upskilling myself in Quality Assurance & Automation Testing to move into better-paying opportunities.

This project is part of my preparation to transition into a **QA Automation / SDET role**.

-------------------------------------------------

Thank you for checking my project 🚀
