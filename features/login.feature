Feature: login
    Scenario: login
        Given visit saucelab login page
        When enter valid username
        And enter valid password
        And click button login
        Then success login
        