import pytest as pytest

def pytest_addoption(parser):
    parser.addoption(
        '--data-source', action='store', default='api', help='Specify mock to run tests on the mock data. Default is API'
    )

@pytest.fixture
def data_source(request):
    return request.config.getoption('--data-source')