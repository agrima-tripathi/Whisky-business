import cgi, cgitb
form = cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")
number = form.getvalue("number")
file1= open("contactdetails.txt","a")
file1.write(name+"\t"+email+"\t"+str(number)+"\n")
file1.close()