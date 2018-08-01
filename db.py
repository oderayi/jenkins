import sqlite3


class db:

  db_name = "jenkins.db"

  def insert(conn, row):
      conn.execute('insert into jobs (job_name, date_checked) values (?, ?)',
                (row['job_name'], row['date_checked']))
      conn.commit()
      conn.close()


  def retrieve(conn, job_name):
      cursor = conn.execute('select * from jobs where job_name = ?', (job_name,))
      record = cursor.fetchone()
      conn.close()
      return record


  def update(conn, row):
      conn.execute('update jobs set date_checked = ? where job_name = ?',
                (row['date_checked'], row['job_name']))
      conn.commit()
      conn.close()


  def delete(conn, job_name):
      conn.execute('delete from jobs where job_name = ?', (job_name,))
      conn.commit()
      conn.close()


  def disp_rows(conn):
      cursor = conn.execute('select * from jobs order by job_name')
      for row in cursor:
          print('{}: {}'.format(row['job_name'], row['date_checked']))
      conn.close()


  def create_tables():
      conn = init()
      conn.row_factory = sqlite3.Row
      print('Creating table: jobs (if it does not already exist:')
      conn.execute('create table if not exists jobs ( id integer primary key autoincrement, job_name text, date_checked datetime )')
      conn.commit()
      conn.close()


  def init():
      conn = sqlite3.connect(db_name)
      create_tables()
      return conn
