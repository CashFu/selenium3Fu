#coding=utf-8

Feature: Register User
  As a developer
  This is my first bdd project

  Scenario: open register website
    When I open the register website
#    Then I expect that the title is "注册"


  Scenario: input username
    When I set with useremail "life@qq.com"
    And I set with username "lifn110"
    And I set with password "1110"
    And I set with code "tet"
    And I click with registerbutton
    Then I expect that text "验证码错误"
