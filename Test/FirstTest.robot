*** Settings ***
Documentation    Suite description
Library          ../Library/PyLib/PlaywrightCore.py

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Provided precondition
    When action
    Then check expectations

*** Keywords ***
Provided precondition
    Setup system under test