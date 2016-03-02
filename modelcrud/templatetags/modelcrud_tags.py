from django import template

register = template.Library()

@register.inclusion_tag('modelcrud/list_table.tag.html')
def render_list(obj, object_list):
    """
    Renders the list view object list taking the passed object's
    crudconf.list_display into account.
    """
    head = []
    for fname in obj.crudconf.get_list_display():
        head.append(type(obj)._meta.get_field(fname).verbose_name)

    rows = []
    for entry in object_list:
        rows.append(
            dict(
                obj=entry,
                values=[getattr(entry, fname) for fname in obj.crudconf.get_list_display()]
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
