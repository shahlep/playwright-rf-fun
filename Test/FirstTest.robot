*** Settings ***
Documentation    Suite description
Resource          ../Library/Helper/CommonHelper.robot

Suite Setup         Launch Chromium Browser
Suite Teardown      Quit Opened Browser

Test Setup         Open TodoMVC Application
Test Teardown      Close TodoMVC Application

*** Test Cases ***
First Test
    log     "open the application"
    take screenshot

