import yate as y
# print(y.start_response())
#Content-type: text/html
# print(y.start_response("text/plain"))
#Content-type: text/plain
# print(y.start_response("application/json"))
#Content-type: application/json
# print(y.include_header("Welcome to my home on the web!"))
#<title>Welcome to my home on the web!</title>
# print(y.include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'})) 
#<a href="/index.html">Home</a>&nbsp;&nbsp;&nbsp;&nbsp;<a href="/cgi-bin/select.py"
#>Select</a>&nbsp;&nbsp;&nbsp;&nbsp;
# print(y.start_form("/cgi-bin/process-athlete.py"))
#<form action="/cgi-bin/process-athlete.py" method"POST">
# print(y.end_form("Click to Confirm Your Order"))
#<p></p><input type=submit value="Click to Confirm Your Order"></form>
# for fab in ['John', 'Paul', 'George', 'Ringo']:
#    print(y.radio_button(fab, fab)) 
# <input type="radio" name="John" value="John">John<br />
# <input type="radio" name="Paul" value="Paul">Paul<br />
# <input type="radio" name="George" value="George">George<br />
# <input type="radio" name="Ringo" value="Ringo">Ringo<br />
# print(y.u_list(['Life of Brian', 'Holy Grail']))
#<ul><li>Life of Brian</li><li>Holy Grail</li></ul>
# print(y.header("Welcome to my home on the web"))
# <h2>Welcome to my home on the web</h2>
# print(y.para("Was it worth the wait? We hope it was..."))
# <p>Was it worth the wait? We hope it was...</p>
