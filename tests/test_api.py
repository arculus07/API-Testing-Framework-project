import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200, "Failed to fetch posts"
    assert len(response.json()) == 100, "Expected 100 posts"
    assert "title" in response.json()[0], "Title field missing"

def test_get_post_by_id():
    response = requests.get(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "Failed to fetch post"
    assert response.json()["id"] == 1, "Incorrect post ID"

def test_get_invalid_post():
    response = requests.get(f"{BASE_URL}/posts/999")
    assert response.status_code == 404, "Expected 404 for invalid ID"

def test_post_new_post():
    new_post = {"title": "Test Post", "body": "This is a test", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201, "Failed to create post"
    assert response.json()["title"] == "Test Post", "Title mismatch"

def test_post_invalid_data():
    invalid_post = {"title": "", "body": "", "userId": -1}
    response = requests.post(f"{BASE_URL}/posts", json=invalid_post)
    assert response.status_code in [400, 422, 201], "Unexpected status code"