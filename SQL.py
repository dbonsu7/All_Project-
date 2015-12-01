import mysql.connector
conn = mysql.connector.connect(user="root", password = "arsenal", host = "localhost", database = 'allproject')
mycursor = conn.cursor()

mycursor.execute("""INSERT INTO users VALUES
(1,
"Daniel",
"46fee5217f7a58cb ",
"12:44:30" , 
1.2720693 ,
6.583606 ,
6.8299093 ,
3 ,
"Acc" ,
1)""")


mycursor.execute("""INSERT INTO users VALUES
(2,
"Briyangha",
"46fee5217f7a58cb ",
"12:20:33",
1.2313678 ,
 6.696133  ,
6.8299345 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(3,
"Kishen",
"46fee5217f7a58cb ",
"12:27:36 ",
0.37424365 ,
 6.77993 ,
6.116437 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(4,
"Jack",
"46fee5217f7a58cb ",
"12:44:39",
-4.004751 ,
 5.1351137 ,
7.409306 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(5,
"Pindi",
"46fee5217f7a58cb ",
"12:16:42 ",
0.20664953 ,
 7.9052052 ,
1.7446249 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(6,
"Matt",
"46fee5217f7a58cb ",
" 12:44:45",
-2.446126 ,
 6.0808234 ,
8.833856 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(7,
"Tony",
"46fee5217f7a58cb ",
"12:44:48",
-0.274585 ,
 8.419958 ,
6.252907 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(8,
"Jay",
"46fee5217f7a58cb ",
" 12:44:54",
0.40536827 ,
 7.0768113 ,
6.9496193 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(9,
"Kajaal",
"46fee5217f7a58cb ",
" 12:44:55",
6.583606  ,
 7.0887823 ,
6.8299093 ,
 3 ,
"Acc ",
1)""")

mycursor.execute("""INSERT INTO users VALUES
(10,
"Jack",
"46fee5217f7a58cb ",
" 12:44:55",
1.2313678 ,
7.445219 ,
6.9280715 ,
 3 ,
"Acc ",
1)""")

##mycursor.execute("""INSERT INTO users VALUES
##(11,\
##"Paula",\#
##"46fee5217f7a58cb ",\
##" 12:47:55",\
##"0.37424365 ",\
##"6.77993 ",\
##"6.116437 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(12,\
##"Rob",\
##"46fee5217f7a58cb ",\
##" 12:44:55",\
##"-4.004751 ",\
##" 5.1351137 ",\
##"7.409306 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(13,\
##"Katy",\
##"46fee5217f7a58cb ",\
##" 12:20:55",\
##"0.20664953 ",\
##" 7.9052052 ",\
##"6.9280715 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(14,\
##"Maria ",\
##"46fee5217f7a58cb ",\
##"12:50:55",\
##"-2.446126 ",\
##"6.0808234 ",\
##"8.833856 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(15,\
##"Vadsika",\
##"46fee5217f7a58cb ",\
##" 12:50:40",\
##"-0.274585 ",\
##"8.419958 ",\
##"6.252907 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(16,\
##"Chris",\
##"46fee5217f7a58cb ",\
##" 12:30:55",\
##"0.40536827 ",\
##" 7.0528693 ",\
##"6.9280715 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(17,\
##"Sora",\
##"46fee5217f7a58cb ",\
##" 12:30:34",\
##"1.2720693 ",\
##"6.583606 ",\
##"6.8299093 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(18,\
##"Michael",\
##"46fee5217f7a58cb ",\
##" 12:26:45",\
##"1.2313678 ",\
##"6.696133  ",\
##"7.445219 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(19,\
##"Andre",\
##"46fee5217f7a58cb ",\
##"12:10:14",\
##"-2.446126 ",\
##"6.0808234  ",\
##"8.833856 ",\
##" 3 ",\
##"Acc ",\
##"1")""")
##
##mycursor.execute("""INSERT INTO users VALUES
##(20,\
##"Reginald",\
##"46fee5217f7a58cb ",\
##"12:10:14",\
##"1.2313678 ",\
##"6.696133   ",\
##"7.445219 ",\
##" 3 ",\
##"Acc ",\
##"1")""")

conn.commit()
