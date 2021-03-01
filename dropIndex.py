# prende un db sqlite e elimina tutti gli indici che contiene.
# Questo viene fatto poiché se gli indici sono creati a ...
# il db potrebbe non essere trasferito su altri sistemi SQL
import sqlite3
import sys
import os

def usageHelp():
    print("Usage:")
    print("\t{} <path/to/sqlite.db>".format(os.path.relpath(sys.argv[0])))

if __name__ == "__main__":

    # controllo dei parametri
    try:
        dbname = sys.argv[1]
        print("using db:", dbname)
    except:
        print("Missing dbname")
        usageHelp()
        exit(1)

    while True:
        print("This script will try to delete all index from the given db")
        ans = input("y/n? ")
        if ans.lower() == 'y':
            print("Continuing...")
            break
        elif ans.lower() == 'n':
            print("Stopped")
            exit(1)
    print() #newline comodo

    try:
        conn = sqlite3.connect(dbname)
        print("Succefully connected to db")
    
        c = conn.cursor()
        print("Cursor created")

        index_query = "SELECT name FROM sqlite_master WHERE type == 'index'"
        delete_query = "DROP INDEX IF EXISTS " # concatenazione vecchio stile

        data_c = list(c.execute(index_query))

        for index in data_c:
            print("deleting", index)
            c.execute(delete_query + index[0])
            print("Indexes successfully deleted")

        
        
    
        conn.close()
        print("Conncection successfully closed")
    except Exception as e:
        print("Fatal error", e)
        exit(1)
    else:
        print("Success!")
    
