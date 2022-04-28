from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from krigjo25.forms import CommentForm
from krigjo25.models import DatabaseProjects, DiscordBots, MiscProjects, BlogComments, BlogPost

def WebIndex(request):

    #   Initializing the database connection
    dBotRepo = DiscordBots.objects.all().order_by('-title')
    mdb = DatabaseProjects.objects.all().order_by('-title')
    
    context = {
                'databases':mdb,
                'dBots': dBotRepo,
                
}

    return render(request, 'home/index.html', context)


def ProjectDetail(request, pk):

    project = DiscordBots.objects.get(pk=pk)
    context = {'discBot': project,}

    return render(request, 'home/projectDetail.html', context)

#   The blog page
def BlogIndex(request):

    blogPost = BlogPost.objects.all().order_by('-created')

    context = {

                'BlogPost':blogPost

    }

    return render(request, 'blog/blogIndex.html', context)

def BlogCategory(request, category):

    blogPost = BlogPost.objects.filter(categories__name__contains=category).order_by('created')
    context = {
        'BlogPost':blogPost,
        'BlogCategories':category,
    }

    return render(request, 'blog/blogCategory.html', context)

def BlogDetails(request, pk):

    form = CommentForm()

    blogPost = BlogPost.objects.filter(pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                blogpost = blogPost)
            comment.save()

    
    comments = BlogComments.objects.filter(post = blogPost)

    context = {
                'form': form,
                'BlogPost':blogPost,
                'BlogComments':comments,
                


}  
    return render(request, 'blog/blogDetails.html', context)


