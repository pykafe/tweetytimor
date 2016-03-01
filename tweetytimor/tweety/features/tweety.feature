Feature: The site should aloow people to post tweeties

    Scenario: The website says Hello Tweety Timor
        When I visit the website
        Then some text is visible
            | text               |
            | Hello Tweety Timor |

    Scenario: I can enter text into the website
        When I visit the website
        Then some text is visible
            | text             |
            | say something... |
        Then a text entry box is visible
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
