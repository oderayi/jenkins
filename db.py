import sqlite3

class db:

  db_name = "jenkins.db"

  def insert(self, conn, row):
      conn.execute('insert into jobs (job_name, job_status, date_checked) values (?, ?, ?)',
                   (row['job_name'], row['job_status'], row['date_checked']))
      conn.commit()
      conn.close()

  def retrieve(self, conn, job_name):
      cursor = conn.execute('select * from jobs where job_name = ?', (job_name,))
      record = cursor.fetchone()
      conn.close()
      return record

  def update(self, conn, row):
      conn.execute('update jobs set date_checked = ?, job_status = ? where job_name = ?',
                   (row['date_checked'], row['job_status'], row['job_name']))
      conn.commit()
      conn.close()

  def delete(self, conn, job_name):
      conn.execute('delete from jobs where job_name = ?', (job_name,))
      conn.commit()
      conn.close()

  def disp_rows(self, conn):
      cursor = conn.execute('select * from jobs order by job_name')
      for row in cursor:
          print('{}: {} {}'.format(row['job_name'], row['job_status'], row['date_checked']))
      conn.close()

  def create_tables(self):
      conn = init()
      conn.row_factory = sqlite3.Row
      print('Creating table: jobs (if it does not already exist:')
      conn.execute('create table if not exists jobs ( id integer primary key autoincrement, job_name text, job_status text, date_checked datetime )')
      conn.commit()
      conn.close()

  def init(self):
      conn = sqlite3.connect(db_name)
      create_tables()
      return conn
