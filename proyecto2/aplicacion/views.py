from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import PostModel
from .forms import PostModelForm
from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate, login


from django.conf import settings
from django.shortcuts import redirect
from django.shortcuts import render_to_response

#Traduccion
from django.utils.translation import ugettext as _
from django.utils import translation

# CRUD

#Create

#Retrieve

#Update

#Delete

##def post_model_list_view(request): #sin render
##    qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
##    print(qs)
##    return HttpResponse("some data")
##

##@login_required(login_url='/login/')
#@login_required()
#def post_model_list_view(request):
#    print(request.user)
#
#    qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
#    context_dictionary = {
#        "object_list": qs#,
#        #"otro_dic": {"abc":123},
#        #"num": 123
#    }
#    func=request.user.is_authenticated
#    #print(func)
#    #if func:
#    #    print("Logueado")
#    #else:
#    #    print("No logueado")
#    if func:
#        template="aplicacion/list-view.html"
#    else:
#        template = "aplicacion/list-view-public.html"
#        #raise Http404
#        #return HttpResponseRedirect("/login")
#    #print(qs)
#    #template = "aplicacion/list-view.html" #esta template es la template especifia de la funcion post_model_list_view
#    return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})

# Habrá que crear templates para toda las funciones

## Metodo que te lleva a una pagina u otra en funcion de si estas o no  regristrado
## def post_model_list_view(request):
##     #print(request.GET)
##     #busqueda=request.GET["q"]
##     qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
##     context_dictionary = {
##         "object_list": qs
##     }
##     if request.user.is_authenticated:
##         busqueda=request.GET.get("q", None)# El get del final elimina el "keyError"
##         #qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
##         if busqueda is not None:
##             qs=qs.filter(Q(title__icontains=busqueda) | Q(content__icontains=busqueda) | Q(slug__icontains=busqueda))
##
##         template="aplicacion/list-view.html"
##     else:
##         template = "aplicacion/list-view-public.html"
##     return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})

#@login_required(redirect_field_name='', login_url='/aplicacion/login')
#@login_required(redirect_field_name='')

# def post_model_list_view(request):
#     qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
#     context_dictionary = {
#         "object_list": qs
#     }
#
#     usern = request.POST.get('username')
#     passw = request.POST.get('password')
#     user = authenticate(username=usern, password=passw)
#     print(request.method)
#     if user:
#         # Is the account active? It could have been disabled.
#         if user.is_active:
#             print("Hola")
#             busqueda=request.GET.get("q", None)# El get del final elimina el "keyError"
#             if busqueda is not None:
#                 qs=qs.filter(Q(title__icontains=busqueda) | Q(content__icontains=busqueda) | Q(slug__icontains=busqueda))
#
#             template="aplicacion/list-view.html"
#             #login(request, user)
#             #return render(request,template,context_dictionary)
#             #return HttpResponseRedirect('/aplicacion')#success page
#         else:
#             template="aplicacion/login.html"
#             #return HttpResponse("aplicacion/login")#invalid login message
#         #print(request.GET)
#         #busqueda=request.GET["q"]
#         return render(request,template,context_dictionary)
#
#     template="aplicacion/login.html"
#     return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})

# def post_model_list_view(request):
#     busqueda=request.GET.get("q", None)# El get del final elimina el "keyError"
#     qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
#     if busqueda is not None:
#         qs=qs.filter(Q(title__icontains=busqueda) | Q(content__icontains=busqueda) | Q(slug__icontains=busqueda))
#     context_dictionary = {
#         "object_list": qs
#     }
#     template="aplicacion/list-view.html"
#     return render(request,template,context_dictionary)

#@login_required(login_url='aplicacion/login/')  #Pagina no encontrada:http://localhost:9090/aplicacion/aplicacion/login/?next=/aplicacion/
#@login_required(redirect_field_name='', login_url='/aplicacion/login')
#@login_required()
def post_model_list_view(request):
    if request.user.is_authenticated:
        busqueda=request.GET.get("q", None)# El get del final elimina el "keyError"
        qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
        if busqueda is not None:
            qs=qs.filter(Q(title__icontains=busqueda) | Q(content__icontains=busqueda) | Q(slug__icontains=busqueda))
        context_dictionary = {
            "object_list": qs
        }
        template="aplicacion/list-view.html"
        return render(request,template,context_dictionary)
    else:
        qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
        context_dictionary = {
            "object_list": qs
        }
        return HttpResponseRedirect("/aplicacion/login")
        #template="aplicacion/login.html"
        #return render(request,template,context_dictionary)


