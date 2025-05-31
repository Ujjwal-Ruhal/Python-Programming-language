# Module 12: Building Database Apps with PostgreSQL & Python

import psycopg2

def table():
    conn = psycopg2.connect( dbname = "postgres" , user = "postgres" , password = "Ujjwal@013" , host = "localhost" , port = "5432" )

    # print('connected successfully')

    cursor = conn.cursor()
    cursor.execute(''' create table employee( Name text , ID int , Age int , Sector text); ''')
    print('Table created successfully')

    conn.commit()
    conn.close()

# def data():
#     conn = psycopg2.connect( dbname = "postgres" , user = "postgres" , password = "Ujjwal@013" , host = "localhost" , port = "5432" )

#     cursor = conn.cursor()
#     cursor.execute(''' insert into employee( Name , ID , Age , Sector ) values ('Aman',01,22,'IT'); ''')
#     print('Data added successfully')

#     conn.commit()
#     conn.close()
def data():
    conn = psycopg2.connect( dbname = "postgres" , user = "postgres" , password = "Ujjwal@013" , host = "localhost" , port = "5432" )

    cursor = conn.cursor()

    name = input('enter name: ')
    id = input('enter id: ')
    age = input('enter age: ')
    sector = input('enter sector: ')

    query = ''' insert into employee( Name , ID , Age , Sector ) values ( %s , %s , %s , %s); '''
    cursor.execute( query, (name , id , age , sector))
    print('Data added successfully')

    conn.commit()
    conn.close()

def extract():

    conn = psycopg2.connect( dbname = "postgres" , user = "postgres" , password = "Ujjwal@013" , host = "localhost" , port = "5432" )

    cursor = conn.cursor()
    cursor.execute(''' SELECT * FROM employee; ''')
    # print(cursor.fetchone()) # .fetchone -> fetch the data from database
    show = cursor.fetchone()
    print(show[0])

    conn.commit()
    conn.close()
    
data()
