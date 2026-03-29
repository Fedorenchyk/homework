def second_index(text, some_str):
    f_index = text.find(some_str)
    s_index =text.find(some_str, f_index+1)
    if s_index <= 0:
        text.find
        return None
    return s_index
print(second_index('hi',  'h'))

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
