from behave import then


@then(u'I see the text')  # noqa
def impl(context):
    assert context.browser.is_text_present('text')
    return True
