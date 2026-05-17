from behave import given, when, then
from donation_service import DonationService

service = DonationService()

@given('a registered community member')
def step_registered_member(context):
    context.user_registered = True

@given('an unregistered user')
def step_unregistered_user(context):
    context.user_registered = False

@when('the member submits a request for {amount:d} food parcels')
def step_submit_request(context, amount):
    context.result = service.request_donation(
        context.user_registered,
        amount
    )

@when('the user submits a request for {amount:d} food parcel')
def step_submit_invalid(context, amount):
    context.result = service.request_donation(
        context.user_registered,
        amount
    )

@then('the request should be approved')
def step_approved(context):
    assert context.result == "Approved"

@then('the request should be rejected')
def step_rejected(context):
    assert context.result == "Rejected"

@then('an error message should be displayed')
def step_error(context):
    assert context.result == "Error: User not registered"