# Better Way #16

def index_words(text):
    result = []
    if text:
        result.append('True')
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index+1)
    return result, index

address = 'Four score and seven years ago...'
result = index_words(address)
print(result[:3])

# print(index_words('anything '))

'''
i = input('input: ')
p = index_words(i)
print(p)
'''


'''
def test(text):
    result = []
    for index, letter in enumerate(text):
        result.append(index)
    return result

print(test('Everlasting'))
'''