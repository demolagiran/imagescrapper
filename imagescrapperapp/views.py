from django.shortcuts import render , redirect
from bs4 import BeautifulSoup
import requests
from .models import Scrapedimage
    
#def your_view(request):


#def getImage(url):
    #r = requests.get(url)
    #return r.text

def copimage(request):
    if request.method == 'POST':
        def getImage(url):
            r = requests.get(url)
        return r.text
        html_data = getImage('https://www.formpl.us/features')
        soup = BeautifulSoup(html_data, "lxml")
        for item in soup.find_all('img'):
            #item['src']
            imageurl = Scrapedimage(image_url=item['src'])
            imageurl.save()
        #return redirect('/')
    return render(request, 'index.html')#, {'images' : images})

def viewImage(request):
    images = Scrapedimage.objects.all()
    return render(request, 'index.html', {'images' : images})
    

#item = ScrapedImage()
#item.save()

#imageList.append(imageurl)
        
        #for i in item:
            #item_data = {'image' : Scrapedimage.image_url}
            #output.append(item_data)
        #print(item['src'])
        #imageurl = item['src']
                #images = Scrapedimage.objects.all()
                #imageurl = Scrapedimage()
#imageurl = ScrapedImage.objects.create()
                #imageurl = item['src']
# Create your views here.
 #print(item['src'])
            #images = Scrapedimage.objects.all()
