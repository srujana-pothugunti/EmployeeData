from django.shortcuts import render
from django.http import Http404
from .models import User,JobDetails
from rest_framework.views import APIView
from django.views.generic import DetailView,UpdateView
from django.core.paginator import Paginator, EmptyPage

class Index(APIView):
    def get(self, request):
        employee_list = JobDetails.objects.all().order_by('id')
        p = Paginator(employee_list, 10)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        return render(request, 'index.html', {'employee_data':page})

class Detail(DetailView):
    model = JobDetails
    template_name = 'detail.html'
    fields = '__all__'
    context_object_name = "employee_detail"
