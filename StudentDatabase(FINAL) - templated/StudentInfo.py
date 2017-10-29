__author__ = 'HARRIE'

import psycopg2

class Student:

    def __init__(self, row = None, inp_idnum = None):
        if row is not None:
            self._idnum = row[0]
            self._lname = row[1]
            self._fname = row[2]
            self._mname = row[3]
            self._gender = row[4]
            self._college_id = row[5]
            self._course_id = row[6]
            self._year_lvl = row[7]
            self._house_num = row[8]
            self._street = row[9]
            self._brgy = row[10]
            self._city = row[11]
            self._bdate = row[12]

        elif inp_idnum is not None:
            try:
                conn = psycopg2.connect(host="localhost",database="student_db", user="postgres", password="apipahdessopolao")
                cur = conn.cursor()

                cur.execute("SELECT idnum, (name).l_name AS l_name, (name).f_name AS f_name, (name).m_name AS m_name, " +
                                "gender, college_id, course_id, year_lvl, (address).house_num AS h_num, (address).street AS street, (address).brgy AS brgy, " +
                                "(address).city AS city, bdate FROM student where idnum = "+ str(inp_idnum))

                row = cur.fetchone()

                if row is not None:
                    self._idnum = row[0]
                    self._lname = row[1]
                    self._fname = row[2]
                    self._mname = row[3]
                    self._gender = row[4]
                    self._college_id = row[5]
                    self._course_id = row[6]
                    self._year_lvl = row[7]
                    self._house_num = row[8]
                    self._street = row[9]
                    self._brgy = row[10]
                    self._city = row[11]
                    self._bdate = row[12]

                else:
                    self = None

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                    if conn is not None:
                        conn.close()

    def _addAccount(self): #working!!
        try:
            conn = psycopg2.connect(host="localhost",database="student_db", user="postgres", password="apipahdessopolao")
            cur = conn.cursor()

            cur.execute("INSERT INTO student (idnum, name.l_name, name.f_name, name.m_name, gender, college_id, course_id, year_lvl, " +
                        "address.house_num, address.street, address.brgy, address.city, bdate) " +
                        "VALUES (" +self._idnum+ ",'"+ self._lname+ "','"+ self._fname+"','"+ self._mname+"','" +self._gender+ "',"+ str(self._college_id)+ "," +
                        str(self._course_id)+ ",'"+ self._year_lvl+ "',"+ self._house_num+",'"+ self._street+"','"+self._brgy+"','"+self._city+"','"+self._bdate+"')")
            print "HERE"
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def _deleteAccount(self): #working!!
        try:
            conn = psycopg2.connect(host="localhost",database="student_db", user="postgres", password="apipahdessopolao")
            cur = conn.cursor()
            cur.execute("DELETE FROM student where idnum="+repr(self._idnum))
            conn.commit()

        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    def _updateToDb(self): #not yet working!!
        try:
            conn = psycopg2.connect(host="localhost",database="student_db", user="postgres", password="apipahdessopolao")
            cur = conn.cursor()

            cur.execute("UPDATE student SET name.l_name = '" + self._lname + "', name.f_name = '" + self._fname +
								"', name.m_name = '" + self._mname + "', gender = '" + self._gender + "', college_id = '" + repr(self._college_id) +
								"', course_id = '" + repr(self._course_id) + "', year_lvl = '" + self._year_lvl +
								"', address.house_num = " + repr(self._house_num) + ", address.street = '" + self._street +
								"', address.brgy = '" + self._brgy + "', address.city = '" + self._city + "', bdate = '" + str(self._bdate) +
								"' WHERE idnum = " + repr(self._idnum))
            print "HERE"
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()