import psycopg2
from sentence_transformers import SentenceTransformer


class TextProcessor:

    def __init__(self, db_connection):
        self.__db_connection = db_connection
        self.__model = SentenceTransformer("distiluse-base-multilingual-cased-v1")
        self.__log = []

    def _embedding(self, text: str) -> str:
        embedding = self.__model.encode(text)
        vector = '[' + ','.join(map(str, embedding)) + ']'
        return vector


    def insert_text(self, text: str) -> str:

        insert_data_sql = """
        INSERT INTO phrases (phrase, embedding)
        VALUES (%s, %s);
        """

        cursor = self.__db_connection.cursor()
        vector = self._embedding(text)
        cursor.execute(insert_data_sql, (text, vector))

        self.__db_connection.commit()
        return vector

    def get_similar_text(self, text: str) -> str:

        cursor = self.__db_connection.cursor()

        # Step 3: Use the '<=>' operator to calculate the similarity (cosine similarity by default)
        # and order the results to find the most similar phrase.
        select_sql = """
                SELECT phrase
                FROM phrases
                ORDER BY embedding <=> %s
                LIMIT 1;
                """

        vector = self._embedding(text)

        # Execute the query with the generated embedding
        cursor.execute(select_sql, vector)

        # Step 4: Fetch the result (most similar text)
        result = cursor.fetchone()[0]
        return result


if __name__ == '__main__':
    conn = psycopg2.connect(
        database="telegram",
        host="127.0.0.1",
        user="telegram",
        password="pizzapizza"
    )
    text_processor = TextProcessor(conn)
    print(text_processor.get_similar_text('mega prova'))
