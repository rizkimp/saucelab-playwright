Feature: checkout 2 product
    Scenario: checkout 2 product
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
        Given click icon cart and in cart page
        Then remove backpack
        And remove bike
        And there is badge 2 in cart
        When click button checkout
        Then in checkout information page
        And enter valid first name
        And enter valid last name
        And enter valid postal code
        When click button continue
        Then in checkout overview page
        When click button finish
        Then success order

        
