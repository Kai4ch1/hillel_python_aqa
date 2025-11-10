
import pytest
from hillel_python_aqa.lesson_14.main_function.func import *


class TestLogging:
    @pytest.mark.parametrize(
            "username, operation, log_level", [
            ("Pablo", "success", "INFO"),
            ("Pablo", "expired", "WARNING"),
            ("Pablo", "22", "ERROR")
        ]
    )
    @pytest.mark.smoke
    def test_check_log_validity(self, username, operation, log_level):
        log_content = "login_system.log"
        log_event(username, operation)
        expected_log = f"- {log_level} - Login event - Username: {username}, Status: {operation}"
        with open(log_content, "r") as f:
             log_file_text = f.read()
             if not log_file_text:
                 pytest.fail("There is no logs in chosen file")
             rows = log_file_text.splitlines()
             last_log = rows[-1].strip()
             assert expected_log in last_log, f"Actual log={last_log}, expected log={expected_log}"

    @pytest.mark.parametrize(
        "test_name, username, operation_status, test_status, log_level", [
            ("invalid Non-type username, valid operation", None, "success", "PASSED", "INFO"),
            ("invalid Number username, valid operation", 2, "success", "PASSED", "INFO"),
            ("valid username, invalid operation", "Victor", None, "FAILED", "ERROR"),
            ("valid username, invalid operation", "Andre", 32, "FAILED", "ERROR")
        ]
    )
    def test_check_logging_negative(self, test_name, username, operation_status, test_status, log_level):
        log_content = "login_system.log"
        log_event(username, operation_status)
        expected_log = f"- {log_level} - Login event - Username: {username}, Status: {operation_status}"
        with open(log_content, "r") as f:
            log_file_text = f.read()
            if not log_file_text:
                pytest.fail("There is no logs in chosen file")
            rows = log_file_text.splitlines()
            last_log = rows[-1].strip()
            assert expected_log in last_log