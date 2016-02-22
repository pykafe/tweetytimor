from behave import when, then


@then(u'I see the five comment of tweety')
def impl(context):
    for row in context.table:
        assert context.browser.find_by_text(row['text'])


@then(u'I see the button show_more')
def impl(context):
    show_more_button = context.browser.find_by_css('a[href^="/tweety/pagination/"]')
    assert show_more_button


@when(u'I click the show_more button')
def impl(context):
    show_more_button = context.browser.find_by_css('a[href^="/tweety/pagination/"]').click()


@then(u'I can see all of the tweety comments')
def impl(context):
    tweetlist = context.browser.find_by_tag('ul').first
    assert tweetlist.visible
    for row in context.table:
        assert tweetlist.find_by_text(row['text']).visible
