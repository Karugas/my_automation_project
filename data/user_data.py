class TestUsers:
    STANDARD_USER = {
        "username": "standard_user",
        "password": "secret_sauce"
    }

    STANDARD_USER_INVALID = {
        "username": "standard_user",
        "password": "123"
    }

    LOCKED_OUT_USER = {
        "username": "locked_out_user",
        "password": "secret_sauce"
    }


class CheckoutInformation:
    INFORMATION = {
        "first_name": "Yaromir",
        "last_name": "Udovkin",
        "postal_code": "66622"
    }
