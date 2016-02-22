Feature: Feature ba pajinasaun
    Scenario: Hau bele hare deit komentariu lima husi komentariu sira
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
            | type any more text to five value |
        When I click the add button
        Then I see the five comment of tweety
            | text |
            | there is 1 tweet   |
            | there are 2 tweets |
            | there are 3 tweets |
            | there are 4 tweets |
            | there are 5 tweets |
        When I click the add button
        Then I see the button show_more 

        When I click the show_more button
        Then I can see all of the tweety comments 
