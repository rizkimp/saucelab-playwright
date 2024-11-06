Feature: add 4 product to cart
    Scenario: add 4 product to cart
        Given visit saucelab login page
        When enter valid username
        And enter valid password
        And click button login
        Then success login
        Given in product page
        When add backpack to cart
        And add bike to cart
        And add shirt to cart
        And add jacket to cart
        Then there is badge 4 in cart