# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests
from playwright.sync_api import Page, expect  # Import Page and expect for Playwright testing

# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_homepage_loads_and_elements_exist(page: Page, fastapi_server):
    """
    Test that the homepage loads successfully and all key calculator elements are visible.
    Combines the functionality of your test_hello_world and checks for calculator UI.
    """
    page.goto("http://localhost:8000")

    # Verify main heading and calculator subheading
    expect(page.locator("h1")).to_have_text("Hello World")
    expect(page.locator("h2")).to_have_text("Calculator")

    # Verify input fields are visible
    expect(page.locator("#a")).to_be_visible()
    expect(page.locator("#b")).to_be_visible()

    # Verify all operation buttons are visible
    expect(page.locator("button:text('Add')")).to_be_visible()
    expect(page.locator("button:text('Subtract')")).to_be_visible()
    expect(page.locator("button:text('Multiply')")).to_be_visible()
    expect(page.locator("button:text('Divide')")).to_be_visible()

    # Verify the result display area is visible and initially empty
    # This assertion will now wait for the element to become visible and have empty text
    expect(page.locator("#result")).to_be_visible()
    expect(page.locator("#result")).to_have_text("")


@pytest.mark.e2e
def test_calculator_add(page: Page, fastapi_server):
    """
    Test the addition functionality of the calculator.
    Simulates user input and verifies the correct result display.
    """
    page.goto('http://localhost:8000')

    page.fill('#a', '10')
    page.fill('#b', '5')
    page.click('button:text("Add")')

    # Use expect().to_have_text() to wait for the element to have the correct text
    expect(page.locator('#result')).to_have_text('Calculation Result: 15')


@pytest.mark.e2e
def test_calculator_subtract(page: Page, fastapi_server):
    """
    Test the subtraction functionality of the calculator.
    """
    page.goto('http://localhost:8000')

    page.fill('#a', '20')
    page.fill('#b', '7')
    page.click('button:text("Subtract")')

    expect(page.locator('#result')).to_have_text('Calculation Result: 13')


@pytest.mark.e2e
def test_calculator_multiply(page: Page, fastapi_server):
    """
    Test the multiplication functionality of the calculator.
    """
    page.goto('http://localhost:8000')

    page.fill('#a', '6')
    page.fill('#b', '4')
    page.click('button:text("Multiply")')

    expect(page.locator('#result')).to_have_text('Calculation Result: 24')


@pytest.mark.e2e
def test_calculator_divide(page: Page, fastapi_server):
    """
    Test the division functionality of the calculator with an integer result.
    """
    page.goto('http://localhost:8000')

    page.fill('#a', '100')
    page.fill('#b', '25')
    page.click('button:text("Divide")')

    expect(page.locator('#result')).to_have_text('Calculation Result: 4')


@pytest.mark.e2e
def test_calculator_divide_by_zero_error(page: Page, fastapi_server):
    """
    Test division by zero error handling on the frontend.
    """
    page.goto('http://localhost:8000')

    page.fill('#a', '10')
    page.fill('#b', '0')
    page.click('button:text("Divide")')

    # Use expect().to_have_text() here as well
    expect(page.locator('#result')).to_have_text('Error: Cannot divide by zero!')


@pytest.mark.e2e
def test_calculator_float_results_and_inputs(page: Page, fastapi_server):
    """
    Test calculations involving float inputs and producing float results.
    """
    page.goto('http://localhost:8000')

    # Test addition with floats
    page.fill('#a', '7.5')
    page.fill('#b', '2.5')
    page.click('button:text("Add")')
    # Expect 10, not 10.0, because we added Number.isInteger check in JS
    expect(page.locator('#result')).to_have_text('Calculation Result: 10')

    # Test division with float result (e.g., 7 / 2 = 3.5)
    page.fill('#a', '7')
    page.fill('#b', '2')
    page.click('button:text("Divide")')
    expect(page.locator('#result')).to_have_text('Calculation Result: 3.5')

    # Test multiplication with float result (e.g., 2.5 * 3 = 7.5)
    page.fill('#a', '2.5')
    page.fill('#b', '3')
    page.click('button:text("Multiply")')
    expect(page.locator('#result')).to_have_text('Calculation Result: 7.5')

    # Test subtraction with float result (e.g., 10 - 2.75 = 7.25)
    page.fill('#a', '10')
    page.fill('#b', '2.75')
    page.click('button:text("Subtract")')
    expect(page.locator('#result')).to_have_text('Calculation Result: 7.25')


@pytest.mark.e2e
def test_calculator_invalid_input_type_on_frontend(page: Page, fastapi_server):
    """
    Test frontend handling of non-numeric input.
    """
    page.goto('http://localhost:8000')

    # Using evaluate to bypass type="number" browser-side validation for testing purposes
    page.evaluate("document.getElementById('a').value = 'abc'")
    page.evaluate("document.getElementById('b').value = '5'")
    page.click('button:text("Add")')

    # This assumes your frontend JS displays the 'error' from the backend's JSON response
    # (FastAPI 422 validation error message)
    expect(page.locator('#result')).to_have_text(
        'Error: a: Input should be a valid number'
    )