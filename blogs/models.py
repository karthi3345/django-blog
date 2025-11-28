from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models eduthu database la table create pannanum
#each model represents a table in the database
#Each attribute of the model represents a field in the table
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True) #name field create pannanum max length 100 characters unique ethuku na oru category name repeat aagathenga models.PhoneNumberField(_(""))
    created_at = models.DateTimeField(auto_now_add=True) #created at field create pannanum auto_now_add true na object create pannumbothu athu automatic aagum
    #auto now na object update pannumbothu athu automatic aagum
    updated_at = models.DateTimeField(auto_now=True) #updated at field create pannanum auto_now true na object update pannumbothu athu automatic aagu
    
    
    
    
    class Meta:
        
        verbose_name_plural = 'Categories' #admin panel la model plural name enna nu sollanum
        
    def __str__(self): #self eduthu model object represent pannanum na ethana field use pannanum nu sollanum
        #ithula object na etha field use panni represent pannanum nu sollanum
        return self.category_name #admin panel la category object name display aagum
    
    
STATUS_CHOICES = (
    ('Draft', 'Draft'),
    ('Published', 'Published'),
) #status choices create pannanum blog publish pannumnu na 1 illana draft aagumnu 0 sollanum
#choices use panni field la ethana values irukkumnu sollanlam
    
class Blog(models.Model):
    title = models.CharField(max_length=200) #title field create pannanum max length 200 characters
    slug = models.SlugField(max_length=150,unique=True, blank=True) #slug oru part of url la use pannuvanga athu unique aagum    
    #slug very useful for SEO(Search Engine Optimization) nu sollum
    #slug useful for creating readable and SEO-friendly URLs for blog posts
    #unique true na slug repeat aagathenga
    #blank true na slug blank aagalam
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #ForeignKey use panni Category model ku relation create pannudhu
    #on_delete=models.CASCADE na category delete pannumbothu athoda related blogs um delete aagum
    #foreign key na oru model la irukura field vera oru model la irukura primary key ku refer pannuumnu sollum
    author = models.ForeignKey(User, on_delete=models.CASCADE) #user deleted pannumbothu athoda related blogs um delete aagum
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True) #featured image field create pannanum
    #upload_to na image evlo folder la save aagumnu sollanum
    #null true na database la null aagalam
    #blank true na form la blank aagalam
    short_description = models.TextField(max_length=500) #short description field create pannanum max length 500 characters
    blog_body = models.TextField(max_length=500) #blog body field create pannanum
    status=models.CharField( max_length=20,choices=STATUS_CHOICES, default='Draft') #status field create pannanum choices use panni STATUS_CHOICES la irukura values la eduthukalam default 0 na draft aagumnu sollanum
    is_featured = models.BooleanField(default=False) #is featured field create pannanum default false na featured aagathenga
    created_at = models.DateTimeField(auto_now_add=True) #created at field create pannanum auto_now_add true na object create pannumbothu athu automatic aagum
    updated_at = models.DateTimeField(auto_now=True) #updated at field create pannanum auto_now true na object update pannumbothu athu automatic aagum
    
    
    def __str__(self):
        return self.title #admin panel la blog object name display aagum