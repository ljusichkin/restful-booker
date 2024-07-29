import allure
import requests
import pytest

import test_1_booking_token
import test_2_booking_create


@allure.feature('Booking Feature')
@allure.suite('Delete Booking Suite')
@allure.title('Test Delete Booking by ID with Valid Token')
@allure.description('Test to delete a booking by ID using a valid token and verify the response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_by_id_valid_token():
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={test_1_booking_token.my_token}'
    }

    with allure.step('Send DELETE request to delete a booking by ID using a valid token'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_booking_create.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify response status code is 201'):
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'

