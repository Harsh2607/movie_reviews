from rest_framework import viewsets
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import render, redirect
from .forms import ReviewForm

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()
    

def review_list_view(request, movie_id):
    reviews = Review.objects.filter(movie_id=movie_id)
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

def add_review_view(request, movie_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie_id = movie_id
            review.user = request.user
            review.save()
            return redirect('movie_detail', pk=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})