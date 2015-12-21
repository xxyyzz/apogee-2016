# from django.contrib.admin.widgets import FilteredSelectMultiple
# from django import forms
# from django.contrib.auth.models import User
# from events.models import Event,Tabs
# # from registration.models import Asme
# from tinymce.widgets import TinyMCE
# #from pagedown.widgets import AdminPagedownWidget
# #from apogee.wmd.widgets import AdminMarkDownInput

# class EventForm(forms.ModelForm):
#    # overview = forms.CharField(widget=AdminMarkDownInput())
#    # contact = forms.CharField(widget=AdminMarkDownInput())
#     class Meta:
#         model = Event
#         widgets = {
#                 'overview' : TinyMCE(attrs={'cols': 120, 'rows': 20 }),
#                 'contact' : TinyMCE(attrs={'cols': 30, 'rows': 10}) ,
#                 }
#         exclude = ('author','register',)

# class EventAdminForm(forms.ModelForm):
#     #overview = forms.CharField(widget=AdminMarkDownInput())
#     #contact = forms.CharField(widget=AdminMarkDownInput())
#     class Meta:
#         model = Event
#         widgets = {
#                 'overview' : TinyMCE(attrs={'cols': 120, 'rows': 20 }),
#                 'contact' : TinyMCE(attrs={'cols': 30, 'rows': 10}) ,
#                 'tag':forms.CheckboxSelectMultiple,
#                 }


        
# class TabsAdminForm(forms.ModelForm):
#     #content =forms.CharField()
#     class Meta:
#         model = Tabs
#         widgets = {
#                 'content' : TinyMCE(attrs={'cols': 120, 'rows': 20}),
#         }
# c = (
# ('Joomla' ,'Joomla'),
# ('Animation','Animation'),
# ('Hacking','Hacking'),
# )
# class WorkshopForm(forms.Form):
#     name = forms.CharField(max_length = 100)
#     college = forms.CharField(max_length = 100)
#     city = forms.CharField(max_length = 50)
#     workshop_details = forms.CharField(widget=forms.Select(choices = c))
#     contact_no = forms.CharField(max_length = 100)
#     e_mail = forms.EmailField()


# #class AsmeForm(forms.ModelForm):
#  #   class Meta:
#   #      model = Asme
#    # events=forms.ModelMultipleChoiceField(queryset=Event.objects.filter(category__name="ASME SPDC"))


#    # username = forms.CharField(max_length = 30 , help_text = ' ')
#     #password = forms.CharField(max_length = 30, widget = forms.PasswordInput())
#     #re_type_password = forms.CharField(max_length = 30,widget = forms.PasswordInput())
#    # first_name = forms.CharField(max_length = 100)
#    # middle_name = forms.CharField(max_length = 100,required=False)
#    # last_name = forms.CharField(max_length = 100)
#    # e_mail = forms.EmailField()
#    # gender = forms.CharField( widget = forms.RadioSelect(choices = ( ('Male'  , 'Male') ,('Female' , 'Female'),)))
#    # college =forms.CharField(max_length=100,label = 'College')
#    # contact_no = forms.IntegerField()
#    # year = forms.ChoiceField(choices = (('1', 'First Year'), ('2', 'Second Year'),('3', 'Third Year'),('4', 'Fourth Year'), ('5', 'Fifth Year'), ('6', 'Post Graduate')
#    # member=forms.CharField( widget = forms.RadioSelect(choices = ( ('Yes'  , 'Yes') ,('No' , 'No'),)))
#    # member_id=forms.CharField(max_length = 100,required=False)
#    # expiry=forms.CharField(max_length = 100,required=False)
#    # college_id=forms.CharField(max_length = 100)
#    # events=forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Others")
#    # other= forms.CharField(max_length = 100)

    

