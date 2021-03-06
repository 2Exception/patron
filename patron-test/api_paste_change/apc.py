import filecmp
import shutil
import os
from Tkinter import *
import inspect

invoker = os.path.basename(inspect.stack()[-1][1]).split('-')[0]

def is_service_installed(service):
    return os.path.exists('/usr/lib/python2.7/dist-packages/' + service)

def get_original_file(service):
    if service == 'nova':
        return '/etc/nova/api-paste.ini'
    elif service == 'glance':
        return '/etc/glance/glance-api-paste.ini'
    elif service == 'neutron':
        return '/etc/neutron/api-paste.ini'
    elif service == 'cinder':
        return '/etc/cinder/api-paste.ini'
    elif service == 'heat':
        return '/etc/heat/api-paste.ini'
    elif service == 'ceilometer':
        return '/etc/ceilometer/api_paste.ini'
    elif service == 'patron':
        return '/etc/patron/api-paste.ini'
    else:
        raise Exception('[get_original_file]: Service not supported!!')

def get_new_file(service):
    return '/usr/lib/python2.7/dist-packages/patron-test/api_paste_change/' + service + '-paste.ini'

def get_old_file(service):
    return '/usr/lib/python2.7/dist-packages/patron-test/api_paste_change/' + service + '-paste-old.ini'

def get_original_hook(service):
    if service == 'nova':
        return '/usr/lib/python2.7/dist-packages/nova/policy.py'
    elif service == 'glance':
        return '/usr/lib/python2.7/dist-packages/glance/api/policy.py'
    elif service == 'neutron':
        return '/usr/lib/python2.7/dist-packages/neutron/policy.py'
    elif service == 'cinder':
        return '/usr/lib/python2.7/dist-packages/cinder/policy.py'
    elif service == 'heat':
        return '/usr/lib/python2.7/dist-packages/heat/common/policy.py'
    elif service == 'ceilometer':
        return '/usr/lib/python2.7/dist-packages/ceilometer/api/rbac.py'
    if service == 'patron':
        return '/usr/lib/python2.7/dist-packages/patron/policy.py'
    else:
        raise Exception('[get_original_hook]: Service not supported!!')

def get_new_hook(service):
    return './' + service + '-policy.py'

def get_old_hook(service):
    return './' + service + '-policy-old.py'

def is_aem_enabled(service):
    if filecmp.cmp(get_original_file(service), get_new_file(service)) == True:
        return True
    elif filecmp.cmp(get_original_file(service), get_old_file(service)) == True:
        return False
    else:
        raise Exception('Original api-paste.ini file not recognized!!')

def is_aem_enabled2(service):
    f = open(get_original_hook(service), 'r')
    text = f.read()

    m = re.search('##apc hook##', text)
    if m != None:
        res = False
    else:
        res = True

    f.close
    return res

# add aem into api.ini
def toggle_aem(service, enable):
    if enable == True:
        shutil.copyfile(get_new_file(service), get_original_file(service))
        # shutil.copyfile(get_new_hook(service), get_original_hook(service))
    else:
        shutil.copyfile(get_old_file(service), get_original_file(service))
        # shutil.copyfile(get_old_hook(service), get_original_hook(service))

apc_log_hook_code = '''f = open('/var/log/tempest/tempest.log','a+')
    f.write(" $ %r\\n" % action)
    f.close()'''

apc_log_hook_code2 = '''f = open('/var/log/tempest/tempest.log','a+')
        f.write(" $ %r\\n" % action)
        f.close()'''

# add policy hooks into service
def toggle_aem2(service, enable):
    f = open(get_original_hook(service), 'r+')
    text = f.read()
    if service == 'nova' or service == 'neutron' or service == 'cinder' or service == 'ceilometer' or service == 'patron':
        hook_code = apc_log_hook_code
    elif service == 'glance' or service == 'heat':
        hook_code = apc_log_hook_code2
    else:
        raise Exception('[toggle_aem2]: Service not supported!!')

    if enable:
        # new_text = re.sub('##apc hook##', apc_log_hook_code, text)
        new_text = text.replace('##apc hook##', hook_code)
        f.seek(0, 0)
        f.truncate()
        f.write(new_text)
    else:
        # new_text = re.sub(apc_log_hook_code, '##apc hook##', text)
        new_text = text.replace(hook_code, '##apc hook##')
        f.seek(0, 0)
        f.truncate()
        f.write(new_text)

    f.close

