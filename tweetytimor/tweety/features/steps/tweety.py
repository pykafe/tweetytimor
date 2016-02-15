from behave import given, when, then


@then(u'the tweety text is visible')
def impl(context):
    # find a list in the page - find_by_tag - look for an unordered list tag 'ul'
    # assign that list to a variable so we can use it later 'tweetlist'
    for row in context.table:
    # assert that we have found that list
        assert context.browser.find_by_text(row['text'])
    # for every row in context.table
        # assert that an element is in the list with the text row['text'] find_by_text


@when(u'I click the add button')
def impl(context):
    context.browser.find_by_css('.context').click()


@when(u'I type some text into the text entry box')
def impl(context):
    context.browser.find_by_test(row['test']


@then(u'a text entry box is visible')
def impl(context):
    assert context.browser.find_by_tag('textarea')


@when(u'I visit the website')
def impl(context):
    context.browser.visit(context.config.server_url)


@then(u'some text is visible')
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row['text'])


@then(u'an Add button is visible')
def impl(context):
    assert context.browser.find_by_css('add').click()
