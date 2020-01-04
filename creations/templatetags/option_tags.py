from django import template
from ..models import option,slider

register =  template.Library()

@register.inclusion_tag('creations/footer.html')
def show_footer():
    options = option.objects.all()
    return {'options':options }

@register.inclusion_tag('creations/slider.html')
def show_slider():
    sliders = slider.objects.all()
    return {'sliders':sliders}