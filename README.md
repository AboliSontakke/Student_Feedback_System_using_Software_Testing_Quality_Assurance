# 🎓 Student Feedback System – Automation Testing And Quality Assurance

This project demonstrates **Automation Testing** of a *Student Feedback System* using **Selenium WebDriver** in Python, applying **Object-Oriented Testing (OOT)** principles.  
It is developed as part of the **Software Testing and Quality Assurance (STQA) FA2 Evaluation**.

---

## 🚀 Project Overview

The **Student Feedback System** is a web-based application that allows students to submit feedback on faculty performance.  
This project focuses on **automating the admin login functionality** using Selenium and applying **Object-Oriented Testing** concepts to ensure code reusability, modularity, and maintainability.

---

## 🧩 Technologies Used

| Component | Technology |
|------------|-------------|
| Programming Language | Python |
| Automation Tool | Selenium WebDriver |
| Web Browser | Google Chrome |
| Design Approach | Object-Oriented Testing (OOP) |
| Local Server | XAMPP / WAMP |
| IDE (optional) | VS Code / PyCharm / Eclipse PyDev |

---

## ⚙️ Features

- Automated Admin Login test using Selenium  
- Object-Oriented design for better modularity and code reusability  
- WebDriver management using `webdriver_manager`  
- Real-time simulation of typing and clicking  
- Console output for pass/fail test results  

---

## 🧠 Object-Oriented Concepts Used

| Concept | Application |
|----------|--------------|
| **Encapsulation** | Each class (BaseTest, LoginPage, TestLogin) contains specific related logic. |
| **Inheritance** | Test class inherits from base class for setup and teardown. |
| **Abstraction** | Test hides browser details — only uses high-level `login()` function. |
| **Reusability** | Code can be extended to test other modules (feedback, admin reports, etc.). |

---

## 🧰 Project Structure

```bash
StudentFeedback_Automation/
│
├── object_oriented_login_test.py   # Main test file
├── README.md                       # Project description
└── requirements.txt                 # Required dependencies

