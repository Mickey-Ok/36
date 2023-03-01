from django.db import models

# Create your models here.
class ApplicationForm(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250, help_text='eg. youremail@gmail.com')

    # class Meta:
    #     model = User
    #     fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'email')
    
    def save(self, commit=True):
        user=super(ApplicationForm, self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
        return user