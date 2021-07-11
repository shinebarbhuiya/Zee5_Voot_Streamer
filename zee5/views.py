from django.shortcuts import render
import requests
import validators


# Create your views here.
def home(request):

    context = {}
    return render(request, 'index.html', context)


def error(request):

    return render(request, 'error.html')



def zee5(request):



    # link = input("Enter the movie link:")
    link = request.GET.get('url' , 'https://www.zee5.com/movies/details/radhe-your-most-wanted-bhai/0-0-399328')

    valid = validators.url(link)

    if valid:
        url = f"https://zee5api.herokuapp.com/z5api.php?q={link}"

        r = requests.get(url, headers= {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36"})

        json_data = r.json()

        if json_data['title'] == 'null':
            return error(request) 

        else:

            title = json_data['title']
            desc = json_data['description']
            thumbnail = json_data['thumbnail']
            main_link = json_data['video_url']



            context = {
                'title' : title,
                'desc' : desc,
                'thumbnail' : thumbnail,
                'main_link' : main_link,
            }
    else:
        return error(request)


    
    
    return render(request, 'zee5.html', context)