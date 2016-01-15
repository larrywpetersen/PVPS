from django.db import models
from django.utils import timezone



class Categories( models.Model):
    name = models.CharField( max_length=100 )
    def name_string( self):
        return self.name
    def __str__( self):
        return self.name_string()



class Entries( models.Model):
    name = models.CharField( max_length=100 ) 
    address = models.CharField( max_length=100 )
    city = models.CharField( max_length=100 )
    state = models.CharField( max_length=100 )
    zip = models.CharField( max_length=100 )
    email = models.CharField( max_length=100 )
    phone = models.CharField( max_length=100 )
    pic1_title = models.CharField( max_length=100 )
    pic2_title = models.CharField( max_length=100 )
    pic3_title = models.CharField( max_length=100 )
    pic4_title = models.CharField( max_length=100 )
    pic5_title = models.CharField( max_length=100 )
    pic6_title = models.CharField( max_length=100 )
    pic7_title = models.CharField( max_length=100 )
    pic8_title = models.CharField( max_length=100 )
    pic1_category = models.CharField( max_length=50, default="" )
    pic2_category = models.CharField( max_length=50, default="" )
    pic3_category = models.CharField( max_length=50, default="" )
    pic4_category = models.CharField( max_length=50, default="" )
    pic5_category = models.CharField( max_length=50, default="" )
    pic6_category = models.CharField( max_length=50, default="" )
    pic7_category = models.CharField( max_length=50, default="" )
    pic8_category = models.CharField( max_length=50, default="" )
    pic1_price = models.CharField( max_length=30, default="")
    pic2_price = models.CharField( max_length=30, default="")
    pic3_price = models.CharField( max_length=30, default="")
    pic4_price = models.CharField( max_length=30, default="")
    pic5_price = models.CharField( max_length=30, default="")
    pic6_price = models.CharField( max_length=30, default="")
    pic7_price = models.CharField( max_length=30, default="")
    pic8_price = models.CharField( max_length=30, default="")
    date = models.DateTimeField( default=timezone.now() )
    def name_string( self):
        return self.name
    def address_string( self):
        msg = self.address + ', ' + self.city + ', '
        msg = msg + self.state + ', ' + self.zip
        return msg
    def num_pics( self):
        n = 0
        if ( len( self.pic1_title) > 1):
            n = n + 1
        if ( len( self.pic2_title) > 1):
            n = n + 1
        if ( len( self.pic3_title) > 1):
            n = n + 1
        if ( len( self.pic4_title) > 1):
            n = n + 1
        if ( len( self.pic5_title) > 1):
            n = n + 1
        if ( len( self.pic6_title) > 1):
            n = n + 1
        if ( len( self.pic7_title) > 1):
            n = n + 1
        if ( len( self.pic8_title) > 1):
            n = n + 1
        return n
    def entry_fee( self):
        return self.num_pics() * 9
    def __str__( self):
        return self.name_string() + ' - ' + self.address_string()
    def date_string(self):
        msg = self.date.strftime( '%b %d, %Y')
        return msg



