import mysql.connector
import random
def get_scores_with_users(score):
    connection = None
    try:
        # Establishing connection to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",  # Replace with your MySQL username
            password="",  # Replace with your MySQL password
            database="geoguessr"
        )
        
        if connection:
            # Creating a cursor to execute SQL queries
            cursor = connection.cursor()

            # Fetching the 5 scores above and below the given score
            query = ("SELECT g.score, p.username "
                     "FROM game_score g "
                     "JOIN player p ON g.playerID = p.playerID "
                     "WHERE g.score >= %s "
                     "ORDER BY g.score ASC "
                     "LIMIT 6")
            cursor.execute(query, (score,))
            rows_above = cursor.fetchall()

            query = ("SELECT g.score, p.username "
                     "FROM game_score g "
                     "JOIN player p ON g.playerID = p.playerID "
                     "WHERE g.score < %s "
                     "ORDER BY g.score DESC "
                     "LIMIT 5")
            cursor.execute(query, (score,))
            rows_below = cursor.fetchall()

            # Combine and sort the lists
            all_scores = rows_below[::-1] + [(score, "Current User")] + rows_above[1:]
            all_scores_sorted = sorted(all_scores, key=lambda x: x[0])

            return all_scores_sorted

    except mysql.connector.Error as error:
        print("Error while connecting to the database:", error)
        return None

    finally:
        if connection:
            # Closing the database connection
            connection.close()

# Example usage
if __name__ == "__main__":
    target_score = random.randint(100,800)
    scores_with_users = get_scores_with_users(target_score)
    if scores_with_users:
        for score, username in scores_with_users:
            print(f"Score: {score}, User: {username}")
