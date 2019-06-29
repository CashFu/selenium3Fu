#coding=utf-8
from behave import *
from features.lib.pages.register_page import RegisterPage

use_step_matcher('re')
@when('I open the register website "([^"]*)"')
def step_register(context,url):
    # 后面登录页.py需要driver,上下文context已经包含了driver
    RegisterPage(context).get_url(url)
    # context.driver.get(url)
@then('I expect that the title is "([^"]*)"')
def step_register1(context,title_name):
    title=RegisterPage(context).get_title()
    assert title_name in title

@when('I set with useremail "([^"]*)"')
def step_register(context,useremail):
    # 使用后面登录页.py文件中方法，这不能使用全局变量
    # context.driver.find_element_by_id("register_email").send_keys(useremail)
    RegisterPage(context).send_useremail(useremail)
@when('I set with username "([^"]*)"')
def step_register(context,username):
    # context.driver.find_element_by_id("register_nickname").send_keys(username)
    RegisterPage(context).send_useremail(username)
@when('I set with password "([^"]*)"')
def step_register(context,password):
    # context.driver.find_element_by_id("register_password").send_keys(password)
    RegisterPage(context).send_password(password)
@when('I set with code "([^"]*)"')
def step_register(context,code):
    # context.driver.find_element_by_id("captcha_code").send_keys(code)
    RegisterPage(context).send_code(code)
@when('I click with registerbutton')
def step_register(context):
    RegisterPage(context).click_register_button()
    # context.driver.find_element_by_id("register-btn").click()

@then('I expect that text "([^"]*)"')
def step_register(context,code_text):
    # text=context.driver.find_element_by_id("captcha_code-error").
    text = RegisterPage(context).get_code_text()

    assert code_text in text