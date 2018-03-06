from django.contrib import admin
from .models import Pet
# import pandas as pd

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
    change_list_template = 'admin/my_change_list.html'
    # date_hierarchy = 'created'
    list_filter = ['sex', 'age', 'species']


    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        # try:
        #     qs = response.context_data['cl'].queryset
        # except (AttributeError, KeyError):
        #     return response
        qs = response.context_data['cl'].queryset

        # metrics = {
        #     'total': Count('id'),
        #     'total_sales': Sum('price'),
        # }
        response.context_data['summary'] = list(
            qs
            # .values('sale__category__name')
            # .annotate(**metrics)
            # .order_by('-age')
        )
        m = 0
        f = 0
        for pet in list(qs):
            if pet.sex == 'M':
                m += 1
            elif pet.sex == 'F':
                f += 1
        response.context_data['sex_summary'] = [{'sex': 'Male', 'count': m}, {'sex': 'Female', 'count': f}]
        return response
