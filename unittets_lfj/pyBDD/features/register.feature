#coding=utf-8
  Feature: Register User
    As a developer
  This is my first bdd project
  Scenario: open register website
    When I open the register website "http://www.5itest.cn/register"
    Then I expect that the title is "注册"

    Scenario: input username
      When I set with useremail "mmm@qq.com"
      And  I set with username "qwwq"
      And  I set with password "112112"
      And  I set with code "code"
      And  I click with registerbutton
      Then I expect that text "验证码错误"