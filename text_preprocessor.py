import re


class TextPreprocessor:


    def __init__(self, chunk_size: int = 300):
        self.__chunk_size = chunk_size
        self.__translations: dict[str, str] = {}

    import re

    def chunked_text(self, text: str) -> list[str]:
        words = re.findall(r'\S+|\n', text)  # Matches words and newlines separately
        chunks: list[str] = []
        current_chunk = []
        current_length = 0

        for word in words:
            word_length = len(word)

            # If adding this word exceeds the chunk size, start a new chunk
            if current_length + word_length > self.__chunk_size:
                chunks.append(" ".join(current_chunk))
                current_chunk = []
                current_length = 0

            # Start new chunk for newlines
            if word == "\n":
                chunks.append(" ".join(current_chunk))  # Save the current chunk
                chunks.append("\n")  # Store the newline as its own chunk
                current_chunk = []
                current_length = 0
                continue  # Skip adding the newline to the next chunk

            current_chunk.append(word)
            current_length += word_length + 1  # +1 accounts for spaces

        # Add the last chunk if not empty
        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def add_word_to_replace(self,words: dict[str: str]):
        self.__translations.update(words)

    def replaced_text(self, text: str) -> str:
        pattern = r'\b(' + '|'.join(re.escape(key) for key in self.__translations.keys()) + r')\b'
        return re.sub(pattern, lambda m: self.__translations.get(m.group().lower(), m.group()), text)
