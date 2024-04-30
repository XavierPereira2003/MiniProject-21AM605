import psycopg2
from psycopg2 import sql

class DatabaseManager:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        return psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def populate_database(self, movie_details, persons, roles, directs):
        conn = self.connect()
        cursor = conn.cursor()

        for movie in movie_details:
            cursor.execute(sql.SQL(
                "INSERT INTO movies (movie_id, language, title, description, poster, director_id, release_date, vote_average) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            ), (
                movie['movie_id'],
                movie['language'],
                movie['title'],
                movie['description'],
                movie['poster'],
                movie['director'],
                movie['release_date'],
                movie['vote_average']
            ))

        for person in persons:
            cursor.execute(sql.SQL(
                "INSERT INTO persons (person_id, name, image, birth_date, biography) VALUES (%s, %s, %s, %s, %s)"
            ), (
                person['id'],
                person['name'],
                person['image'],
                person['birth_date'],
                person['biography']
            ))

        for role in roles:
            for person_id, character in role.items():
                cursor.execute(sql.SQL(
                    "INSERT INTO roles (movie_id, person_id, character) VALUES (%s, %s, %s)"
                ), (
                    role['id'],
                    person_id,
                    character
                ))

        for direct in directs:
            cursor.execute(sql.SQL(
                "INSERT INTO directs (movie_id, director_id) VALUES (%s, %s)"
            ), (
                direct['movie'],
                direct['id']
            ))

        conn.commit()
        cursor.close()
        conn.close()


