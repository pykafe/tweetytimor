
@then(u'typing text into the entry box changes the character count displayed')  # noqa
def impl(context):
    textarea = get_text_entry_box(context)
    for row in context.table:
        # fill the textarea with text
        textarea.fill(row['text'])
        assert context.browser.is_text_present(row['count'])


def get_text_entry_box(context):
    return context.browser.find_by_tag('textarea')
