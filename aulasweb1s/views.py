from django.shortcuts import render, get_object_or_404
from .models import Entry

def entry_list(request):
    entries = Entry.objects.all()
    return render(request, 'entries/entry_list.html', {'entries': entries})

def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, 'entries/entry_detail.html', {'entry': entry})
