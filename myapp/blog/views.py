from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post ,AboutUs ,ContactForm as ContactFormModel
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactFormModelForm
# Create your views here.   
 # Static demo data 
    #posts = [
    #       {'id':1, 'title':'Post 1','content':'content of the post 1'},
    #      {'id':2, 'title':'Post 2','content':'content of the post 2'},
    #       {'id':3, 'title':'Post 3','content':'content of the post 3'},
    #       {'id':4, 'title':'Post 4','content':'content of the post 4'},
    # 
    #  ]
def index(request):
    blog_title="Latest Posts"
    #Getting in data from post model
    all_posts = Post.objects.all()
    # Pagination
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,"blog/index.html",{'blog_title':blog_title,'page_obj':page_obj})

def detail(request, slug):
    #Getting static data below code used.
        # post = next((item for item in posts if item['id'] == int(post_id)), None)
    # logger = logging.getLogger("Testing")
    # logger.debug(f'post variable is {post}')
    try:  
        post = Post.objects.get(slug=slug)
        related_posts= Post.objects.filter(category = post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
          raise Http404("Post Doesn't exists!..")
    return render(request,"blog/detail.html",{'post':post,'related_posts':related_posts}) 

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This new redirect url page.")

def contact_view(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        logger = logging.getLogger("TESTING")
        
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Save the data to the database
            contact = ContactFormModel(name=name, email=email, message=message)
            contact.save()
            
            logger.debug(f'POST Data is {name} {email} {message}')
            
            success_message = 'Your Email has been sent!'
            return render(request, 'blog/contact.html', {'form': form, 'success_message': success_message})
        else:
            logger.debug('Form validation failure')
            return render(request, 'blog/contact.html', {'form': form})
    else:
        form = ContactFormModelForm()
    
    return render(request, 'blog/contact.html', {'form': form})

def about_view(request):
    about_content= AboutUs.objects.first().content
    return render(request,'blog/about.html',{'about_content':about_content})