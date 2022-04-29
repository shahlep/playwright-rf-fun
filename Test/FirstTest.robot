*** Settings ***
Documentation    Suite description
Resource          ../Library/Helper/CommonHelper.robot
Resource          ../Library/Helper/PageHelper.robot

Suite Setup         Launch Webkit Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open TodoMVC Application
Test Teardown      Close TodoMVC Application

*** Test Cases ***
First Scenario
    [Tags]    odd
    log     "open the application"
    take screenshot
Second Scenario
    [Tags]    even  count
    TodoMVC.Add todos and Count
Third Scenario
    [Tags]     odd
    TodoMVC.Focus on todo input field when user visits the site
Fourth Scenario
    [Tags]    even
    TodoMVC.Clear input field after add a todo
Fifth Scenario
    [Tags]    odd
    TodoMVC.To check todo can be completed
Sixth Scenario
    [Tags]    even
    TodoMVC.Clear all completed todos
Seventh Scenario
    [Tags]    odd
    TodoMVC.Can edit a todo
Eighth Scenario
    [Tags]    even
    TodoMVC.Count number of todo left to complete
Nineth Scenario
    [Tags]    odd
    TodoMVC.Page reload and persist
Tenth Scenario
    [Tags]    even
    TodoMVC.Display only completed todos


