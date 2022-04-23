*** Settings ***
Documentation    Common Helper File
Library          ../PyLib/PlaywrightCore.py

*** Keywords ***
Launch Chromium Browser
    launch browser    browser_name=chromium

Launch FireFox Browser
    launch browser    browser_name=firefox

Launch Webkit Browser
    launch browser    browser_name=webkit

Quit Opened Browser
    close browser

Open TodoMVC Application
    open application

Close TodoMVC Application
    close application
Get Page Handle
    ${page}     get page object
    [Return]    ${page}