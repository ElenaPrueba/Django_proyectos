from django.shortcuts import render, Http404
from django.utils import timezone
from django.forms import formset_factory, modelformset_factory
# Create your views here.
from .models import Post
from .forms import TestForm, PostModelForm

def formset_view(request):
    if request.user.is_authenticated:
        PostModelFormset= modelformset_factory(Post,form=PostModelForm)#fields=['user','title','slug'])#, extra=3)# parametro extra: añade 'extra' formularios en blanco
                                                                                            #PostModelFormset nos muestra todos los posts
        #formset = PostModelFormset(request.POST or None, queryset=Post.objects.filter(user__username="abc"))  :No sale ningun post xq no hay ningún usuario "abc"
        formset = PostModelFormset(request.POST or None, queryset=Post.objects.filter(user=request.user)) #Para hacer esto necesitaremos que e usuario este autenticado
        if formset.is_valid():
            #formset.save(commit=False)
            for form in formset:
                print(form.cleaned_data)
                obj= form.save(commit=False)
                if form.cleaned_data:
                    if not form.cleaned_data.get("publish"):
                            obj.publish = timezone.now()
                    obj.title="Titulo cambiado %s"%(obj.id)
                    obj.save()
                    #print(form.cleaned_data)
                #return redirect("/")
        context={
                "formset": formset
        }
        return render(request,"formset_view.html",context)
    else:
        raise Http404


# def formset_view(request):
#     TestFormset= formset_factory(TestForm, extra=3)# parametro extra: para repetir los formularios
#     formset = TestFormset(request.POST or None)
#     if formset.is_valid():
#         for form in formset:
#             print(form.cleaned_data)
#     context={
#             "formset": formset
#     }
#     return render(request,"formset_view.html",context)

def home(request):
    form= PostModelForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False)
        obj.title="Some random title"
        obj.publish= timezone.now()
        obj.save()#= obj.save(commit=True)
    if form.has_error:
        print(form.errors.as_json())
        print(form.errors.as_text())

        # data= form.errors.iteritems()
        # for key,value in data:
        #     print(key, value)
        #print(dir(form.errors))
        #print(dir(form))
        #print(dir(form.non_field_errors))
    ## initial_dict={
    ##     #"some_text": "Text",
    ##     "boolean": True,
    ##
    ## }
    ## form = TestForm(request.POST or None, initial=initial_dict)
    ## if form.is_valid():
    ##     print(form.cleaned_data.get("some_text"))
    ### if request.method=='POST':
    ###     print(request.POST)
    ###     print(request.POST.get("nombre"))
    ### elif request.method=='GET':
    ###     print(request.GET)

    # if request.method=='POST':
    #     form=TestForm(data=request.POST)
    #     if form.is_valid():
    #         print(form.cleaned_data)
    #     # print(request.POST)
    #     # print(request.POST.get("username"))
    # elif request.method=='GET':
    #     form=TestForm(user=request.user)
    #     print(request.GET)

    return render(request, "forms.html", {"form": form})

def error404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    #return render(request,'aplicacion/handler404.html', data)
    return render(request,'form_app/error404.html', data)
