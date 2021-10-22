from django.http import JsonResponse
import praw
from .app_config import REDDIT_AUTH

# Create your views here.

def get_reddit_titles(request):

    reddit = praw.Reddit(
        client_id= REDDIT_AUTH['client_id'],
        client_secret= REDDIT_AUTH['client_secret'],
        user_agent= REDDIT_AUTH['user_agent'])

    try:
        hot_topics = reddit.subreddit('all').hot(limit=5)
        json = {
            "Success" : True,
            "Message" : "\\n".join([post.title for post in hot_topics])
        }

    except Exception as e:
        json = {
        'Success' : False,
        'message' : e
        }

    return JsonResponse(json)