def is_aem_variable_enabled(var):
    if var == 'aem':
        var = 'aem_to_patron_enabled';
    elif var == 'cache':
        var = 'cache_enabled'
    else:
        raise Exception('[toggle_aem_variable]: Variable not supported!!')

    f = open('/usr/lib/python2.7/dist-packages/patron/aem/patron_verify.py', 'r')
    text = f.read()

    m = re.search(var + ' = True', text)
    if m != None:
        res = True
    else:
        res = False

    f.close
    return res

# decide whether aem and cache is on or off
def toggle_aem_variable(var, enable):
    if var == 'aem':
        var = 'aem_to_patron_enabled';
    elif var == 'cache':
        var = 'cache_enabled'
    else:
        raise Exception('[toggle_aem_variable]: Variable not supported!!')

    f = open('/usr/lib/python2.7/dist-packages/patron/aem/patron_verify.py', 'r+')
    text = f.read()

    if enable:
        new_text = re.sub(var + ' = False', var + ' = True', text)
        f.seek(0, 0)
        f.truncate()
        f.write(new_text)
    else:
        new_text = re.sub(var + ' = True', var + ' = False', text)
        f.seek(0, 0)
        f.truncate()
        f.write(new_text)

    f.close

def restart_service(service):
    if service == 'nova':
        output = os.popen('sudo service nova-api restart')
    elif service == 'glance':
        output = os.popen('sudo service glance-api restart')
    elif service == 'neutron':
        output = os.popen('sudo service neutron-server restart')
    elif service == 'cinder':
        output = os.popen('sudo service cinder-api restart')
    elif service == 'heat':
        output = os.popen('sudo service heat-api restart')
    elif service == 'ceilometer':
        output = os.popen('sudo service ceilometer-api restart')
    elif service == 'patron':
        output = os.popen('sudo service patron-api restart')
    else:
        raise Exception('[restart_service]: Service not supported!!')
    res = output.read()
    return res

# toggle_aem('nova', False)
# res = is_aem_enabled('nova')
# print res
# restart_service('nova')

#####################################################################################################################

buttonStatus = {}

def sel_aem():
    service = 'aem'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_cache():
    service = 'cache'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_nova():
    service = 'nova'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_glance():
    service = 'glance'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_neutron():
    service = 'neutron'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_cinder():
    service = 'cinder'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_heat():
    service = 'heat'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_ceilometer():
    service = 'ceilometer'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def sel_patron():
    service = 'patron'
    res = str(globals()[service + 'Var'].get())
    selection = "You selected the option: " + res
    setText(selection)
    if res == 'enable':
        res_bool = True
    else:
        res_bool = False
    handleRadioButton(service, res_bool)

def handleRadioButton(service, enable):
    print (service, enable)
    if service == 'aem' or service == 'cache':
        toggle_aem_variable(service, enable)
    else:
        toggle_aem(service, enable)
        toggle_aem2(service, enable)
        restart_service(service)

def handleButton_nova():
    res = restart_service('nova')
    print res
    setText(res)

def handleButton_glance():
    res = restart_service('glance')
    print res
    setText(res)

def handleButton_neutron():
    res = restart_service('neutron')
    print res
    setText(res)

def handleButton_cinder():
    res = restart_service('cinder')
    print res
    setText(res)

def handleButton_heat():
    res = restart_service('heat')
    print res
    setText(res)

def handleButton_ceilometer():
    res = restart_service('ceilometer')
    print res
    setText(res)

def handleButton_patron():
    res = restart_service('patron')
    print res
    setText(res)

def setRadioButton(service, enable):
    if enable:
        globals()[service + 'Var'].set('enable')
    else:
        globals()[service + 'Var'].set('disable')

