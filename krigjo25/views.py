from multiprocessing import context
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from krigjo25.forms import CommentForm
from krigjo25.models import DatabaseProjects, DiscordBots, MiscProjects, BlogComments, BlogPost, BlogCategory

def WebIndex(request):

    #   Initializing the database connection
    dBotRepo = DiscordBots.objects.all().order_by('id')
    mdb = DatabaseProjects.objects.all().order_by('id')
    
    context = {
                'databases':mdb,
                'dBots': dBotRepo,
                
}

    return render(request, 'home/index.html', context)


def ProjectDetail(request, pk):

    project = DiscordBots.objects.get(pk=pk)
    context = {'discBot': project}

    return render(request, 'home/projectDetail.html', context)

#   The blog page
def BlogIndex(request):

    blogCategory = BlogCategory.objects.all()

    context = {

                'Tag':blogCategory,

    }

    return render(request, 'blog/blogIndex.html', context)

def blogPost(request, category):


    
    post = BlogPost.objects.filter(category__name__contains=category). order_by('-created')

    bots = DiscordBots.objects.all()


    context = {

                
                'tag':category,
                'blogPost':post,
                'DBots':bots.filter(title__contains=f'{BlogPost.title}'),

    }
    print(bots)
    return render(request, 'blog/blogDetail.html', context)

def BlogDetails(request, pk):

    post = BlogPost.objects.filter(pk=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                blogpost = post)
            comment.save()

    
    comments = BlogComments.objects.filter(post = post)

    context = {
                'form': form,
                'BlogPost':post,
                'BlogComments':comments,
                


}  
    return render(request, 'blog/blogDetails.html', context)


