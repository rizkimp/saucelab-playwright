import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'visit saucelab login page')
def step_impl(context):
    context.page.goto(locator.url_saucelab)
    time.sleep(3)

@when(u'enter valid username')
def step_impl(context):
    context.page.fill(f'#{locator.input_username}',(locator.username))

@when(u'enter valid password')
def step_impl(context):
    context.page.fill(f'#{locator.input_password}',(locator.password))

@when(u'click button login')
def step_impl(context):
    context.page.click(f'#{locator.button_login}')
    time.sleep(3)

@then(u'success login')
def step_impl(context):
    context.page.hover(f'#{locator.icon_cart}')
    time.sleep(3)