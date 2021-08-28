from datetime import date

from django.shortcuts import render

# Create your views here.

all_posts = [
    # {
    #     "slug": "hike-in-the-mountains",
    #     "image": "mountains.jpg",
    #     "author": "Matt Sirkis",
    #     "date": date(2021, 8, 26),
    #     "title": "Mountain Hiking",
    #     "excerpt": "I can't wait to get back to the mountains..",
    #     "content": """Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #             """
    # },
    # {
    #     "slug": "programming-is-fun",
    #     "image": "code.png",
    #     "author": "Matt Sirkis",
    #     "date": date(2022, 3, 10),
    #     "title": "Programming Is Great!",
    #     "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "into-the-woods",
    #     "image": "woods.jpg",
    #     "author": "Matt Sirkis",
    #     "date": date(2020, 8, 5),
    #     "title": "Into The Woods",
    #     "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # }
]

def get_date(post):
    return post["date"]


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)

    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_details(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-details.html", {
        "post": identified_post
    })
