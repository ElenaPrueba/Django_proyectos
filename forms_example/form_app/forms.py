from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):
    year_field=forms.DateField(initial="2019-01-01",widget=forms.SelectDateWidget)
    # title=forms.CharField(max_length=120,
    #                     label="Some field",
    #                     help_text="some help text",
    #                     error_messages={"required": "The title is required."})
    # #Es mejor no hacerlo así porque ya has definido previamente el titulo en los modelos

    class Meta:
        model = Post
        fields = ['user','title','slug']
        labels={"title": "This is title",
                "slug": "This is slug"}
        help_text={"title": "This is title help",
                "slug": "This is slug help"}
        # error_messages={"title": { "max_length": "This title is too long",
        #                             "required": "The title field is required"},
        #         "slug": {"max_length": "This slug is too long",
        #                 "required": "The slug fiel8d is required",
        #                 "unique": "The slug must be unique"}}

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget = forms.Textarea()
        self.fields["title"].error_messages={ "max_length": "This title is too long",
                                            "required": "The title field is required"}

        self.fields["slug"].error_messages={"max_length": "This slug is too long",
                                            "required": "The slug field is required",
                                            "unique": "The slug must be unique"}

        for field in self.fields.values():
            field.error_messages ={
                                "required": "You know, {fieldname} is required".format(fieldname=field.label),
            }

    # def clean_title(self, *args, **kwargs):
    #     #instance = self.instance
    #     title = self.cleaned_data.get('title')
    #     # qs = Post.objects.filter(title__iexact=title)
    #     # if instance is not None:
    #     #     qs = qs.exclude(pk=instance.pk) # id=instance.id
    #     # if qs.exists():
    #     #     raise forms.ValidationError("This title has already been used. Please try again.")
    #     #raise forms.ValidationError("Error")
    #     return title

    # def save(self, commit=True, *args, **kwargs):
    #     obj=super(PostModelForm, self).save(commit=True, *args, **kwargs)
    #     obj.publish="2018-12-01"
    #     if commit:
    #         obj.save()
    #     return obj




SOME_CHOICES=[
    ('db-value','Display-value'),
    ('db-value2','Display-value2'),
    ('db-value3','Display-value3'),
]
INTS = [tuple([x,x]) for x in range(0,100)]

class TestForm(forms.Form):
    year_field=forms.DateField(widget=forms.SelectDateWidget)
    some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows": 4, "cols":10}))
    choices = forms.CharField(label='Text', widget=forms.Select(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=10, widget=forms.Select(choices=INTS))
    email = forms.EmailField(min_length=3)

    def __init__(self, user=None, *args,**kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        if user:
            self.fields["some_text"].initial=user.username

    def clean_integer(self, *args,**kwargs):
        integer=self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer most be grater than 10")
        return integer

    def clean_some_text(self, *args,**kwargs):
        some_text=self.cleaned_data.get("some_text")
        if len(some_text) < 3:
            raise forms.ValidationError("Ensure the text is greater than 3 characters")
        return some_text
