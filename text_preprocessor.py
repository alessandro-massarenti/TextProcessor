class TextPreprocessor:


    def __init__(self, chunk_size: int):
        self.__chunk_size = chunk_size
        self.__translations: list= []

    def chunked_text(self, text: str) -> list[str]:
        return [text[i:i + self.__chunk_size] for i in range(0, len(text), self.__chunk_size)]

    def add_word_to_replace(self,words: list[str]):
        self.__translations.append(words)
        # TODO: can be a lot better