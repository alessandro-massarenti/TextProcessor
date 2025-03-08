from text_preprocessor import TextPreprocessor


class Text:

    def __init__(self, text: str, text_processor: TextPreprocessor):
        self.__text_preprocessor = text_processor
        self.__text: list = self.__text_preprocessor.chunked_text(text)

    def change_text_preprocessor(self, text_processor: TextPreprocessor):
        self.__text_preprocessor = text_processor

    def append_phrase(self, text: str) -> None:
        self.__text.append(self.__text_preprocessor.chunked_text(text))

    def translate(self):
        full_text = " ".join(self.__text)
        translated_text = self.__text_preprocessor.replaced_text(full_text)
        self.__text = self.__text_preprocessor.chunked_text(translated_text)

    def __str__(self) -> str:
        return " ".join(self.__text)



