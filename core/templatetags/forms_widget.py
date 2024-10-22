from django import template

register = template.Library()

@register.filter('input_css')
def input_css(field, css):
    return field.as_widget(attrs={'class': css})

@register.filter('label_css')
def label_css(field, css):
    label = field.label_tag(attrs={'class': css})
    return label

@register.inclusion_tag('misc/flowbite_forms.html')
def form_flowbite(form):
    return {'form': form }