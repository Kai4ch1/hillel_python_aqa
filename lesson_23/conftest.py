import pytest
import logging

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    logging.basicConfig(
        filename='test_search.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        force=True
    )


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()

    if report.when == "call":
        logger = logging.getLogger("SEARCH EVENT")

        message = f"Test: {item.name} | Result: {report.outcome.upper()}"
        logger.log(20, message)
