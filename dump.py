# Convert file existing_db.db to SQL dump file dump.sql
import sqlite3
import sys
import os
import datetime

if __name__ == "__main__":
    while True:
        print("This script will try to dump the given db")
        ans = input("y/n? ")
        if ans.lower() == 'y':
            print("Continuing...")
            break
        elif ans.lower() == 'n':
            print("Stopped")
            exit(1)
    print() #newline comodo

    try:
        dbname = sys.argv[1]
        print("using db:", dbname)
    except:
        print("Missing dbname")
        exit(1)

    try:
        con = sqlite3.connect(dbname)
        #for line in con.iterdump():
        #    print('%s' % line)

        dumpname = "dump-" + os.path.basename(os.path.splitext(dbname)[0]) + "-" + str(datetime.datetime.now()).replace(":",".") + ".sql"
        print("Dumping db on \"", dumpname, "\"", sep="")
        with open(dumpname, 'w', encoding='utf-8') as f:
            f.write("SET SESSION sql_mode = 'ANSI';\n")
            f.write("drop database if exists test_bot;\n")
            f.write("create database if not exists test_bot;\n")
            f.write("use test_bot;\n")

            for line in con.iterdump():
                #print(line)
                f.write('%s\n' % line.replace("\\", "\\\\")
                                    .replace("option ", "\"option\" ")
                                    .replace("BEGIN TRANSACTION;", "START TRANSACTION;")
                                    .replace("VARCHAR", "VARCHAR(64)")
                        )
        print("Dumped!")
        
        con.close()
    except Exception as e:
        print("Fatal error", e)
        exit(1)
    else:
        print("Success!")

