from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Categories, Entries



def index( request):
     context = {}
     return render( request, 'show_2016/index.html', context)


def entry_form( request):
     entry_list = range( 1, 9)
     context = { 'entry_list' : entry_list }
     all_categories = Categories.objects.all()
     context[ 'all_categories'] = all_categories
     return render( request, 'show_2016/entry_form.html', context)


def entry_action( request):
     entry = Entries()
     entry.name = request.POST[ 'name']
     entry.address = request.POST[ 'address']
     entry.city = request.POST[ 'city']
     entry.state = request.POST[ 'state']
     entry.zip = request.POST[ 'zip']
     entry.email = request.POST[ 'email']
     entry.phone = request.POST[ 'phone']
     entry.pic1_title = request.POST[ 'pic1_title']
     entry.pic2_title = request.POST[ 'pic2_title']
     entry.pic3_title = request.POST[ 'pic3_title']
     entry.pic4_title = request.POST[ 'pic4_title']
     entry.pic5_title = request.POST[ 'pic5_title']
     entry.pic6_title = request.POST[ 'pic6_title']
     entry.pic7_title = request.POST[ 'pic7_title']
     entry.pic8_title = request.POST[ 'pic8_title']
     if ( len( entry.pic1_title) > 0):
          catid = request.POST[ 'pic1_category']
          entry.pic1_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic2_title) > 0):
          catid = request.POST[ 'pic2_category']
          entry.pic2_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic3_title) > 0):
          catid = request.POST[ 'pic3_category']
          entry.pic3_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic4_title) > 0):
          catid = request.POST[ 'pic4_category']
          entry.pic4_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic5_title) > 0):
          catid = request.POST[ 'pic5_category']
          entry.pic5_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic6_title) > 0):
          catid = request.POST[ 'pic6_category']
          entry.pic6_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic7_title) > 0):
          catid = request.POST[ 'pic7_category']
          entry.pic7_category = Categories.objects.get( id=catid).name_string()
     if ( len( entry.pic8_title) > 0):
          catid = request.POST[ 'pic8_category']
          entry.pic8_category = Categories.objects.get( id=catid).name_string()
     entry.date = timezone.now()
     entry.save()
     context = {}
     context[ 'entry' ]= entry
     return render( request, 'show_2016/entry_confirm.html', context)


def list_entries( request):
     all_entries = Entries.objects.all()
     totalentries = 0
     totalpics = 0
     income = 0
     for entry in all_entries:
          totalentries = totalentries + 1
          totalpics = totalpics + entry.num_pics()
          income = income + entry.entry_fee()
     context = { 'all_rows' : all_entries}
     context[ 'totalentries' ] = totalentries
     context[ 'totalpics' ] = totalpics
     context[ 'income' ] = income
     return render( request, 'show_2016/list_entries.html', context)


def list_pics( request, sortkey):
     piclist = build_pic_list()
     all_pics = piclist[ 'all_pics' ]
     totalpics = piclist[ 'totalpics' ]
     totalentries = piclist[ 'totalentries' ]
     income = piclist[ 'income' ]
     all_rows = all_pics
     if sortkey == 'category':
          all_rows = sorted( all_pics, key=lambda Picture: Picture.category )
     if sortkey == 'entrant' :
          all_rows = sorted( all_pics, key=lambda Picture: Picture.entrant)
     context = { 'all_rows' : all_rows}
     context[ 'totalentries' ] = totalentries
     context[ 'totalpics' ] = totalpics
     context[ 'income' ] = income
     context[ 'sortkey' ] = sortkey.capitalize()
     return render( request, 'show_2016/list_pics.html', context)


def detail( request, entryid):
     entry = Entries.objects.get( id=entryid)
     context = {'entry' : entry}
     return render( request, 'show_2016/detail.html', context)


def print_wallcards( request):
     piclist = build_pic_list()
     all_pics = piclist[ 'all_pics' ]
     context = { 'all_pics' : all_pics }
     return render( request, 'show_2016/wallcards.html', context)


def print_backtags( request):
     context = {}
     return render( request, 'show_2016/index.html', context)






class Picture( ):
     title = 'title'
     category = 'category'
     entrant = 'entrant'
     entry_id = 0
     def __init__( self, title, cat):
          self.title = title
          self.category = cat


def build_pic_list():
     all_entries = Entries.objects.order_by( 'date')
     all_pics = [ ]
     totalentries = 0
     totalpics = 0
     income = 0
     for entry in all_entries:
          totalentries = totalentries + 1
          income = income + entry.entry_fee()
          if len( entry.pic1_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic1_title, entry.pic1_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic2_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic2_title, entry.pic2_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic3_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic3_title, entry.pic3_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic4_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic4_title, entry.pic4_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic5_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic5_title, entry.pic5_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic6_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic6_title, entry.pic6_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic7_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic7_title, entry.pic7_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
          if len( entry.pic8_title) > 0:
               totalpics = totalpics + 1
               pic = Picture( entry.pic8_title, entry.pic8_category)
               pic.entrant = entry.name_string()
               pic.entry_id = entry.id
               all_pics.append( pic)
     result = {}
     result[ 'totalentries' ] = totalentries
     result[ 'totalpics' ] = totalpics
     result[ 'income' ] = income
     result[ 'all_pics' ] = all_pics
     return result
