def test_always_passes():
    assert 2 + 2 == 4


def test_string_is_lowercase():
    name = "ism3232"
    assert name == name.lower()


def test_path_segments():
    path = "a/ism3232/b"
    print(path)
    parts = path.split("/")
    print(parts)
    assert "ism3232" in parts
