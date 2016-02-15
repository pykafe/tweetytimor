from behave import when, then


@when(u'I visit the website')
def impl(context):
    context.browser.visit(context.config.server_url)


@then(u'some text is visible')  # noqa
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row['text']).visible


def get_text_entry_box(context):
    return context.browser.find_by_tag('textarea')


def get_add_button(context):
    return context.browser.find_by_css('input[type=submit]')


@then(u'a text entry box is visible')  # noqa
def impl(context):
    assert get_text_entry_box(context).visible


@then(u'an Add button is visible')  # noqa
def impl(context):
    assert get_add_button(context).visible


@when(u'I type some text into the text entry box')  # noqa
def impl(context):
    textarea = get_text_entry_box(context)
    for row in context.table:
        # fill the textarea with text
        textarea.fill(row['text'])


@when(u'I click the add button')  # noqa
def impl(context):
    get_add_button(context).click()


@then(u'the tweety text is visible')  # noqa
def impl(context):
    # find a list in the page - find_by_tag - look for an unordered list tag 'ul'
    # assign that list to a variable so we can use it later 'tweetlist'
    tweetlist = context.browser.find_by_tag('ul').first
    # assert that we have found that list
    assert tweetlist.visible
    # for every row in context.table
    for row in context.table:
        # assert that an element is in the list with the text row['text'] find_by_text
        assert tweetlist.find_by_text(row['text']).visible
