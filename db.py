import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def query(string, dbname,search_path=None):
    con = psycopg2.connect("dbname=%s"%dbname)
    if search_path != None:
        sp='set search_path=%s;'%search_path
        stWpath= sp+string
    else:
        stWpath=string
    curs=con.cursor()
    sql=curs.mogrify(stWpath)
    try:
        curs.execute(sql)
    except Exception, e:
        print e.pgerror
        pass
    res = curs.fetchall()
    curs.close()
    return res


def create(name, origindb= 'postgres',template=None):
    con = psycopg2.connect("dbname=%s"%origindb)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    if template != None:
        createString= 'CREATE DATABASE "%s" TEMPLATE=%s'%(name,template)
    else:
        createString= 'CREATE DATABASE "%s"'%(name)        
    cur = con.cursor()
    cmd=cur.mogrify(createString)
    try:
        cur.execute(cmd)
    except Exception, e:
        print e.pgerror
        pass
    cur.close()
    con.close()

def drop(name, origindb= 'postgres'):
    con = psycopg2.connect("dbname=%s"%origindb)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    dropString= 'DROP DATABASE if exists "%s"'%(name)        
    cur = con.cursor()
    cmd=cur.mogrify(dropString)
    try:
        cur.execute(cmd)
    except Exception, e:
        print e.pgerror
        pass
    cur.close()
    con.close()

def queryCommit(string, dbname='afri',search_path='afri, solar, public'):
    con = psycopg2.connect("dbname=%s"%dbname)
    sp='set search_path=%s;'%search_path
    stWpath= sp+string
    curs=con.cursor()
    sql=curs.mogrify(stWpath)
    try:
        curs.execute(sql)
    except Exception, e:
        print e.pgerror
        pass
    #res = curs.fetchall()
    con.commit()
    curs.close()
    #return res

def sqliteQ(string,filename):
    '''
    string= query string
    filename= string file name
    '''
    import sqlite
    con=sqlite.connect(filename)
    c= con.cursor()
    #c.execute()
    c.execute(string)
    out=c.fetchall()
    c.close()
    return out


def sqliteQcommit(string,filename):
    '''
    string= query string
    filename= string file name
    '''
    import sqlite
    con=sqlite.connect(filename)
    c= con.cursor()
    c.execute(string)
    con.commit
    c.close()
