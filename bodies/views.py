from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from account.models import Consultant, University
from .forms import ConsultantCommentForm, UniCommentForm, CommentForm, ContactForm
from django.views.generic import ListView, DetailView, FormView
from .models import AllComment


class ConsultantList(ListView):
    queryset = Consultant.objects.all()
    context_object_name = 'consultant_object'
    template_name = 'bodies/consultant_view.html'
    paginate_by = 5


def consultant_detail(request, **kwargs):
    consultant = get_object_or_404(Consultant, **kwargs)
    # List of active comments for this post
    comments = consultant.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = ConsultantCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
    # Assign the current post to the comment
            new_comment.consultant = consultant
    # Save the comment to the database
            new_comment.save()
    else:
        comment_form = ConsultantCommentForm
    return render(request,
                  'bodies/consultant_detail.html',
                  {'consultant': consultant, 'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


class UniversityList(ListView):
    queryset = University.objects.all()
    context_object_name = 'universities'
    # for list view we can have template by this format:
    # model's name_list and
    # we should put in directory same as name of our model in templates
    # template_name = 'bodies/university_list.html'
    paginate_by = 5


class UniversityDetail(DetailView):
    model = University
    context_object_name = 'universities'
    template_name = 'bodies/university_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UniversityDetail, self).get_context_data(**kwargs)
        return context


class ContactView(FormView):
    template_name = 'bodies/contact.html'
    form_class = ContactForm
    success_url = '/bodies/success'

    def form_valid(self, form):
        message = "{phone} / {email} said: ".format(
            phone=form.cleaned_data.get('phone'),
            email=form.cleaned_data.get('email'))
        message += "\n\n{0}".format(form.cleaned_data.get('message'))
        send_mail(
            subject=form.cleaned_data.get('subject').strip(),
            message=message,
            # what is this?
            from_email='contact-form@myapp.com',
            recipient_list=[settings.LIST_OF_EMAIL_RECIPIENTS],
        )
        return super(ContactView, self).form_valid(form)


def success(request):
    return HttpResponse('درخواست شما با موفقیت ارسال شد.')


def services(request):
    return render(request, 'services.html')


def our_comment(request):
    # List of active comments for this post
    comments = AllComment.objects.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = AllComment
        if comment_form.validate_unique:
            new_comment = comment_form.save()
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm
    return render(request,
                  'bodies/about.html',
                  {'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


