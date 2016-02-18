Feature: Niko's feature
    Scenario: I can see a total count of tweets
        When I visit the website
        When I type some text into the text entry box
            | text |
            | any text |
        When I click the add button
        Then I see the text
            | text |
            | there is 1 tweet |
        When I type some text into the text entry box
            | text |
            | any more text |
        When I click the add button
        Then I see the text
            | text |
            | there are 2 tweets |

