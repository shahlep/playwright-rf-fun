*** Settings ***
Documentation    Suite description
Library          ../Library/PyLib/PlaywrightCore.py

Suite Setup         launch browser      chromium
Suite Teardown      close browser

Test Setup          open application
Test Teardown       close application

*** Test Cases ***
First Test
    log     "open the application"
    take screenshot

