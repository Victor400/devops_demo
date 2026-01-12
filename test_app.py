from flask import Flask
import os

def test_movie_list():
    from app import MOVIES
    assert len(MOVIES) == 5, "Need exactly 5 movies in the list"
    print(f"Test Passed: Found {len(MOVIES)} movies.")


def test_app_starts():
    from app import app
    assert app is not None, "Flask app should be initialized"
    print("Test Passed: Flask app is initialized.")


if __name__ == '__main__':
    test_movie_list()
    test_app_starts()
    print("All tests passed.")