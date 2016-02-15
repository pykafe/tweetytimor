from behave import when, then


@then(u'the tweety text is visible') #noqa
def impl(context):
    # find the list of comments - an unordered list <ul> - use find_by_tag
    tweetlist = context.browser.find_by_tag('ul').first
    # find the list of comments - an unordered list <ul> - use find_by_tag
    assert tweetlist
    # for every row in the context table
    for row in context.table:
    # assert that an element exists IN THE list of comments with text from the table
        text = row['text']
        assert tweetlist.find_by_text(text)

@when(u'I click the add button') #noqa
def impl(context):
    context.browser.find_by_css('form button').click()

@when(u'I type some text into the text entry box') #noqa
def impl(context):
    for row in context.table:
        context.browser.find_by_tag('textarea').fill(row=['text'])

@then(u'a text entry box is visible') #noqa
def impl(context):
    assert context.browser.find_by_tag('textarea')

@when(u'I visit the website') #noqa
def impl(context):
    context.browser.visit(context.config.server_url)

@then(u'some text is visible') #noqa
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row['text'])

@then(u'an Add button is visible') #noqa
def impl(context):
    assert context.browser.find_by_css('form button')