novaState = is_service_installed('nova')
glanceState = is_service_installed('glance')
neutronState = is_service_installed('neutron')
cinderState = is_service_installed('cinder')
heatState = is_service_installed('heat')
ceilometerState = is_service_installed('ceilometer')
patronState = is_service_installed('patron')

def setDefaultRadioButtons():
    setRadioButton('aem', is_aem_variable_enabled('aem'))
    setRadioButton('cache', is_aem_variable_enabled('cache'))
    if novaState: setRadioButton('nova', is_aem_enabled('nova'))
    if glanceState: setRadioButton('glance', is_aem_enabled('glance'))
    if neutronState: setRadioButton('neutron', is_aem_enabled('neutron'))
    if cinderState: setRadioButton('cinder', is_aem_enabled('cinder'))
    if heatState: setRadioButton('heat', is_aem_enabled('heat'))
    if ceilometerState: setRadioButton('ceilometer', is_aem_enabled('ceilometer'))
    if patronState: setRadioButton('patron', is_aem_enabled('patron'))

    # setRadioButton('nova', True)
    # setRadioButton('glance', False)
    # setRadioButton('neutron', False)

def setText(str):
    label.config(text = str)

def clearTempestLog():
    f = open('/var/log/tempest/tempest.log', 'w+')
    f.truncate()
    f.close
    setText('/var/log/tempest/tempest.log\nhas been cleared!')

root = Tk()
root.geometry('600x500+10+10')

aemVar = StringVar()
cacheVar = StringVar()
novaVar = StringVar()
glanceVar = StringVar()
neutronVar = StringVar()
cinderVar = StringVar()
heatVar = StringVar()
ceilometerVar = StringVar()
patronVar = StringVar()

setDefaultRadioButtons()

labelframe_top = LabelFrame(root, text="", borderwidth=0)
labelframe_top.pack(side="top", fill="both", expand="yes")
labelframe_bottom = LabelFrame(root, text="", borderwidth=0)
labelframe_bottom.pack(side="bottom", fill="both", expand="yes")
labelframe_left = LabelFrame(labelframe_top, text="", borderwidth=0)
labelframe_left.pack(side="left", fill="both", expand="yes")
labelframe_right = LabelFrame(labelframe_top, text="", borderwidth=0)
labelframe_right.pack(side="right", fill="both", expand="yes")


labelframe_aem = LabelFrame(labelframe_left, text="AEM")
labelframe_aem.pack(fill="both", expand="yes")
labelframe_nova = LabelFrame(labelframe_left, text="nova")
labelframe_nova.pack(fill="both", expand="yes")
labelframe_glance = LabelFrame(labelframe_left, text="glance")
labelframe_glance.pack(fill="both", expand="yes")
labelframe_neutron = LabelFrame(labelframe_left, text="neutron")
labelframe_neutron.pack(fill="both", expand="yes")
labelframe_cinder = LabelFrame(labelframe_right, text="cinder")
labelframe_cinder.pack(fill="both", expand="yes")
labelframe_heat = LabelFrame(labelframe_right, text="heat")
labelframe_heat.pack(fill="both", expand="yes")
labelframe_ceilometer = LabelFrame(labelframe_right, text="ceilometer")
labelframe_ceilometer.pack(fill="both", expand="yes")
labelframe_patron = LabelFrame(labelframe_right, text="patron")
labelframe_patron.pack(fill="both", expand="yes")

Radiobutton(labelframe_aem, text="AEM -> patron [ON]", variable=aemVar, value='enable', command=sel_aem).pack()
Radiobutton(labelframe_aem, text="AEM -> patron [OFF]", variable=aemVar, value='disable', command=sel_aem).pack()
Radiobutton(labelframe_aem, text="AEM cache [ON]", variable=cacheVar, value='enable', command=sel_cache).pack()
Radiobutton(labelframe_aem, text="AEM cache [OFF]", variable=cacheVar, value='disable', command=sel_cache).pack()
Button(labelframe_aem, text ="Clear tempest.log", command = clearTempestLog).pack()

