import os #allows interops with windows,linux

def get_template_path(path):
	file_path = os.path.join(os.getcwd())#makes the path system agnostic
	if not os.path.isfile(file_path):
		raise Exception("This is not a valid path %s"%(file_path))#if the path or file doesnt exist this exception will tell ya which file_path was searched
	return file_path


def get_template(path):
	file_path = get_template_path(path)
	return open(file_path).read()#open(pathToFile).read() will actually read the file 


def render_context(template_string,context):
	return template_string.format(**context)# the **is saying based the format off of the string in the context


file_ = "template/email_message.html"# the path for the plain text is just the .txt file
template = get_template(file_)
print(get_tempate(file_)) #to ensure the content of the .txt file is actually being read

#example
#file_ = 'this/is/a/file.txt' <<---this is what woult be returned

#get_template_path(file_)