from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

#Clase home
#def home(request):
#	#print(request) #0
#	#print(dir(request)) #0
#	#print(request.method) #1
#	#print(request.user) #2
#	#print(request.is_ajax) #1
#	#print(request.is_ajax()) #1
#	print(request.get_full_path) #3
#	print(request.get_full_path())#3 #te dice la ruta
#	return HttpResponse(" <!DOCTYPE html><html><head><title>Page Title</title><style> h1 {        color: #00FF00;}</style>	Hola</head><body><h1>This is a Heading</h1><p>This is a paragraph.</p></body></html> ")
#	return HttpResponse("<p>Texto con response</p>")

def home(request):
	#response = HttpResponse()
	#response = HttpResponse(content_type='text/json')
	response = HttpResponse(content_type='application/json')
	response = HttpResponse(content_type='text/html')

	#response.write("<p>Texto con response 1</p>")
	#response.write("<p>Texto con response 2</p>")
	#response.write("<p>Texto con response 3</p>")
	#response.write("<p>Texto con response 4</p>")
	#response.write("<p>Not Found</p>")
	#response.status_code=404

	response.content=' <!DOCTYPE html><html><head><title>BIENVENIDO</title><style> h1 {        color: #00FF00;}</style>	Hola</head><body><h1>ESTAS DENTRO</h1>	<a href="/aplicacion/">Pagina principal</a></body></html>'
	print(response.status_code)
	response.status_code=200

	return response

def redirect_somewhere(request):
	return HttpResponseRedirect("/some/path") #http://joincfe.com
