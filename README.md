# tweetytimor

1. Create a new virtual environment to work in
2. Git clone this repository
3. Pip install `Django`, and the BDD requirements `django-behave` and `splinter`
4. Create a django project `tweetytimor` with a single app named `tweety`
5. edit your `settings.py` file to add `django_behave` and `tweety` to `INSTALLED_APPS` and set `TEST_RUNNER` to `django_behave.runner.DjangoBehaveTestSuiteRunner`
6. Create a directory named `features` in the app you created
7. Create a directory named `steps` directory inside the `features` directory
8. Create a file named `environment.py` inside the `features` directory with the following contents:
            
        from splinter.browser import Browser

        def before_all(context):
            browser = context.config.browser
            if browser is None:
                browser = 'phantomjs'
            context.browser = Browser(browser)

        def after_all(context):
            context.browser.quit()
            context.browser = None

9. Create a new file named `tweety.feature` file inside the `features` directory with feature below:

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
                Feature: Hello World


10. Run the test with `python manage.py test tweety`
11. Create a new file named `tweety.py` in the `features/steps/` directory.
12. In `tweety.py` import from behave and then copy the suggested step implementations into `features/steps/tweety.py`:


13. Implement the steps with meaningful python code
14. Satisfy the tests so they pass
