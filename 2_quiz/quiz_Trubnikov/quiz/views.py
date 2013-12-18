# ~*~ coding: utf-8 ~*~
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from quiz.models import Question, Answer
from datetime import datetime


def index(request):
    context = {'ts': datetime.now(), }
    return render(request, 'index.html', context)


def quiz(request, que_id):
    que = get_object_or_404(Question, pk=que_id)
    if request.method == 'POST':
        try:
            selected_ans = que.answer_set.get(pk=request.POST['choice'])
        except (KeyError, Answer.DoesNotExist):
            return render(request, 'quiz.html', {'que': que, 'err': 1})
        else:
            selected_ans.freq += 1
            selected_ans.save()
            return HttpResponseRedirect(reverse(
                'quiz.views.stats', args=(que.id,)))
    else:
        return render(request, 'quiz.html', {'que': que, 'err': 0})


def stats(request, que_id):
    context = {'que': get_object_or_404(Question, pk=que_id)}
    return render(request, 'stats.html', context)
