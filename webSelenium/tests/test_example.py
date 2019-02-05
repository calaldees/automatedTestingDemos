
def test_example(selenium):
    selenium.get('http://www.example.com')
    assert 'Example' in selenium.title
    assert 'example' in selenium.page_source.lower()
