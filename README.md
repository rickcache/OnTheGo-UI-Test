## On The Go Site Automation Project (Selenium + Pytest)

**On The Go** is a convenient online ticket booking platform that allows users to:

-Search and compare available travel routes

-Book tickets for buses or trains seamlessly

-View and manage existing bookings

-Cancel tickets and request refunds

-Download e-tickets and booking receipts for travel

---

## **Overview**

This project is a complete automation testing suite for the On The Go web application, built using Selenium WebDriver, Pytest, and the Page Object Model (POM) design pattern.
It performs end-to-end functional testing across all major user journeys — from registration to booking management, including reviews, profile updates, and ticket downloads.

---

## Project Overview

The goal of this project is to ensure the stability, functionality, and reliability of the On The Go platform through automated testing.

This suite includes test coverage for:

User Authentication – Login, Logout, Registration (new & existing users)

Reviews – Submit, validate, and confirm feedback

Trending Deals – Verify display and accessibility of trending offers

Profile Management – Update profile details

Booking Management – Check booking details, cancel tickets

Downloads – Ticket downloads and confirmation
---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/rickcache/On-The-Go-Ui-Testing.git

```

### Navigate to the project folder
```bash
cd On The Go_test
```


### Create a Virtual Environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux

```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run all tests
```bash
pytest -v -s
```

### Run a specific test module
```bash
pytest tests/test_login.py -v -s
```

### Run tests by marker (e.g., review):
```bash
pytest -m review -v -s
```

### Generate HTML report
```bash
pytest --html=report.html -v -s
```

### Generate self-contained HTML report with screenshots
```bash
pytest -v -s --self-contained-html
```

## Featured Tested

Login / Logout – Validate authentication with valid and invalid credentials

Registration – New user signup, duplicate email handling

Trending Deals – Validate display and links of trending offers

Submit Review – Fill and submit reviews, validate success messages

Profile Update – Update user information and verify persistence

Check Booking Details – Verify correct booking information display

Cancel Booking – Test ticket cancellation workflow

Download Ticket – Verify tickets are downloadable and saved correctly

## Reporting & Artifacts

HTML Reports
Generated automatically using pytest-html, located in /reports/

Screenshots
Captured automatically on test failures, stored in /screenshots/

Logs
Detailed execution logs in test_log.log, include timestamps, test start/stop info, and errors

Downloads
Tickets and other files are stored in /downloads/### Framework Highlights

Page Object Model (POM) – Keeps test logic separate from page locators

Data-Driven Testing – Loads credentials and test data dynamically from JSON files

Custom Fixtures – conftest.py handles WebDriver setup, teardown, logging, and reporting

Error Capture – Screenshots and logs are automatically attached to reports on failure

Cross-Browser Ready – ChromeOptions configured; extendable for Firefox or Edge


## Tools & Libraries

Tool / Library	Purpose
Selenium WebDriver	Browser automation
Pytest	Test framework
pytest-html	Report generation
pytest-ordering / pytest-xdist	Parallel and ordered test execution
logging	Centralized test logs
os, time	File handling and waits
ChromeDriver	Browser driver for automation
## Notes

>This project is for educational and portfolio purposes

>Demonstrates real-world automation architecture with POM and fixtures

>You can clone, modify, and expand this framework for your own learning

>The site resets data periodically; test data may need refreshing
## Author

Rick Biswas
🎓 B.Sc Computer Science | Bhairabh Ganguly College
💼 Aspiring QA Engineer | Automation Enthusiast
🌐 GitHub: rickcache
