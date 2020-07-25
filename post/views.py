from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import  HomeForm
from . models import Post, Like

# Create your views here.

def upload_post(request):
    if request.method == 'POST':
        form = HomeForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            text = form.cleaned_data['caption']
            form = HomeForm()
            return redirect('feed')
        
        args = {'form': form}
        return render(request, 'photo_upload.html', args)
    
    else:
        form = HomeForm
        return render(request, 'photo_upload.html', {'form':form})

    
def like(request):
    post = Post.objects.get(id=request.POST['post'])
    new_like = Like(user=request.user, post=post)
    new_like.save()
    return JsonResponse({'success': 1})