import os

def get_template_path(path):
	#getcwd - currant working diretry
	file_path = os.path.join(os.getcwd(), path)
	if not os.path.isfile(file_path):
		raise Exception(" error not valid template path: %s"%(file_path))
	return file_path

def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()

def render_context(template_string, context):
	return template_string.format(**context)
file_ = 'templates/message_text.txt';
file_html = 'templates/message_text.html';
template = get_template(file_)
template_html = get_template(file_html)
context = {
	"name": "Justin",
	"date": "Justin",
	"total": "Justin",
}

print(render_context(template, context))
print(render_context(template_html context))
#temlate_text = get_template(file_).format(name='Justin', date="0-0-0", total="5")	


