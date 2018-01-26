from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import model1,Code
import os
from django.shortcuts import render
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from . forms import addData

def sendmail(receiver, dirname):
    fromaddr = "rishabh23jain@gmail.com"
    toaddr = receiver

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ML model run results"

    body = "download attachment for results"

    msg.attach(MIMEText(body, 'plain'))

    filename = os.getcwd() + "/media/" + dirname + '/result.txt'
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % 'result.txt')

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "loveumom")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()



def index(request):
    form = addData(request.POST or None, request.FILES)
    email = ""
    dirname = ""
    lowerlimit = ""
    upperlimit = ""
    emailsent = False
    if form.is_valid():
        new_data = form.save(commit=False)
        new_data.save()
        dirname = str(new_data.id)
        lowerlimit = str(new_data.lower_limit)
        upperlimit = str(new_data.upper_limit)
        email = str(new_data.email)
        olddir = os.getcwd() + '/media/' + str(new_data.file.name)
        newdir = os.getcwd() + '/media/' + dirname + '/data.txt'
        os.mkdir(os.path.join(os.getcwd() + '/media', dirname))
        os.rename(olddir, newdir)
        os.system('python ' + os.getcwd() + '/coderun/combo_ex.py ' + dirname + " " + lowerlimit + " " + upperlimit)
        sendmail(email, dirname)
        emailsent = True
    return render(request, 'coderun/model1_form.html', {'form': form, 'emailsent': emailsent, 'email': email})