from django.shortcuts import render
from ArtI.models import Creation, Creator, Category


def homepage(request):
    artists = Creator.objects.all()
    creations = Creation.objects.all()
    return render(
        request, "ArtI/homepage.html", {"artists": artists, "creations": creations}
    )


def our_artists(request):
    artists = Creator.objects.all()
    return render(request, "ArtI/our_artists.html", {"artists": artists})


def artist_detail(request, id):
    artist = Creator.objects.get(id=id)
    return render(request, "ArtI/artist_detail.html", {"artist": artist})


def browse_creations(request):
    creations = Creation.objects.all()
    return render(request, "ArtI/browse_creations.html", {"creations": creations})


def creation_detail(request, id):
    creation = Creation.objects.get(id=id)
    return render(request, "ArtI/creation_detail.html", {"creation": creation})
