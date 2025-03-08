import pytest
from src.text import Text
from src.text_preprocessor import TextPreprocessor


# Example test for the Text class
def test_text_initialization():
    text_processor = TextPreprocessor(chunk_size=10)
    text_instance = Text("Hello world! This is a test.", text_processor)

    # Assert that __text is a list
    assert isinstance(text_instance._Text__text, list)

    # Assert that the chunk size is respected
    assert all(len(chunk) <= 10 for chunk in text_instance._Text__text)


def test_append_phrase():
    text_processor = TextPreprocessor(chunk_size=10)
    text_instance = Text("Hello world!", text_processor)

    # Append a phrase
    text_instance.append_phrase("This is a new phrase.")

    # Check if new text has been appended correctly
    assert "This" in text_instance._Text__text
    assert "new" in text_instance._Text__text
    assert "phrase." in text_instance._Text__text
