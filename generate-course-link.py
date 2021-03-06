import os,csv

course_file = open('courses-link.csv', encoding="utf-8-sig")
courseReader = csv.DictReader(course_file)

max_session =20;
header_row = f"""
    <tr>
        <th>جلسه</th>
        <th>تاریخ برگزاری</th>
        <th>لینک</th>
    </tr>
"""
tables = ""
counter = 0
for row in courseReader :
    counter += 1
    teacher_split = row['teacher'].split(';')
    teacher = teacher_split[0]
    link    = teacher_split[1]

    table_caption = f"<caption><span class='course-name'>{row['course']}</span> - <span>{row['group']}</span> - <a href='{link}'><span class='teacher'>{teacher}</span></a></caption>"
   
    table_body_row = "" 
   
    for i in range(1,max_session+1) :
        table_data  ="<tr>"
        table_row   = ""
        session_n   = f"session {i}"
        if row[session_n] == ".":
            continue
        if ';' in row[session_n] :
            session_n_1 = row[session_n].split(';')[0].strip()
            session_n_2 = row[session_n].split(';')[1].strip()
        else :
            session_n_1 = row[session_n]
            session_n_2 = ""
        table_data +=f"""
            <td>{session_n}</td>
            <td>{session_n_2}</td>
            <td><a href="{session_n_1}">{session_n_1}</a></td>
        """
        table_data += "</tr>"
        table_body_row += table_data


    table_header  = table_caption + "<thead>" + header_row + "</thead>" 
    tabel_body    = "<tbody>" + table_body_row + "</tbody>"
    table_footer = ""
    if row['other data'] != ".":
        dl = "<dl>"
        data = row['other data']
        data = data.split(',')
        for i in data :
            sub_data = i.split(':')
            dl += f"<dt dir='rtl' >{sub_data[0]} :</dt><dd>{sub_data[1]}</dd>"
        dl += "</dl>"
        table_footer = "<div class='tfoot'>" + dl + "</div>"

    table = f"<table id=\'{counter}\' >" + table_header + tabel_body +  "</table>" + table_footer + "<hr>"
    tables += table

html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css" type="text/css">
    <title>Teachers Link</title>
</head>
<body>
    {tables}
</body>
</html>
"""
course_file.close()

file = open("course-link.html","w",encoding="utf-8")
file.write(html_template)
file.close()
