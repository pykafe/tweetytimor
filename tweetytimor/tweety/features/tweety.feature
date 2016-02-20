Feature: The site should display a title

    Scenario: The website says Hello Tweety Timor
        When I visit the website
        Then some text is visible
            | text               |
            | Hello Tweety Timor |

    Scenario: I can enter text into the website
        When I visit the website
        Then some text is visible
            | text             |
            | Say Something:   |
        Then a text entry box is visible
        Then select only country
        Then an Add button is visible

    Scenario: I can add tweeties to the site
        When I visit the website
        When I type some text into the text entry box
            | text |
            | Diak ka lae? |
        When I click the add button
        Then the tweety text is visible
            | text |
            | Diak ka lae? |
        When I visit the website
        Then the tweety text is visible
            | text |
            | Diak ka lae? |

    Scenario:I visit the all history
        When I visit the website
        Then an Add button is visible
        When I click tha button history
        Then I see on page history
        Then an Add button is visible
        When I clik the button add
        Then I am on page add comment
