def getData(form, fieldname):
    return form.cleaned_data.get(fieldname)
