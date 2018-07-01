# coding=utf-8
import ipdb
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from task.models import Task
from task.permissions import IsOwnerOrReadOnly
from task.serializers import TaskSerializer


class TaskList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'TaskList.html'
    #permission_classes = (permissions.IsAuthenticated,)
    #authentication_classes = (BasicAuthentication, SessionAuthentication)

    def get(self, request, format=None):
        screen = request.GET.get('screen')
        if screen == u'ALL_NOT_FINISHED':
            tasks = Task.objects.filter(finished__exact=0)
        elif screen == u"SORT_BY_CREATED_DATE":
            tasks = Task.objects.all().order_by('-created')
        elif screen == u'SORT_BY_EXPIRE_DATE':
            tasks = Task.objects.all().order_by('-expire_date')
        elif screen == u'SORT_BY_PRIORITY':
            tasks = Task.objects.all().order_by('-priority')
        else:
            tasks = Task.objects.all()
        return Response({'tasks': tasks})

    def post(self, request, format=None):

        owner = request.user
        serializer_context = {'request': request, }
        serializer = TaskSerializer(data=request.data, context=serializer_context)
        if serializer.is_valid():
            serializer.save(owner=owner)
            return self.get(request)
        else:
            ipdb.set_trace()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'TaskDetail.html'
    #permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticated)
    #authentication_classes = (BasicAuthentication, SessionAuthentication)

    def get(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        return Response({'task': task})
        #
        # if request.accepted_media_type == u'application/json':
        #     serializer_context = {'request': request, }
        #     serializer = TaskSerializer(task, context=serializer_context)
        #     return Response(serializer.data)
        # else:
        #     return Response({'task': task})

    def put(self, request, pk):
        # ipdb.set_trace()
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if not serializer.is_valid():
            ipdb.set_trace()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response({'task': get_object_or_404(Task, pk=pk)})

    def delete(self, request, pk):
        # ipdb.set_trace()
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        # 删除之后回到主页
        return HttpResponseRedirect(reverse('task-list'))
        # 删除之后在原始页面 提示删除成功
        # return Response({'task': None})

    # 按理说这里不应该有post的 但是发来的HTTP request不进入另外两个函数
    def post(self, request, pk, format=None):
        # ipdb.set_trace()
        if request.data['_method'] == u'DELETE':
            # del request.data['_method']
            response = self.delete(request, pk)
            return response

        elif request.data['_method'] == u'PUT':
            # del request.data['_method']
            response = self.put(request, pk)
            return response

#
# def register(request):
#     registered = False
#     if request.method == "POST":
#         user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
#         user.save()
#         # ipdb.set_trace()
#         return redirect(reverse('task-list'))
#     else:
#         return render(request, 'register.html', {'registered': registered})
