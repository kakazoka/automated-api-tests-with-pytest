# Automated API Tests with pytest
This automation uses pytest to automate API tests of the RAWG Video Games Database API.

## Features
- Tests designed to verify responses for game-related data
- Focus on the game Elden Ring, its DLCs and its development team
- Generates a .html report after the tests are executed

## Requirements
- [pytest](https://docs.pytest.org/en/stable/)
- [pytest-html](https://pytest-html.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/en/latest/)

## Dependencies
1. Install the required Python packages using `pip`:
```bash
pip install pytest
```
```bash
pip install pytest-html
```
```bash
pip install requests
```
2. Get API Key:
- [Get API Key](https://rawg.io/login/?forward=developer)

## File Structure
- `main.py` contains the test cases for verifying the API responses
- `make_request.py` contains the logic for making API requests
- `pytest.ini` is the configuration file, which allows the customization of the test suite

## How to Use
1. Clone or download the repository to your local machine
2. Open the script file `make_request.py`
3. Modify the `url` path with your API key
4. Run the script

## Script Overview
1. Defines the Test Class
2. Tests for game data
3. Tests for DLCs data
4. Tests for development team data
5. Generates a .html report after the tests are executed for better visualization of test results
