import sqlite3
import argparse



connection = sqlite3.connect("db.sqlite3")
cursor=connection.cursor()

def getColumnNames(tableName):
    cursor.execute(f'PRAGMA table_info({tableName})')
    columns_list = cursor.fetchall() # fetchall return a list tuples
    columns_list = [col[1] for col in columns_list]  # Use index 1 to get column names
    column_names= ', '.join(columns_list)
    return column_names

def preparedQuery(tableName,columnName):
    if tableName == 'COMPANIES':
        insert_query= f'INSERT INTO {tableName} ({columnName}) VALUES(?,?)'
    elif tableName == 'HOLIDAY':
        insert_query= f'INSERT INTO {tableName} ({columnName}) VALUES(?,?,?,?)'
    return insert_query



# One Row at a time
def insertValues(tableName,values):
   
   if tableName == 'COMPANIES':
      column_names= getColumnNames(tableName)
      insert_query = preparedQuery(tableName,column_names )
      cursor.execute(insert_query,(values[0],values[1]))
      connection.commit()

   elif tableName == 'HOLIDAY':
      column_names= getColumnNames(tableName)
      insert_query = preparedQuery(tableName,column_names )
      cursor.execute(insert_query,(values[0],values[1],values[2],values[3]))
      connection.commit()





       



def main():
    parser = argparse.ArgumentParser(description='Enter the table for given values')
    parser.add_argument('tableName',type=str, help="The table you are putting the values in")
    parser.add_argument('values',nargs='+',type=str,help="Enter the values you want to insert")
    args=parser.parse_args()
    tableName=args.tableName
    values=args.values
    insertValues(tableName,values)

if __name__ == '__main__':
    main()
