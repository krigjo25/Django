from multiprocessing import context
from django.shortcuts import render
from krigjo25.models import DatabaseProjects, DiscordBots, MiscProjects, BlogComments, BlogPost

def webIndex(request):

    #   Initializing the database connection
    dBotRepo = DiscordBots.objects.all()
    mdb = DatabaseProjects.objects.all()
    
    context = {
                'databases':mdb,
                'dBots': dBotRepo,
                
}

    return render(request, 'index.html', context)


def ProjectDetail(request, pk):

    project = DiscordBots.objects.get(pk=pk)
    context = {'discBot': project,}

    return render(request, 'projectDetail.html', context)

#   The blog page
def BlogIndex(request):

    blogPost = BlogPost.objects.all().order_by('-created')
    context = {

                'BlogPost':blogPost

    }

    return render(request, 'blogIndex.html', context)

def BlogCategory(request, category):

    blogPost = BlogPost.objects.filter(categories__name__contains=category).order_by('- created')
    context = {
        'BlogPost':blogPost,
        'BlogCategories':category,
    }

    return render(request, 'blogCategory.html', context)

def BlogDetails(request, pk):
    blogPost = BlogPost.objects.filter(pk=pk)
    cmts = BlogComments.objects.filter(post = blogPost)
    context = {
                'BlogPost':blogPost,
                'BlogComments':cmts,


}  
    return render(request, 'blogDetails.html', context)

#   Testing
def TestBackGround(request):
    return render(request, 'backGroundTest.html')
