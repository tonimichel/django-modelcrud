from django import template
import types

register = template.Library()

@register.inclusion_tag('modelcrud/list_table.tag.html')
def render_list(obj, object_list):
    """
    Renders the list view object list taking the passed object's
    crudconf.list_display into account.
    """
    head = []
    for fname in obj.crudconf.get_list_display():
        if fname in [f.name for f in type(obj)._meta.get_fields()]:
            head.append(type(obj)._meta.get_field(fname).verbose_name)
        else:
            try:
                """
                try the fieldname foo from getter method get_foo_display()
                """
                head.append(type(obj)._meta.get_field(fname.replace('get_','').replace('_display','')).verbose_name)
            except:
                head.append('unknown')

    rows = []
    for entry in object_list:
        rows.append(
            dict(
                obj=entry,
                values=[getattr(entry, fname)() if isinstance(getattr(entry, fname), types.MethodType) \
                    else getattr(entry, fname) for fname in obj.crudconf.get_list_display()]
            )
        )
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
