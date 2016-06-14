from django import template
import types
from django.core.exceptions import FieldDoesNotExist
import datetime

register = template.Library()

@register.inclusion_tag('modelcrud/list_table.tag.html')
def render_list(obj, object_list):
    """
    Renders the list view object list taking the passed object's
    crudconf.list_display into account.
    """
    head = []
    list_display = obj.crudconf.get_list_display()
    for fname in list_display:


        if '__' in fname:
            rel_attr = fname.split('__')[1]
            rel_field_name = fname.split('__')[0]
            field = type(obj)._meta.get_field(rel_field_name)
            rel_field = field.rel.to._meta.get_field(rel_attr)
            label=rel_field.verbose_name
        else:
            try:
                label=type(obj)._meta.get_field(fname).verbose_name
            except FieldDoesNotExist as e:

                getter = getattr(obj, fname)
                label = getattr(getter, 'short_description', fname)

        head.append(dict(
            name=fname,
            label=label
        ))


    rows = []
    for i, entry in enumerate(object_list):
        row = dict(
            obj=entry,
            values=[]
        )
        for field_name in list_display:

            if '__' in field_name:

                rel_name = field_name.split('__')[0]
                rel_attr = field_name.split('__')[1]

                obj = getattr(entry, rel_name)
                value = getattr(obj, rel_attr)

                row['values'].append(value)
            else:
                row['values'].append(getattr(entry, field_name)() if isinstance(getattr(entry, field_name), types.MethodType) \
                    else getattr(entry, field_name))

        rows.append(row)




    return dict(
        head=head,
        rows=rows
    )



@register.inclusion_tag('modelcrud/details.tag.html')
def render_details(obj):
    """
    Renders the detail view properties taking the passed object's
    crudconf.detail_properties into account.
    """
    props = []
    for fname in obj.crudconf.get_detail_properties():
        props.append(dict(
            label=type(obj)._meta.get_field(fname).verbose_name,
            value=getattr(obj, fname),
        ))
    return dict(
        properties=props
    )


@register.filter
def isinstance_datetime(value):
    return isinstance(value, datetime.date)