from django import template
import locale

register = template.Library()

@register.filter
def currency(value):
    """Formata valor como moeda brasileira"""
    try:
        return f"R$ {float(value):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    except (ValueError, TypeError):
        return f"R$ 0,00"