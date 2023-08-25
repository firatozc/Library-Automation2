# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 20:00:32 2023

@author: User
"""

import sqlite3 as sql

conn=sql.connect("datas.db")
cursor = conn.cursor()


cursor.execute(""" CREATE TABLE IF NOT EXISTS BOOK_INFO(
    id INTEGER PRIMARY KEY,
    book_name TEXT,
    author_name TEXT,
    number_of_pages INTEGER,
    edition_number INTEGER,
    publishing_house INTEGER,
    is_taken text
        ) 
""")


cursor.execute(""" CREATE TABLE IF NOT EXISTS PASSWORDS(
    id INTEGER PRIMARY KEY,
    NAME TEXT,
    SURNAME TEXT,
    PASSWORD TEXT
        )
               
               """)
               
cursor.execute(""" CREATE TABLE IF NOT EXISTS USER_INFO(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    phone_number INTEGER,
    mail TEXT,
    AGE INTEGER
        )
               
               """)

cursor.execute("""DELETE FROM PASSWORDS WHERE NAME = 'neval' """)  ## DELETE FOR EMPTY DATAS



# datas=[('Berk','Uysalgil','berk123'),('Fırat','Özcan','fırat456'),('Mustafa Selim','Ateşmen','selim789')]

# add_command = """ INSERT INTO PASSWORDS (NAME,SURNAME,PASSWORD) VALUES {} """
# for data in datas:
#     cursor.execute(add_command.format(data))


# datas2 = [('Berke','Balcı',5437472416,'brklc@gmail.com',21),('Mehmet','Tunca',5383428028,'mehmettnc@hotmail.com',19),('Aleyna','Kenar',5468666401,'aleynknr22@outlook.com',20),
#           ('Ebru','Yaşlı',5454166637,'ebrumyasli@gmail.com',24),('Üzeyir Can','Toksöz',5438461543,'uzutoksoz22@hotmail.com',19),('İlayda','Kaya',5458265657,'leydiaknr123@gmail.com',17),
#           ('Alper','Günday',5212665894,'alpr_gnd@gmail.com',34),('Mustafa','Yılmaz',5693655127,'mustafylmz@gmail.com',26),('Arslan','Karaduman',5388300385,'drarslan-kara25@gmail.com',36),
#           ('Esin','Karabulut',5630650085,'esnblackcloud@outlook.com',24),('Alp','Durmaz',5212658475,'alp_durmaz06@gmail.com',29),('Beyza','Sarı',5365063241,'beyza_yellow@hotmail.com',16),
#           ('Çağrı','Kahveci',5346859124,'cagrkahve@gmail.com',31),('Sıla','Kaynarca',5638666498,'silakayn@outlook.com',18),('Bora','Kulaksızoğlu',5192845967,'borawithoutear@gmail.com',21),
#           ('Aybüke','Özdemir',5648563689,'aybuk_ozdemir@hotmail.com',23),('Elif','Afacan',5749582648,'eliffacan49@gmail.com',20),('Mustafa','Özcan',5438266399,'mustafaozc12@gmail.com',20)]

# add_command2 = """INSERT INTO USER_INFO (name,surname,phone_number,mail,AGE) VALUES {} """
# for data in datas2:
#     cursor.execute(add_command2.format(data))

# datas3 = [('Bin Dokuz Yüz Seksen Dört','George Orwell',352,73,'Can Yayınları'),('Sefiller','Victor Hugo',1724,50,'Iş Bankası Kültür Yayınları'),('Suç Ve Ceza','Fyodor Mihayloviç Dostoyevski',1100,98,'Iş Bankası Kültür Yayınları'),
#           ('Anna Karenina','Tolstoy',1062,13,'Iş Bankası Kültür Yayınları'),('Şeker Portakalı','José Mauro de Vasconcelos',184,152,'Can Yayınları'),('Uçurtma Avcısı','Fyodor Mihayloviç Dostoyevski',1100,98,'Everest Yayınları'),
#           ('Çalıkuşu','Reşat Nuri Güntekin',544,64,'Inkılap-Kitabevi'),('Tutunamayanlar','Oğuz Atay',724,110,'Iletişim Yayınları'),('Küçük Prens','Antoine-de-Saint-Exupéry',115,8,'Altın-Kitaplar'),
#           ('Hayvan Çiftliği','George-Orwell',104,1,'Iş Bankası Kültür Yayınları'),('Beyaz Zambaklar Ülkesi','Grigory-Petrov',140,7,'Can Yayınları'),('Zaman Makinesi','H-G-Wells',144,19,'Ithaki Yayınevi'),
#           ('Suç Ve Ceza','Fyodor Mihayloviç Dostoyevski',1050,30,'Can Yayınları'),('Bin Dokuz Yüz Seksen Dört','George Orwell',352,1,'Iş Bankası Kültür Yayınları'),('Suç Ve Ceza','Fyodor Mihayloviç Dostoyevski',1100,24,'Akvaryum-Yayınları'),
#           ('Fareler Ve Insanlar','John-Steinbeck',126,11,'Sel Yayınları'),('Don Kişot','Miguel-De-Cervantes-Saavedra',430,2,'Koridor Yayıncılık'),('Hamlet','William-Shakespeare',185,38,'Iş Bankası Kültür Yayınları')]

# add_command3 = """INSERT INTO BOOK_INFO (book_name,author_name,number_of_pages,edition_number,publishing_house) VALUES {}"""
# for data in datas3:
#     cursor.execute(add_command3.format(data))

conn.commit()
conn.close()




