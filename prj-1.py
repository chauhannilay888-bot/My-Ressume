# Simple HTML/CSS generator + json details 
import json
a = input("What is the title of the file (with extintion): ")
b = input("Wnat should be the color of the font (body): ")
c = input("Color of background: ")
d = input("Color of heading: ")
e = input("Enter the heading: ")
bo = input("Write the body: ")
g = input("Size of body in px: ")
h = input("Size of heading in px: ")
with open(f"{a}", "w") as f:
    f.write("<html>" + "\n")
    f.write("<head>" + "\n")
    f.write(f"<title> {a} </title> \n")
    f.write("<style type='text/css'>" + "\n")
    f.write("body{background-color: " f" {c}{'}'} \n")
    f.write("body{color:" f"{b} {';font-size: '}{g}{'px'}{'}'} \n")
    f.write("h1{color: " f"{d} {';font-size: '}{h}{'px'}{'}'} \n")
    f.write("</head>" + "\n")
    f.write("</style>" + "\n")
    f.write(f"<h1> {e} </h1> \n")
    f.write("<body>" + "\n")
    f.write(f"{bo} \n")
    f.write("</body>" + "\n")
    f.write("</html>" + "\n")
    
details = {
    "File name": a,
    "body": bo,
    "body_color": b,
    "heading": e,
    "heading_color": d,
    "background_color": c,
    "body_size (px)": g,
    "heading_size (px)": h 
}
with open("Details.json", "w") as f:
    json.dump(details, f, indent=4)