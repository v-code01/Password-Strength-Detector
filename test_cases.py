# test_cases.py
from advanced_password_checker import SuperAdvancedPasswordChecker

def run_test_case(password, expected_score):
    checker = SuperAdvancedPasswordChecker(password)
    security_score = checker.get_security_score()
    assert security_score == expected_score, f"Test Case Failed: Password: {password}, Expected: {expected_score}, Actual: {security_score}"
    print(f"Test Case Passed: Password: {password}, Expected: {expected_score}, Actual: {security_score}")

if __name__ == "__main__":
    # Test cases with varying scores
    run_test_case("WeakPwd123", 50)
    run_test_case("StrongP@ssw0rd", 950)
    run_test_case("123456789", 0)
    run_test_case("P@ssw0rdP@ssw0rd", 800)
    run_test_case("AbCdEfGhIjK", 400)
    run_test_case("SuperSecure1!2@3#", 1000)
    run_test_case("qwerty", 0)
    run_test_case("pass", 0)
    run_test_case("Passw0rd123", 700)
    run_test_case("!@#$%^&*()", 600)
    run_test_case("ABCDabcd1234!@#$", 1000)
