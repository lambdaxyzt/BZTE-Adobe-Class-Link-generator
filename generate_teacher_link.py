#! python
import csv,os

teacherFile = open('bzte_teacher_link.csv')
csvReaderTeacher = csv.reader(teacherFile)
teacher_table_header = ""
teacher_table_body   = ""
teacher_table_footer = ""
for row in csvReaderTeacher :
    if csvReaderTeacher.line_num == 1 :
        header_list = row
        break

teacher_table_header = f"""
        <tr>
            <th lang="fa-IR">{header_list[0]}</th>
            <th lang="fa-IR">{header_list[1]}</th>

        </tr>\n
    """


for row in csvReaderTeacher :
    teacher_table_body += f"""
        <tr>
            <td lang="fa-IR">{row[0]}</td>
            <td><a href="{row[1]}">{row[1]}</a></td>

        </tr>\n
    """
teacherFile.close()


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
    <table>
        <thead>
            {teacher_table_header}
        </thead>
        <tbody>
            {teacher_table_body}
        </tbody>
        <tfoot>
            {teacher_table_footer}
        </tfoot>
    </table>
</body>
</html>
"""

html_file = open('teacher_link.html','w')
html_file.write(html_template)
html_file.close()