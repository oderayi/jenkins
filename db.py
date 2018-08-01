import sqlite3

db_name = "jenkins.db"


def insert(db, row):
    db.execute('insert into jobs (job_name, date_checked) values (?, ?)',
               (row['job_name'], row['date_checked']))
    db.commit()
    db.close()


def retrieve(db, job_name):
    cursor = db.execute('select * from jobs where job_name = ?', (job_name,))
    record = cursor.fetchone()
    db.close()
    return record


def update(db, row):
    db.execute('update jobs set date_checked = ? where job_name = ?',
               (row['date_checked'], row['job_name']))
    db.commit()
    db.close()


def delete(db, job_name):
    db.execute('delete from jobs where job_name = ?', (job_name,))
    db.commit()
    db.close()


def disp_rows(db):
    cursor = db.execute('select * from jobs order by job_name')
    for row in cursor:
        print('{}: {}'.format(row['job_name'], row['date_checked']))
    db.close()


def create_tables():
    db = init()
    db.row_factory = sqlite3.Row
    print('Creating table: jobs (if it does not already exist:')
    db.execute('create table if not exists jobs ( id integer primary key autoincrement, job_name text, date_checked datetime )')
    db.commit()
    db.close()


def init():
  db = sqlite3.connect(db_name)
  create_tables()
  return db
