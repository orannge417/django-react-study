from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

# クエリセットを一覧化
class PostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# クエリセットを取得
class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
