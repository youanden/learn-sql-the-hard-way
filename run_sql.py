#!/usr/bin/python

# chmod +x this file for this syntax:
# ./run_sql.py [dbname.db] [sqlfile_n.sql]...
# Otherwise,
# python run_sql.py [dbname.db] [sqlfile_n.sql]...

import sqlite3
import sys
import os

# Hold constant variables
DBS_DIR = 'dbs/'
SQL_DIR = 'sql/'
DEBUG = False

def main():
  # Checks
  checkArgsExist()
  cleanArgs()
  cleanDbs()

  db_path = isDbFile( sys.argv.pop( 0 ), True )

  # SQL Processing
  print '{:-^50}'.format( 'Processing SQL' )
  for sql_file_path in sys.argv:
    if( isSqlFile( sql_file_path ) ):
      processSqlFile( db_path, sql_file_path )

def processSqlFile( db_path, sql_file_path ):
  print '{:^50}'.format(
    'Processing ' +
    SQL_DIR + sql_file_path +
    ' to '  +
    DBS_DIR + db_path )

  qry_file = open( SQL_DIR + sql_file_path, 'r' ).read()
  con = sqlite3.connect( DBS_DIR + db_path )
  c   = con.cursor()
  queries = qry_file.split(';')

  for query in queries:
    try:
      c.execute( query )
    except sqlite3.OperationalError:
      exit('Check if db table exists, or for syntax errors')

  con.commit()
  c.close()
  con.close()

def checkArgsExist():
  if( len( sys.argv ) == 1 ):
    print '{:-^50}'.format( 'No Data' )
    exit( 0 )

def isSqlFile( sql_file ):
  if( sql_file[-4:] == '.sql' ):
    return True

def isDbFile( db_file, required=False ):
  if( db_file[-3:] == '.db' ):
    return db_file
  elif( required ):
    exit( "Invalid DB file specified" )

def cleanArgs():
  # Remove called script
  sys.argv.pop( 0 )

def cleanDbs():
  if( DEBUG ):
    for db_file in os.listdir( DBS_DIR ):
      file_path = os.path.join( DBS_DIR , db_file)
      if( not isDbFile( file_path ) ):
        continue
      try:
        if os.path.isfile( file_path ):
          os.unlink( file_path )
      except Exception, e:
        print e

main()