from behave import when, then


@when(u'I click the show_more button')
def impl(context):
    context.browser.find_by_css('a[href^="/tweety/pagination/"]').click()


def get_text_entry_box(context):
    return context.browser.find_by_tag('textarea')


def get_add_button(context):
    return context.browser.find_by_css('input[type=submit]')


@when(u'I add some tweets')
def impl(context):
    for row in context.table:
        get_text_entry_box(context).fill(row['tweet'])
        get_add_button(context).click()


@then(u'I can see more than five tweets')
def impl(context):
    tweets = context.browser.find_by_css('li.tweet')
    assert len(tweets) > 5


@then(u'I see only five tweets')
def impl(context):
    tweets = context.browser.find_by_css('li.tweet')
    assert len(tweets) == 5
