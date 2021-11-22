#!/usr/bin/env python

import os
import http.server
import socketserver

_TEMPLATE = """<!DOCTYPE html> 
<!--
 _______  ______   _____  _____  
|_   __ \\|_   _ `.|_   _||_   _| 
  | |__) | | | `. \\ | |    | |   
  |  ___/  | |  | | | '    ' |   
 _| |_    _| |_.' /  \\ \\__/ /    
|_____|  |______.'    `.__.'     
                                 
-->
<html>

    <head>
        <meta charset='utf-8'>

        <title>{}</title>

        <script src="../../lib/p5.min.js"></script>
        <script src="../../lib/p5.dom.min.js"></script>
        <script src="../../sketches/{}"></script>

        <meta name='viewport' content='width=device-width, initial-scale=1'>

    </head>
</html>

"""
_STUDENTS = ["ridge", "sam", "zadek"]
PORT = 8000

def generate_static_files(student):
	for sketch_filename in os.listdir("./sketches/" + student):
		title = sketch_filename.split(".")[0].replace("-", " ")
		sketch_path = "{}/{}".format(student, sketch_filename)
		html_filename = sketch_filename.split(".")[0].replace("-", "_") + ".html"
		with open("gallery/{}/{}".format(student, html_filename), "w") as file:
			file.write(_TEMPLATE.format(title, sketch_path))

def serve_files():
	handler = http.server.SimpleHTTPRequestHandler
	httpd = socketserver.TCPServer(("", PORT), handler)
	print("Server started at localhost:" + str(PORT))
	print("Check out http://localhost:8000/gallery to see your work!\n"
		"And hit control+c to shut down this server.")
	httpd.serve_forever()


if __name__ == '__main__':
	for student in _STUDENTS:
		generate_static_files(student)
	serve_files()
