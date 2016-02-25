Feature: Mario's feature
    Scenario: I can see how many characters i have used
        When I visit the website
        Then typing text into the entry box changes the character count displayed
            | text         | count |
            | Diak ka lae? | 188   | 
            | Diak loos    | 191   | 
