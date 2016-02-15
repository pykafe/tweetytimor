from behave import when, then


@then(u'the tweety text is visible')
def impl(context):
    for row in context.table:
        assert context.browsser.find_by_text(row[text])


@when(u'I click the add button')
def impl(context):
    context.browser.find_by_css('a[href="/add/"]').click


@when(u'I type some text into the text entry box')
def impl(context):
    context.browser.find_by_tag('textarea')


@then(u'a text entry box is visible')
def impl(context):
    assert context.browser.find_by_text("text")


@when(u'I visit the website')
def impl(context):
    context.browser.visit(context.config.server_url)


@then(u'some text is visible')
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row[text])


@then(u'an Add button is visible')
def impl(context):
    assert context.browser.find_by_css('

