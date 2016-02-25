from behave import then


@then(u'I see the text')  # noqa
def impl(context):
    for row in context.table:
        assert context.browser.is_text_present(row['text'])
