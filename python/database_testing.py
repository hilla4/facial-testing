import sqlite3
from sqlite3 import Error

with sqlite3.connect('database') as conn:
    def create_table(create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)


    def select_all_users():
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")

        rows = cur.fetchall()

        for row in rows:
            print(row)


    def delete_all_tasks():
        """
        Delete all rows in the tasks table
        :param conn: Connection to the SQLite database
        :return:
        """
        sql = 'DELETE FROM user'
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()


    def select_name_users():
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT id FROM user")

        rows = cur.fetchall()

        for row in rows:
            print(row)


    def select_email_users():
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT email FROM user")

        rows = cur.fetchall()

        for row in rows:
            return row


    def select_phone_users():
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT phoneNum FROM user")

        rows = cur.fetchone()

        return rows
        #for row in rows:
         #   print(row)


    def insert_test(user):
        """
            Create a new task
            :param conn:
            :param user:
            :return:
            """
        sql = ''' INSERT INTO user(id,email,phoneNum)
                          VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, user)
        return cur.lastrowid


    def main():
        sql_create_user_table = """ CREATE TABLE IF NOT EXISTS user (
                                                id text PRIMARY KEY,
                                                email text,
                                                phoneNum integer
                                            ); """
        # create a database connection
        conn = create_connection('database')

        # create tables
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_user_table)

        else:
            print("Error! cannot create the database connection.")
        return conn
        # user = ('Aidan', '4123289513', 'aidanhill61@gmail.com')
        # user2 = ('Not Aidan', '9999999999', 'hello@yahoo.com')
        # insert_test(conn, user)
        # insert_test(conn, user2)
        # select_all_users(conn)
        # select_name_users(conn)
        # select_phone_users(conn)
        # select_email_users(conn)


if __name__ == '__main__':
    main()
