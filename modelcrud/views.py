# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.forms import modelform_factory


def list_view(request, modelclass=None, template='modelcrud/list.html', extra_context=dict()):
    """
    Generische Listenansicht zur Darstellung von Objekten.
    """
    context = dict(
        object_list=modelclass.objects.all(),
        obj=modelclass(),
    )
    context.update(extra_context)
    return render(request, template, context)


def create_view(request, modelclass=None, template='modelcrud/create.html', extra_context=dict()):
    """
    Generic View zum Anlegen von Objekten.
    """
    # instanziere leeres, ungespeichertes Objekt um auf viewinfo-Objekt
    # zugreifen zu können; Instanz hat sonst keinen weiteren nutzen.
    obj = modelclass()
    formclass = modelform_factory(modelclass, exclude=[])

    if request.method == 'POST':
        form = formclass(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(obj.crudconf.get_list_url())
    else:
        form = formclass()

    context = dict(
        obj=obj,
        form=form,
    )
    context.update(extra_context)
    return render(request, template, context)


def detail_view(request, id, modelclass=None, template='modelcrud/detail.html', extra_context=dict()):
    """
    Generic View zum Darstellen der Detailansicht von Objekten.
    """


    context = dict(
        obj=modelclass.objects.get(pk=id)
    )
    context.update(extra_context)
    return render(request, template, context)

def change_view(request, id, modelclass=None, template='modelcrud/change.html', extra_context=dict()):
    """
    Generic View zum Darstellen der Detailansicht von Objekten.
    """

    obj = modelclass.objects.get(pk=id)
    formclass = modelform_factory(modelclass, exclude=[])

    if request.method == 'POST':
        form = formclass(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(obj.crudconf.get_list_url())
    else:
        form = formclass(instance=obj)

    context = dict(
        obj=obj,
        form=form
    )
    context.update(extra_context)
    return render(request, template, context)


def delete_view(request, id, modelclass=None, template='modelcrud/delete.html', extra_context=dict()):
    """
    Generic View zum Darstellen der Detailansicht von Objekten.
    """

    obj = modelclass.objects.get(pk=id)

    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect(obj.crudconf.get_list_url())

    context = dict(
        obj=obj,
    )
    context.update(extra_context)
    return render(request, template, context)
