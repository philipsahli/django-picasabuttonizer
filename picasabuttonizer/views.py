# Create your views here.
import django
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.db.models.fields.files import FileField
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from buttonizer import Buttonizer
from picasabuttonizer.forms import HybridButtonForm, TrayexecButtonForm, OpenButtonForm
from picasabuttonizer.models import Button, HybridButton, TrayexecButton, OpenButton

def _model_form_type(type, model=None, form=None):
    if type == "hybrid":
        form = HybridButtonForm
        model = HybridButton
    if type == "exec":
        form = TrayexecButtonForm
        model = TrayexecButton
    if type == "open":
        form = OpenButtonForm
        model = OpenButton
    return form, model


def new_button(request, type):
    return {'form': _model_form_type(type)[0], 'type': type}


def index_handle(request, guid=None, type=None):
    print request.GET.items()

    form, model = _model_form_type(type)
    print form, model

    if request.method == 'POST':
        print "POST"
        try:
            instance = Button.objects.get(guid=guid)
            form = form(request.POST, request.FILES, instance=instance)
        except model.DoesNotExist:
            form = form(request.POST, request.FILES)
        if form.is_valid():
            button = form.save(commit=False)
            if not isinstance(request.user, AnonymousUser):
                # save button to db
                button.user = request.user
                button.save()
            else:
                button.save()
                session_buttons = request.session.get('buttons', [])
                session_buttons.append(button.guid)
                request.session['buttons'] = session_buttons
            messages.info(request, "Saved")
            print button
            return HttpResponseRedirect("/buttonizer/")
        else:
            print form.errors
    else:
        if type:
            if not guid:
                form = form()
            else:
                form = form(instance=Button.objects.get(guid=guid))
        else:
            # entry point
            return
    if request.user.is_authenticated():
        buttons = model.objects.filter(user=request.user.id)
    else:
        buttons = []
        for guid in request.session.get('buttons', []):
            try:
                buttons.append(model.objects.get(guid=guid))
            except model.DoesNotExist, e:
                pass

    return {'form': form, 'buttons': buttons}

def index(request, guid=None):
    vars = index_handle(request, guid)
    return render_to_response('pages/buttonizer.html', vars, RequestContext(request))


def remove_button(request, guid):
    button = Button.objects.get(guid=guid)
    button.delete()
    messages.info(request, "Deleted")
    if not request.user.is_authenticated():
        session_buttons = request.session.get('buttons')
        session_buttons.remove(guid)
    return index(request)


def _button_in_session(button_list, guid):
    return False

def _can_access(request, button, guid):
    if button.user:
        if button.user.id!=request.user.id:
            raise Button.DoesNotExist
    else:
        if _button_in_session(request.session.get('buttons', []), guid):
            raise Button.DoesNotExist

def get_button(request, guid):
    buttonizer = Buttonizer()
    try:
        button = Button.objects.get(guid=guid)
        _can_access(request, button, guid)
    except Button.DoesNotExist:
        raise Http404
    (name, button_file) = buttonizer.create_for_buttonmodel(button)
    response = HttpResponse(mimetype="appplication/zip")
    response['Content-Disposition'] = "attachment; filename="+name
    response.write(button_file.getvalue())
    button_file.close()
    return response

