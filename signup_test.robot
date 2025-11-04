*** Settings ***
Library    C:/Users/Aboli/AutomationTests/AutomationLibrary.py
Library    BuiltIn

*** Variables ***
${ADMIN_EMAIL}      aboli@admin.com
${ADMIN_PASSWORD}   aboli
${USER_EMAIL}       sayali05@gmail.com
${USER_FIRST}       Aboli
${USER_LAST}        Sontakke
${USER_PASSWORD}    aboli123

*** Test Cases ***
Admin Login Test
    ${result}=    Admin Login    ${ADMIN_EMAIL}    ${ADMIN_PASSWORD}
    Should Be True    ${result}

Signup Test - Positive
    ${result}=    Signup User    ${USER_EMAIL}    ${USER_FIRST}    ${USER_LAST}    ${USER_PASSWORD}
  Should Be True    ${result} == False


Signup Test - Negative
    ${result}=    Signup User    ${USER_EMAIL}    A    ${USER_LAST}    ${USER_PASSWORD}
    Should Be False    ${result}

*** Keywords ***
Close Browser
    Close Browser
