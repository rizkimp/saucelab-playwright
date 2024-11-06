import time
import asyncio
from behave import *
from locators import *
from playwright.sync_api import sync_playwright

@given(u'in product page')
def step_impl(context):
    context.page.hover(f'#{locator.icon_cart}')

@when(u'add backpack to cart')
def step_impl(context):
    context.page.click(f'#{locator.button_addtocart_backpack}')

@when(u'add bike to cart')
def step_impl(context):
    context.page.click(f'#{locator.button_addtocart_bike}')

@when(u'add shirt to cart')
def step_impl(context):
    context.page.click(f'#{locator.button_addtocart_shirt}')

@when(u'add jacket to cart')
def step_impl(context):
    context.page.click(f'#{locator.button_addtocart_jacket}')

@then(u'there is badge 4 in cart')
def step_impl(context):
    context.page.locator(f'#{locator.badge_4_cart}')