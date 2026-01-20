from database.DB_connect import DBConnect
from model.artist import Artist

class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT a.id, a.name
                    FROM artist a
                    
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_artists_maggiore_di_n(n_alb):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT a.id, a.name
                    FROM artist a, album alb
                    WHERE a.id = album.artist_id
                    GROUP BY a.id
                    HAVING COUNT(alb.artist_id) >=%s)
                        
                    
                """
        cursor.execute(query,(n_alb))
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result




    @staticmethod
    def get_genere_per_artista(artist_id):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT DISTINCT t.genre_id
                FROM playlist_track t, genre g 
                WHERE t.genre_id = g.id
                AND t.artist_id = %s
                
                


                """
        cursor.execute(query, (artist_id,))
        for row in cursor:
            genere = (row['genre_id'])
            result.append(genere)
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def get_artist_with_d_min(artist_id,d_min):

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT COUNT(*) AS conto
                FROM track t, album alb
                WHERE t.album_id = alb.id 
                AND alb.artist_id = %s
                AND t.milliseconds >= %s    




                """
        cursor.execute(query, (artist_id,d_min*60000,))
        for row in cursor:
            conto = (row['conto'])
            result.append(conto)
        cursor.close()
        conn.close()
        return result['conto']>0