Radiobutton(labelframe_nova, text="Nova's AEM and hook [ON]", variable=novaVar, value='enable', command=sel_nova, state = NORMAL if novaState else DISABLED).pack()
Radiobutton(labelframe_nova, text="Nova's AEM and hook [OFF]", variable=novaVar, value='disable', command=sel_nova, state = NORMAL if novaState else DISABLED).pack()
Button(labelframe_nova, text ="Restart nova-api", command = handleButton_nova, state = NORMAL if novaState else DISABLED).pack()

Radiobutton(labelframe_glance, text="Glance's AEM and hook [ON]", variable=glanceVar, value='enable', command=sel_glance, state = NORMAL if glanceState else DISABLED).pack()
Radiobutton(labelframe_glance, text="Glance's AEM and hook [OFF]", variable=glanceVar, value='disable', command=sel_glance, state = NORMAL if glanceState else DISABLED).pack()
Button(labelframe_glance, text ="Restart glance-api", command = handleButton_glance, state = NORMAL if glanceState else DISABLED).pack()

Radiobutton(labelframe_neutron, text="Neutron's AEM and hook [ON]", variable=neutronVar, value='enable', command=sel_neutron, state = NORMAL if neutronState else DISABLED).pack()
Radiobutton(labelframe_neutron, text="Neutron's AEM and hook [OFF]", variable=neutronVar, value='disable', command=sel_neutron, state = NORMAL if neutronState else DISABLED).pack()
Button(labelframe_neutron, text ="Restart neutron-server", command = handleButton_neutron, state = NORMAL if neutronState else DISABLED).pack()

Radiobutton(labelframe_cinder, text="Cinder's AEM and hook [ON]", variable=cinderVar, value='enable', command=sel_cinder, state = NORMAL if cinderState else DISABLED).pack()
Radiobutton(labelframe_cinder, text="Cinder's AEM and hook [OFF]", variable=cinderVar, value='disable', command=sel_cinder, state = NORMAL if cinderState else DISABLED).pack()
Button(labelframe_cinder, text ="Restart cinder-api", command = handleButton_cinder, state = NORMAL if cinderState else DISABLED).pack()

Radiobutton(labelframe_heat, text="Heat's AEM and hook [ON]", variable=heatVar, value='enable', command=sel_heat, state = NORMAL if heatState else DISABLED).pack()
Radiobutton(labelframe_heat, text="Heat's AEM and hook [OFF]", variable=heatVar, value='disable', command=sel_heat, state = NORMAL if heatState else DISABLED).pack()
Button(labelframe_heat, text ="Restart heat-api", command = handleButton_heat, state = NORMAL if heatState else DISABLED).pack()

Radiobutton(labelframe_ceilometer, text="Ceilometer's AEM and hook [ON]", variable=ceilometerVar, value='enable', command=sel_ceilometer, state = NORMAL if ceilometerState else DISABLED).pack()
Radiobutton(labelframe_ceilometer, text="Ceilometer's AEM and hook [OFF]", variable=ceilometerVar, value='disable', command=sel_ceilometer, state = NORMAL if ceilometerState else DISABLED).pack()
Button(labelframe_ceilometer, text ="Restart ceilometer-api", command = handleButton_ceilometer, state = NORMAL if ceilometerState else DISABLED).pack()

Radiobutton(labelframe_patron, text="Patron's AEM and hook [ON]", variable=patronVar, value='enable', command=sel_patron, state = NORMAL if patronState else DISABLED).pack()
Radiobutton(labelframe_patron, text="Patron's AEM and hook [OFF]", variable=patronVar, value='disable', command=sel_patron, state = NORMAL if patronState else DISABLED).pack()
Button(labelframe_patron, text ="Restart patron-api", command = handleButton_patron, state = NORMAL if patronState else DISABLED).pack()


label = Label(labelframe_bottom)
label.pack()
root.title("API Paste Change (APC)")
if invoker == "apc.py":
    root.mainloop()