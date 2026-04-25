# SauceDemo QA Automation Project 🚀

## 📌 Overview
This project demonstrates automated end-to-end testing for the SauceDemo web application using Playwright and Pytest.  
It follows the Page Object Model (POM) design pattern to ensure clean, maintainable, and scalable test code.

---

## 🛠️ Tech Stack
- Python
- Playwright
- Pytest

---

## 📂 Project Structure
first_python_project/

├── pages/        # Page Object classes  
├── tests/        # Test cases (UI automation)  
├── reports/      # Test reports  
├── utils/        # Helper functions  

├── pytest.ini  
├── requirements.txt  
├── README.md  
└── .gitignore  

---

## ✅ Test Coverage

### 🔐 Login
- Valid login
- Invalid login

### 🛒 Inventory
- Add item to cart
- Remove item from cart

### 🛍️ Cart
- Verify item appears in cart
- Verify cart content

### 💳 Checkout
- Successful checkout flow
- Empty fields validation
- Missing required fields validation

---

## ▶️ How to Run Tests

### 1. Install dependencies
pip install -r requirements.txt

### 2. Run all tests
pytest -s --headed

### 3. Generate HTML report
pytest --html=reports/report.html --self-contained-html

---

## 🧠 Key Features
- Page Object Model (POM)
- Clean and scalable test structure
- Positive and negative test scenarios
- End-to-End test coverage
- Automated test reporting

---

## 🎯 Future Improvements
- Add API testing (Requests)
- Implement test fixtures (pytest)
- Add CI/CD integration (GitHub Actions)
- Data-driven testing

---

## 👨‍💻 Author
Obadah
