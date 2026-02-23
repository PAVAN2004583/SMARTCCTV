import sqlite3
import os
import getpass

db = r'c:\\Users\\pavan\\Desktop\\SMART CCTV\\data\\cctv.db'
pwd = getpass.getpass('Paste Google App Password (input hidden): ')
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute(\"UPDATE system_settings SET value=? WHERE key='smtpPass'\", (pwd,))
conn.commit()
conn.close()
print('smtpPass updated in DB')