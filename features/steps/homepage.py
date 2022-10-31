from behave import *


@given("I am on the Homepage")
def step_implement(context):
    context.homepage.go_to()


@when('I click on "{page_link_text}" link')
def step_implement(context, page_link_text):
    context.homepage.go_to(page_link_text)


@then("I am redirected to Login Page")
def step_implement(context):
    assert context.browser.get_current_url() == context.authentication.URL
