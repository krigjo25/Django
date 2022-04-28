
from django.shortcuts import render
from ecrpg.models import  ManagementTeam, WikiCategory, WikiPost


def EcRPGIndex(request):
    return render(request, 'ecrpg.html')

def CommunityRules(request):
        return render(request, 'comrules.html')


def managementTeam(request):

    lvl = ManagementTeam.objects.all()
    lvl3 = lvl.filter(lvl__startswith='4')
    lvl2 = lvl.filter(lvl__startswith='3')
    helper = lvl.filter(lvl__startswith='1')

    context = {
        'lvl3':lvl3,
        'lvl2':lvl2,
        'lvl':lvl.filter(lvl__startswith='2'),
        'helper':helper,
    }

    return render(request,'managementTeam.html', context)

    # Wiki

def WikiIndex(request):

    blogPost = WikiCategory.objects.all().order_by('-name')


    context = {

                'Wiki':blogPost,

    }

    return render(request, 'wiki/wikiIndex.html', context)

def wikiPost(request, category):

    post = WikiPost.objects.filter(category__name__contains=category).order_by('-title')
    context = {

        'WikiPost':post,
        'WikiCategory':category,
    }

    return render(request, 'wiki/wikiPost.html', context)

def WikiDetails(request, pk):

    blogPost = WikiPost.objects.filter(pk=pk)
    

    context = {
                'WikiDetail':blogPost,
                


}  
    return render(request, 'wiki/wikiDetail.html', context)

