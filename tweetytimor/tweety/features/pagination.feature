Feature: Feature ba pajinasaun
    Scenario: Hau bele hare deit komentariu lima husi komentariu sira
        When I visit the website
        When I add some tweets
            | tweet |
            | this is the first tweet |
            | this is the second tweet |
            | this is the third tweet |
            | this is the fourth tweet |
            | this is the fifth tweet |
            | this is the sixth tweet |
            | this is the seventh tweet |
        Then I see only five tweets
        When I click the show_more button
        Then I can see more than five tweets 
