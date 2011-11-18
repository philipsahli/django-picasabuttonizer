# Create your views here.
import StringIO
import django
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from django.db.models.fields.files import FileField
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from buttonizer import Buttonizer
from models import Button
from forms import ButtonForm

def index_handle(request, guid=None):
    edit_url = ""
    if "edit" in request.GET:
        guid=request.GET.__getitem__('edit')
    if request.method == 'POST':
        try:
            instance = Button.objects.get(guid=guid)
            form = ButtonForm(request.POST, request.FILES, instance=instance)
        except Button.DoesNotExist:
            form = ButtonForm(request.POST, request.FILES)
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
            return HttpResponseRedirect("/buttonizer/")
    else:
        if not guid:
            form = ButtonForm()
        else:
            form = ButtonForm(instance=Button.objects.get(guid=guid))
            edit_url = guid
    if request.user.is_authenticated():
        buttons = Button.objects.filter(user=request.user.id)
    else:
        buttons = []
        for guid in request.session.get('buttons', []):
            try:
                buttons.append(Button.objects.get(guid=guid))
            except Button.DoesNotExist, e:
                pass

    #return {'form': form, 'buttons': buttons, 'edit_url': edit_url}, RequestContext(request)
    return {'form': form, 'buttons': buttons, 'edit_url': edit_url}

def index(request, guid=None):
    vars = index_handle(request, guid)
    return render_to_response('pages/apps/buttonizer.html', vars, RequestContext(request))


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

