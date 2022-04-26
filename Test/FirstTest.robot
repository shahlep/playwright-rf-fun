*** Settings ***
Documentation    Suite description
Resource          ../Library/Helper/CommonHelper.robot
Resource          ../Library/Helper/PageHelper.robot

Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open TodoMVC Application
Test Teardown      Close TodoMVC Application

*** Test Cases ***
First Scenario
    log     "open the application"
    take screenshot
Second Scenario
    TodoMVC.Add todos and Count
Third Scenario
    TodoMVC.Focus on todo input field when user visits the site
Fourth Scenario
    TodoMVC.Clear input field after add a todo
Fifth Scenario
    TodoMVC.To check todo can be completed
Sixth Scenario
    TodoMVC.Clear all completed todos
Seventh Scenario
    TodoMVC.Can edit a todo
Eighth Scenario
    TodoMVC.Count number of todo left to complete
Nineth Scenario
    TodoMVC.Page reload and persist
Tenth Scenario
    TodoMVC.Display only completed todos


