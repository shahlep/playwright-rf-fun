*** Settings ***
Documentation    Page Helper File
Library          ../Page/LandingPage.py
Resource         CommonHelper.robot

*** Keywords ***
TodoMVC.Add todos and Count
    ${page}     get page handle
    url page is working     ${page}

TodoMVC.Focus on todo input field when user visits the site
    ${page}     get page handle
    focus on todo input field    ${page}

TodoMVC.Clear input field after add a todo
    ${page}     get page handle
    clear input field after add    ${page}

TodoMVC.To check todo can be completed
    ${page}     get page handle
    to check todo can be completed    ${page}

TodoMVC.Clear all completed todos
    ${page}     get page handle
    clear all completed todos    ${page}

TodoMVC.Can edit a todo
    ${page}     get page handle
    can edit a todo    ${page}

TodoMVC.Count number of todo left to complete
    ${page}     get page handle
    count number of todo left to complete    ${page}

TodoMVC.Page reload and persist
    ${page}     get page handle
    page reload and persist    ${page}

TodoMVC.Display only completed todos
    ${page}     get page handle
    display only completed todos    ${page}

TodoMVC.Image Compare
    ${page}     get page handle
    image compare    ${page}