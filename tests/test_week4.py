# test_always_passes:
name = 'ism3232'
assert 2 + 2 == 4

# test_string_is_lowercase
assert name == 'ism3232' .lower()
# test_path_segments
path = 'a/ism3232/b'
print(path)
parts = path.split('/')
print(parts)
assert 'ism3232' in parts