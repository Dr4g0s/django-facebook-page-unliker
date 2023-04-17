from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
import facebook


def liked_pages(request):
    user = request.user
    try:
        social_account = SocialAccount.objects.get(user=user, provider='facebook')
        access_token = social_account.socialtoken_set.get(account=social_account).token
        graph = facebook.GraphAPI(access_token)
        pages = graph.get_object('/me/likes')['data']
        return render(request, 'liked_pages.html', {'pages': pages})
    except:
        return render(request, 'liked_pages.html', {'pages': []})


def unlike_pages(request):
    user = request.user
    pages = request.POST.getlist('pages')
    try:
        social_account = SocialAccount.objects.get(user=user, provider='facebook')
        access_token = social_account.socialtoken_set.get(account=social_account).token
        graph = facebook.GraphAPI(access_token)
        for page in pages:
            graph.delete_object('/' + page + '/likes')
        return redirect('liked_pages')
    except Exception as e:
        print("##########", e)
        return redirect('liked_pages')
