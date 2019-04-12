from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from rest_framework.response import Response
from .models import Song
from rest_framework.decorators import api_view
from .serializers import SongSerializer


@api_view(["GET"])
def song_list(request):
    songs = get_list_or_404(Song)
    serializers = SongSerializer(songs, many=True)
    return Response(serializers.data)


@api_view(["GET", "PATCH", "DELETE"])
def song_detail(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == "PATCH":
        serializer = SongSerializer(data=request.data, instance=song)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("Song is edited!")
    else:
        song.delete()
        return Response("Song is deleted!")


@api_view(["POST"])
def create_song(request):
    serializer = SongSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)