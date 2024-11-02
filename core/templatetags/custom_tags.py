from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='split_url', is_safe=True)
@stringfilter
def split_url(string, sep):
    return string.split(sep)

@register.filter(name='path_name', is_safe=True)
@stringfilter
def path_name(string):
    return string.split('/')[1]

@register.simple_tag
@stringfilter
def path_name_css(url, equal, **kwargs):
    path = url.split('/')[1]
    if path == equal:
        return kwargs['selected']
    else:
        return kwargs['default']


@register.filter('input_css')
def input_css(field, css):
    return field.as_widget(attrs={'class': css})

@register.filter('label_css')
def label_css(field, css):
    label = field.label_tag(attrs={'class': css})
    return label

@register.inclusion_tag('components/flowbite_forms.html')
def form_flowbite(form):
    return {'form': form }

@register.inclusion_tag('components/empty.html')
def empty_list(**kwargs):
    return kwargs

@register.inclusion_tag('components/alert_modal.html')
def alert_modal(**kwargs):
    return kwargs

@register.inclusion_tag('components/fab-button.html')
def fab_button(**kwargs):
    return kwargs