@login_required
def login_required_view(request):
    #print(request.user)
    qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
    context_dictionary = {
        "object_list": qs
    }

    if request.user.is_authenticated:
        template="aplicacion/list-view.html"
    else:
        template = "aplicacion/list-view-public.html"
        #raise Http404
        #return HttpResponseRedirect("/login")
    return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})

#@login_required()
def post_model_detail_view(request, id=None):
    if request.user.is_authenticated:
        idaux=id
        #try:
        #    obj=PostModel.objects.get(id=100)
        #except:
        #    raise Http404
        #qs=PostModel.objects.filter(id=100)
        #if not qs.exits() and qs.count()!=1:
        #    raise Http404
        #else:
        #    obj=qs.first()
        obj=get_object_or_404(PostModel, id=idaux)

        context_dictionary = {
            "object": obj,
        }
        template="aplicacion/detail-view.html"
        return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})
    else:
        qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
        context_dictionary = {
            "object_list": qs
        }
        return HttpResponseRedirect("/aplicacion/login")


#@login_required()
def post_model_create_view(request):
    if 'lang' in request.GET:
        translation.activate(request.GET.get('lang'))

    if request.user.is_authenticated:
    # if request.method == "POST":
    #     print(request.POST)
    #     form = PostModelForm(request.POST)
    #     if form.is_valid:
    #         form.save(commit=False)
    #         print(form.cleaned_data)

        form = PostModelForm(request.POST or None)
        context_dictionary = {
        "form": form
        }
        if form.is_valid() and form!=None:
            obj=form.save(commit=False)
            obj.save()
            messages.success(request,_("Post creado exitosamente"))
            context_dictionary = {
                "form": PostModelForm()
            }#@login_required()
            #return HttpResponseRedirect("/aplicacion/{num}".format(num=obj.id))

        template="aplicacion/create-view.html"
        return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})

    else:
        qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
        context_dictionary = {
            "object_list": qs
        }
        return HttpResponseRedirect("/aplicacion/login")

#@login_required()
def post_model_update_view(request, id=None):
    if 'lang' in request.GET:
        translation.activate(request.GET.get('lang'))

    if request.user.is_authenticated:
        obj=get_object_or_404(PostModel, id=id)
        form = PostModelForm(request.POST or None, instance=obj)
        context_dictionary = {

        "form": form
        }
        if form.is_valid() and form!=None:
            obj=form.save(commit=False)
            obj.save()
            messages.success(request,_("Post actualizado exitosamente"))
            context_dictionary = {
                "form": PostModelForm()
            }
            #return HttpResponseRedirect("/aplicacion/post_%s",obj.id)
            return HttpResponseRedirect("/aplicacion/post:{num}/".format(num=obj.id))

        template="aplicacion/update-view.html"
        return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})
    else:
        qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
        context_dictionary = {
            "object_list": qs
        }
        return HttpResponseRedirect("/aplicacion/login")

def post_model_delete_view(request, id=None):
    if 'lang' in request.GET:
        translation.activate(request.GET.get('lang'))

    if request.user.is_authenticated:
        idaux=id
        obj=get_object_or_404(PostModel, id=idaux)
        if request.method=="POST":
            obj.delete()
            messages.success(request,_("Post eliminado exitosamente"))
            return HttpResponseRedirect("/aplicacion/")

        context_dictionary = {
            "object": obj,
        }
        template="aplicacion/delete-view.html"
        return render(request,template,context_dictionary) #argumentos: request, direccion donde esta el template,diccionario({})
    else:
        qs = PostModel.objects.all()#lista que devuelve una lista conocida como un conjunto de consultas en DjangoTemplates
        context_dictionary = {
            "object_list": qs
        }
        return HttpResponseRedirect("/aplicacion/login")
