import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'click icon cart and in cart page')
def step_impl(context):
    context.page.click(f'#{locator.icon_cart}')
    context.page.locator(f'#{locator.in_cart_page}')

@then(u'remove backpack')
def step_impl(context):
    context.page.click(f'#{locator.button_remove_backpack}')

@then(u'remove bike')
def step_impl(context):
    context.page.click(f'#{locator.button_remove_bike}')

@then(u'there is badge 2 in cart')
def step_impl(context):
    context.page.locator(f'#{locator.badge_2_cart}')

@when(u'click button checkout')
def step_impl(context):
    context.page.click(f'#{locator.button_checkout}')

@then(u'in checkout information page')
def step_impl(context):
    context.page.locator(f'#{locator.in_checkout_information_page}')

@then(u'enter valid first name')
def step_impl(context):
    context.page.fill(f'#{locator.input_firstname}','rizz')

@then(u'enter valid last name')
def step_impl(context):
    context.page.fill(f'#{locator.input_lastname}','qweeqwee')

@then(u'enter valid postal code')
def step_impl(context):
    context.page.fill(f'#{locator.input_postalcode}','1234567')

@when(u'click button continue')
def step_impl(context):
    context.page.click(f'#{locator.button_continue}')

@then(u'in checkout overview page')
def step_impl(context):
    context.page.locator(f'#{locator.in_checkout_overview}')

@when(u'click button finish')
def step_impl(context):
    context.page.click(f'#{locator.button_finish}')

@then(u'success order')
def step_impl(context):
    context.page.locator(f'#{locator.success_order}')