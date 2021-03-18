# django_05_workshop

> **django model form**



```python
# models.py
class Reservation(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
```



1. 모델 폼을 정의하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
from django import forms
from .models import Reservation

class REservationFrom(__(a)__):
    class(__(b)__):
        model = Reservation
        filed = '__all__'
```

```python
(a): forms.ModelForm
(b): Meta
```



2. 글 작성 기능을 구현하기 위해 다음과 같이 코드를 작성하였다. 서버를 실행시킨 후 기능을 테스트 해보니 특정 상황에서 문제가 발생하였다. 이유와 해결방법을 작성하시오.

```python
def create(request):
    if request.moethod == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
        else:
            form = ReservationForm()
            context = {
                'form': form,
            }
        return render(requeste, 'reservation/create.html', context)
```

```python
인스턴스를 생성해주어야 하므로, form = ReservationsForm(instance=reservation)으로 해주어야한다.
```



3. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 코드를 작성하시오.

```python
def update(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST'
        __(a)__
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
        else:
            __(b)__
        context = {
            'reservation': reservation,
            'form': form,
        }
    return render(request, 'reservations/update.html', context)
```

```python
(a): form = ReservationForm(request.POST)
(b): form = ReservationForm(instance=reservation)
```



4. 글 수정 기능을 구현하기 위해 빈칸에 들어갈 수 있는 코드를 모두 작성하시오.

```html
<h2>edit</h2>
<form action="{% url 'reservations:update' reservation.pk %}" method="POST">
  {% csrf_token %}
  {{ form.__(a)__ }}
    <input type="submit" value="submit">
</form>
```

```python
(a): as_table
```

