def test_reverse(text):
    for i, char in enumerate(text):
        print('%d: %s' % (len(text)-i, char))

test_reverse('Give it to me')
