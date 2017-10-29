__author__ = 'HARRIE'

from flask import Flask, render_template, request
from StudentInfo import Student
import psycopg2

app = Flask(__name__)
conn  = psycopg2.connect(host="localhost",database="student_db", user="postgres", password="apipahdessopolao")

cur = conn.cursor()
cur.execute("SELECT idnum, (name).l_name AS l_name, (name).f_name AS f_name, (name).m_name AS m_name, " +
                        "gender, college_id, course_id, year_lvl, (address).house_num AS h_num, (address).street AS street, (address).brgy AS brgy, " +
                        "(address).city AS city, bdate FROM student")
rows = cur.fetchall()
student_list = list()
for student in rows:
    info = Student(student)
    student_list.append(info)


courseList = {}
collegeList = {}
temp_student = Student()

temp_cur = conn.cursor()
temp_cur.execute("SELECT idnum, name from college")
college_row = temp_cur.fetchall()
for r in college_row:
    collegeList[r[0]] = (r[1],r[0])

temp_cur = conn.cursor()
temp_cur.execute("SELECT idnum, name, college_id from course")
course_row = temp_cur.fetchall()
for r in course_row:
    courseList[r[0]] = (r[1],r[2],r[0])


def _checkIfExists(idnum):
    cur = conn.cursor()
    cur.execute("SELECT idnum FROM student")
    row = cur.fetchall()
    id_row = list()
    for r in row:
        id_row.append(r[0])
    return int(idnum) in id_row

@app.route("/", methods=['GET', 'POST'])
def index(): #working!!
    return render_template("home.html", student_list = student_list, course = courseList, college = collegeList)

@app.route("/profile/<idnum>")
def profile(idnum):
    if _checkIfExists(idnum):
        student = Student(None, idnum)
        return render_template("profile.html", student = student,  course = courseList, college = collegeList)
    else:
        return "Account does not exist!!"

@app.route("/add") #edit here
def add():
    return render_template("writeinfo.html", college = collegeList, course = courseList)

@app.route("/profile/<idnum>/update")
def update(idnum):
    student = Student(None, idnum)
    return render_template("updateinfo.html", student = student, college = collegeList, course = courseList)

@app.route("/profile/<idnum>/delete")
def delete(idnum):
    student = Student(None, idnum)
    return render_template("deleteinfo.html", student = student)

@app.route("/search_results", methods=['GET', 'POST'])
def search():
    added_stmt = str
    if str(request.form['input_type']) == "ID":
        added_stmt = "idnum = " + str(request.form['search_input'])
    else:
        print "Here"
        added_stmt = "(name).l_name = '" + str(request.form['search_input']) + "'"

    cur.execute("SELECT idnum, (name).l_name AS l_name, (name).f_name AS f_name, (name).m_name AS m_name, " +
                        "gender, college_id, course_id, year_lvl, (address).house_num AS h_num, (address).street AS street, (address).brgy AS brgy, " +
                        "(address).city AS city, bdate FROM student where " + added_stmt)
    t_rows = cur.fetchall()
    t_student_list = list()
    for student in t_rows:
        info = Student(student)
        t_student_list.append(info)
    if len(t_student_list) != 0:
        return render_template("search_results.html", student_list = t_student_list, isEmpty = True, search_key = request.form['search_input'])
    else:
        return render_template("search_results.html", student_list = t_student_list, isEmpty = False, search_key = request.form['search_input'])

@app.route("/add/confirm", methods=['POST'])
def add_confirm():
    query_type = "A"
    temp_row = []
    temp_row.append(str(request.form['input_id']))
    temp_row.append(str(request.form['input_lname']))
    temp_row.append(str(request.form['input_fname']))
    temp_row.append(str(request.form['input_mname']))
    temp_row.append(str(request.form['input_gender']))
    temp_course = int(str(request.form['input_course']))
    temp_college = courseList[temp_course][1]
    temp_row.append(temp_college)
    temp_row.append(temp_course)
    temp_row.append(str(request.form['input_year_lvl']))
    temp_row.append(str(request.form['input_house_num']))
    temp_row.append(str(request.form['input_street']))
    temp_row.append(str(request.form['input_brgy']))
    temp_row.append(str(request.form['input_city']))
    temp_row.append(str(request.form['input_bdate']))
    temp_student = Student(temp_row)
    temp_student._addAccount()
    student_list.append(temp_student)
    return render_template("confirm.html", student = temp_student, college = collegeList, course = courseList, query_type = query_type)

@app.route("/profile/<idnum>/update/confirm", methods=['POST'])
def update_confirm(idnum):
    temp_student = None
    query_type = "U"

    for stud in student_list:
        if stud._idnum == int(str(idnum)):
            temp_student = stud
            break

    temp_student._lname = str(request.form['input_lname'])
    temp_student._fname = str(request.form['input_fname'])
    temp_student._mname = str(request.form['input_mname'])
    temp_student._gender = str(request.form['input_gender'])
    temp_course = int(str(request.form['input_course']))
    temp_college = courseList[temp_course][1]
    temp_student._college_id = (temp_college)
    temp_student._course_id = (temp_course)
    temp_student._year_lvl = str(request.form['input_year_lvl'])
    temp_student._house_num = str(request.form['input_house_num'])
    temp_student._street = str(request.form['input_street'])
    temp_student._brgy = str(request.form['input_brgy'])
    temp_student._city = str(request.form['input_city'])
    temp_student._bdate = str(request.form['input_bdate'])
    temp_student._updateToDb()
    return render_template("confirm.html", student = temp_student, college = collegeList, course = courseList, query_type = query_type)

@app.route("/profile/<idnum>/delete/confirm")
def delete_confirm(idnum):
    temp_student = None
    query_type = "D"
    for stud in student_list:
        if stud._idnum == int(str(idnum)):
            temp_student = stud
            break

    temp_student._deleteAccount()
    student_list.remove(temp_student)
    return render_template("confirm.html", student = temp_student, college = collegeList, course = courseList, query_type = query_type)

@app.route("/course")
def course():
    return render_template("course.html", college = collegeList, course = courseList)

if __name__ == "__main__":
    app.run()
    conn.close()


