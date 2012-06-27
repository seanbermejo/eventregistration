from registration.models import Student, Event, Attend
from django.shortcuts import render_to_response
from django.template import RequestContext
from registration.forms import StudentForm
from auth.views import user_login_required
from django.db import connection, transaction
import datetime
import re
# Create your views here.

@user_login_required
def register_form(request):
    """ Registration Form
    from registration.forms import StudentForm 
    textbox: id_barcode
             id_last_name
    """
    context_instance=RequestContext(request)

    studentform = StudentForm() #instanc

    response = {
            'studentform' : studentform
            }
    return render_to_response('register.html', response, context_instance)


def register(request):
    """ Register Student
    triggers upon checked event(select) in jquery function 
    """
    context_instance=RequestContext(request)
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            try:
                e = Event.objects.get(pk=1)
                s = Student.objects.get(studentID=q) 
                dup = Attend.objects.filter(student=s, event=e) # check if student is registered
                if len(dup) == 0:
                    result = Attend.objects.create(student=s, event=e, time=datetime.datetime.now())
                    result.save()   # inserts data into database
            except Exception as e:
                print e
            
    return render_to_response('', {}, context_instance)

def withdraw(request):    
    """ Register Student
    triggers upon unchecked event(select) in jquery function 
    """
    context_instance=RequestContext(request)
  
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            try:
                # get student information 
                # raises database exception if it gets nothing
                attend = Attend.objects.get(student__studentID__exact=q, event__id=1)
                attend.delete()     # delete from database
            except  Exception as e:
                print e

    return render_to_response('', {}, context_instance)
    
            
def register_barcode(request):
    """ Register Student by Barcode
    triggers upon barcode input event(id_barcode) in jquery function
    """
    context_instance=RequestContext(request)
    studentform = StudentForm() # get new form: empty values
    message = ""
    data = {
        'message' : message,
        'studentform' : studentform
        }

    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            c = re.sub(r'[^\w]', '', q)     # removes special character
            p = re.compile("220..00(\d\d\d\d\d\d)") 
            m = p.match(c)  # match the barcode from the regex function
            if m is not None:
                # m.group(0) has 220xx00xxxxxx value
                studID = m.group(1) # gets last six value
                if studID:
                    try:
                        student = Student.objects.get(studentID=studID)
                        event = Event.objects.get(pk=1)
                        dup = Attend.objects.filter(student=student, event=event)  
                        if len(dup) == 0:    # check if student is registered
                            attend = Attend.objects.create(student=student, event=event, time=datetime.datetime.now())
                            attend.save()   # insert into database
                            data['message'] = "Student ID {0} : Successfully Registered".format(str(studID))
                            print "success"
                        else:
                            data['message'] = "Student ID {0} is already registered.".format(str(studID))
                                    
                    except Exception as e:
                        data['message'] = e
            else:
                data['message'] = "Error reading barcode!"

    return render_to_response('student.html', data, context_instance)

def search_attend(request):
    """ Search Attended Students
    searches only by course
    """
    context_instance=RequestContext(request)
    data = {
          'students' : "",
          'message' : "",
          }        
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            if q == '%':
                results = Attend.objects.all()
            else:
                results = Attend.objects.filter(student__course=q)

            data['students'] = results
            
            if len(results) == 0:
                data['message'] = "Your search yielded no results"
            return render_to_response('student_attended.html', data, context_instance)


def attended_form(request):
    context_instance=RequestContext(request)
    

    return render_to_response('attended.html', {}, context_instance)

@user_login_required
def event_form(request):
    """ Event Form
    Add Event ?
    Search Event ?
    Activate Event ?
    Deactivate Event ?
    """
    context_instance=RequestContext(request)
    event = Event.objects.all()
    
    response = {
            'event' : event
            }
    return render_to_response('event.html', response, context_instance)

@user_login_required
def ajax_user_search(request):
    """ Search by last_name
    triggers upon enter event(id_last_name) in jquery function
    """
    template = 'student.html'
    cursor = connection.cursor()    # establish connection database
    results = ""
    message = ""
    data = {
       'students': results,
       'message': message
         }
    if request.is_ajax():
        q = request.GET.get('q')
        if q is not None:
            print "a"   # test
            try:
                # event_id is hardcoded, it must get value in activated event
                cursor.execute("SELECT student.studentID, student.last_name, student.first_name, student.middle_initial, student.sex, student.year, student.course, student.section, attend.id as attendid from EventRegistration.student left join EventRegistration.attend on (EventRegistration.attend.event_id = 1 and EventRegistration.attend.student_id = student.id)where (EventRegistration.student.last_name like %s)", [q + "%"])
                results = cursor.fetchall()
                    
            except Exception as e:
                print e

            data['students'] = results
            if len(results) == 0:
                data['message'] = "Your search yielded no results"
            print "b"   # test
            return render_to_response(template, data,
                    context_instance = RequestContext(request))
        #http://www.nomadjourney.com/2009/01/using-django-templates-with-jquery-ajax/
