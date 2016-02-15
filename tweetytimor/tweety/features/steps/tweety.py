from behave import when, then


@then(u'the tweety text is visible') #noqa
def impl(context):
    context.browser.find_by_css('.container.ul.li')

@when(u'I click the add button') #noqa
def impl(context):
    context.browser.find_by_id('submit').click()

@when(u'I type some text into the text entry box') #noqa
def impl(context):
    context.browser.find_by_id('id_comment').fill('Diak ka lae?\r')

@then(u'a text entry box is visible') #noqa
def impl(context):
    assert context.browser.find_by_id('id_comment')

@when(u'I visit the website') #noqa
def impl(context):
    context.browser.visit(context.config.server_url)

@then(u'some text is visible') #noqa
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row['text'])

@then(u'an Add button is visible') #noqa
def impl(context):
    assert context.browser.find_by_id('submit')
