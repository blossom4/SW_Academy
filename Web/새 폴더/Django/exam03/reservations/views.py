from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Reservation, Comment
from .forms import ReservationForm, CommentForm 

# Create your views here.
def create(request):
    # Q2-1
    # 1. POST 방식으로 입력이 들어오지 않았으면,
    # 3. POST 방식으로 입력이 들어왔다면, 유효성 검사 후 그 입력을 저장하고 해당 상세페이지로 redirect해준다.
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)   
    # 2. 만들어놓은 form을 불러오고 보여준다.  
    else:
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)
    

def index(request):
    # Q2-2
    # 입력된 모든 정보를 역순으로 보여준다.
    reservations = Reservation.objects.all()[::-1]
    context = {
        'reservations': reservations,
    }
    
    return render(request, 'reservations/index.html', context)
    

def detail(request, pk):
    # Q2-3
    # 해당 번호에 저장된 정보를 보여주는데, 만약 해당 번호에 정보가 없다면 404오류 페이지를 출력한다.
    reservation = get_object_or_404(Reservation, pk=pk)
    # 상세페이지에서 보여줄 댓글form을 불러와 보여준다.
    comment_form = CommentForm()
    context = {
        'reservation': reservation,
        'comment_form': comment_form,
    }
    return render(request, 'reservations/detail.html', context)
    

@require_POST
def comments_create(request, pk):
    # Q3-1
    # 댓글을 달아야하는 해당 페이지의 정보를 불러온다.
    # 댓글에 POST방식으로 입력이 들어오면 유효성 검사를 진행하고 저장한다.
    reservation = Reservation.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.reservation = reservation
        comment.save()
        return redirect('reservations:detail', reservation.pk)

    