from splinter.browser import Browser


def before_all(context):
    browser = context.config.browser
    if browser is None:
        browser = 'phantomjs'
    context.browser = Browser(browser)


def after_all(context):
    context.browser.quit()
    context.browser = None