# Metodo que hace lo mismo que los anteriores, pero todo en uno
# def post_model_robust_view(request, id=None):
#     obj = None
#     context_dictionary = {}
#     success_message = 'Creado nuevo Post'
#
#     if id is None:
#         template="aplicacion/create-view.html"
#     else:
#         obj=get_object_or_404(PostModel, id=idaux)
#         success_message = 'Creado nuevo Post'
#         context_dictionary["object"]= obj
#         template="aplicacion/detail-view.html"
#         if "edit" is in request.get_full_path():
#             template="aplicacion/update-view.html"
#         if "delete" is in request.get_full_path():
#             template="aplicacion/delete-view.html"
#             if request.method=="POST":
#                 obj.delete()
#                 messages.success(request, "Post eliminado")
#                 return HttpResponseRedirect("/aplicacion/")
#     #if "edit" is in request.get_full_path() or "create" is in request.get_full_path():
#     form= PostModelForm(request.POST or None, instance=obj)
#     context_dictionary["form"]=forms
#     if form.is_valid():
#         obj=form.save(commit=False)
#         obj.save()
#         messages.success(request, success_message)
#         if obj is not None:
#             return HttpResponseRedirect("/aplicacion/{num}".format(obj.id))
#         context_dictionary["form"]=PostModelForm
#
#     return render(request,template,context_dictionary)

# def user_login(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#         # Gather the username and password provided by the user.
#         # This information is obtained from the login form.
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         print("auth",str(authenticate(username=username, password=password)))
#
#         if user:
#             # Is the account active? It could have been disabled.
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect('/aplicacion')#success page
#         else:
#             return HttpResponse("aplicacion/login")#invalid login message
#     else:
#         # Bad login details were provided. So we can't log the user in.
#         print ("Invalid login details: {0}, {1}".format(username, password))
#         return HttpResponse("Invalid login details supplied.")
#
#     return render_to_response('user/profile.html', {}, context)

def user_login(request):
    form = PostModelForm(request.POST or None)
    context_dictionary = {
    "form": form
    }
    print(form)
    print("1")

    if form.is_valid() and form!=None:
        print("hola")
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print("auth",str(authenticate(username=username, password=password)))
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                template="aplicacion/list-view.html"
                #return render(request,template,context_dictionary)
                return HttpResponseRedirect('/aplicacion')#success page
            else:
                template="aplicacion/login.html"
                #return render(request,template,context_dictionary)
                return HttpResponse("aplicacion/")#invalid login message
        else:
            # Bad login details were provided. So we can't log the user in.
            print ("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    template="aplicacion/registration/login.html"
    return render(request,template,context_dictionary)
    #return render_to_response('user/profile.html', {}, context_dictionary)


def redirigir(request):
    if request.user.is_authenticated:
        raise Http404
    else:
        return HttpResponseRedirect('/aplicacion/login')


# def post_model_create_view(request):
#     form = PostModelForm(request.POST or None)
#     context_dictionary = {
#     "form": form
#     }
#     if form.is_valid() and form!=None:
#         obj=form.save(commit=False)
#         obj.save()
#         messages.success(request,"Post creado exitosamente")
#         context_dictionary = {
#             "form": PostModelForm()
#         }@login_required()
#         #return HttpResponseRedirect("/aplicacion/{num}".format(num=obj.id))
#
#     template="aplicacion/create-view.html"
#     return render(request,template,context_dictionary)

# def handler404(request, *args, **argv):
#     response = render_to_response('404.html', {},
#                                   context_instance= RequestContext(request))
#     response.status_code = 404
#     return response
#
#
# def handler500(request, *args, **argv):
#     response = render_to_response('500.html', {},
#                                   context_instance= RequestContext(request))
#     response.status_code = 500
#     return response

def handler404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    #return render(request,'aplicacion/handler404.html', data)
    return render(request,'aplicacion/handler404.html', data)


def handler500(request):
     data = {}
     return render(request,'aplicacion/handler500.html', data)
