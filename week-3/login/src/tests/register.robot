*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  m
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Click Button  Register
    Register Should Fail With Message  Username is too short!

Register With Valid Username And Too Short Password
    Set Username  mikko
    Set Password  m
    Set Password Confirmation  m
    Click Button  Register
    Register Should Fail With Message  Password is too short!

Register With Valid Username And Invalid Password
    Set Username  mikko
    Set Password  mikkoyksikaksikolme
    Set Password Confirmation  mikkoyksikaksikolme
    Click Button  Register
    Register Should Fail With Message  Password must contain at least one number or special character.

Register With Nonmatching Password And Password Confirmation
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko
    Click Button  Register
    Register Should Fail With Message  Passwords do not match!

Register With Username That Is Already In Use
    Create User  kalle  kalle123
    Set Username  kalle
    Set Password  kalle456
    Set Password Confirmation  kalle456
    Click Button  Register
    Register Should Fail With Message  Username is already taken!

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}


*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
