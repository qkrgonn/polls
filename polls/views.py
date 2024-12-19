from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse

# View to display the list of latest questions
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# View to show details of a specific question
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

# View to display the results of a specific question
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

# View to handle voting on a specific question
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Get the selected choice
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # If no choice was selected, redisplay the question voting form with an error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Increment the vote count and save the choice
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to the results page
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # Return the last five published questions
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'