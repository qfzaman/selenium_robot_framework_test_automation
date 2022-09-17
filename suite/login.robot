*** Settings ***
Library  Selenium2Library
Library  ../pages/loginPage.py

*** Variables ***
${url}    https://www.saucedemo.com/
${username}    standard_user
${password}    secret_sauce
${title}    Swag Labs

*** Test Cases ***
Open SWAGLabs Site in Browser
    open_login_screen  ${url}

Verify Login
    login_function  ${username}  ${password}

Verify Home Page
    ${verify}    validate_login  ${title}
    should be true  ${verify}
