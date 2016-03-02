from django import template

register = template.Library()

@register.inclusion_tag('modelcrud/list_table.tag.html')
def render_list(obj, object_list):
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
    props = []
    for fname in obj.crudconf.get_list_display():
        props.append(dict(
            label=type(obj)._meta.get_field(fname).verbose_name,
            value=getattr(obj, fname),
        ))
    return dict(
        properties=props
    )
