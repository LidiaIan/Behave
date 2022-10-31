from browser import Browser
from pages.homepage import Homepage
from pages.authentication_page import Authentication


def before_all(context):
    context.browser = Browser()
    context.homepage = Homepage(context.browser.driver)
    context.authentication_page = Authentication(context.browser.driver)


def after_all(context):
    context.browser.close()