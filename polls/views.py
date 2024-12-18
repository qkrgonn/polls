from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


<<<<<<< HEAD
=======


>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

<<<<<<< HEAD

=======
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

<<<<<<< HEAD

=======
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
<<<<<<< HEAD
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

class IndexView(generic.ListView):
=======
        #Redisplay the question voting form
        return render(request, 'polls/detail.html', {
        'question':question,
        'error_message': "You didn't select a choice.",
        })


    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

### Generic View (class-based views)
class IndexView (generic.ListView):
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    """Return the last five published questions."""
    def get_queryset(self):
<<<<<<< HEAD
        return Question.objects.order_by('-pub_date')[:5]

    class DetailView(generic.DetailView):
        model = Question
        template_name = 'polls/detail.html'

    class ResultsView(generic.DetailView):
        model = Question
        template_name = 'polls/results.html'
=======
     return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
