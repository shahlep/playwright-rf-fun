*** Settings ***
Documentation    Suite description
Resource          ../Library/Helper/CommonHelper.robot
Resource          ../Library/Helper/PageHelper.robot

Suite Setup         Launch Webkit Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open TodoMVC Application
Test Teardown      Close TodoMVC Application

*** Test Cases ***
First Scenarios
    log     "open the application"
    take screenshot
Second Scenarios
    TodoMVC.Add todos and Count
Third Scenarios
    TodoMVC.Focus on todo input field when user visits the site
Fourth Scenarios
    TodoMVC.Clear input field after add a todo
Fifth Scenarios
    TodoMVC.To check todo can be completed
Sixth Scenarios
    TodoMVC.Clear all completed todos
Seventh Scenarios
    TodoMVC.Can edit a todo
Eighth Scenarios
    TodoMVC.Count number of todo left to complete
Nineth Scenarios
    TodoMVC.Page reload and persist
Tenth Scenarios
    TodoMVC.Display only completed todos


