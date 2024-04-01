import psycopg2

class Leaderboard_Controller:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_top_scores_html_table(self, n):
        top_scores = self.get_top_n_scores(n)
        html_table = "<table border='1'>\n"
        html_table += "<tr><th>Score ID</th><th>Player ID</th><th>Score</th></tr>\n"
        for score in top_scores:
            html_table += f"<tr><td>{score[0]}</td><td>{score[1]}</td><td>{score[2]}</td></tr>\n"
        html_table += "</table>"
        return html_table

    def get_top_n_scores(self, n):
        query = f"""
            SELECT score, final_time, player_ID
            FROM Game_Score
            ORDER BY score DESC
            LIMIT {n};
        """
        return self._execute_query(query)

    def _execute_query(self, query):
        cursor = self.db_connection.cursor()
        cursor.execute(query)
        scores = cursor.fetchall()
        cursor.close()
        return scores