@echo off
REM ==========================================
REM Student Feedback Automation Test Suite
REM ==========================================

REM Navigate to the AutomationTests folder
cd C:\Users\Aboli\AutomationTests

echo -----------------------------
echo Test Case 1: Admin Login
echo -----------------------------
python test_login.py
echo -----------------------------
echo Test Case 2: Feedback Form Submission (Student)
echo -----------------------------
python test_feedback_submission.py
echo -----------------------------
echo Test Case 3: Admin Report View
echo -----------------------------
python test_admin_report.py
echo -----------------------------

echo ✅ All automation tests completed.
pause
