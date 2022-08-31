import os

# EDIT
USERNAME = 'falodunosolomon@gmail.com'
PASSWORD = 'SyntaxLinkdIn!@#123'
# visual studio essential training: 01 Exploring visual studio ecosystem with Walt Risher
# visual studio essential training: 06 Debug and Troubleshoot Code with Walt Risher
# C# Test driven development by Reynald Adolphe
# Learning ASP.NET Core MVC with Jess Chadwick
# Xamarine Essential Training with Walt Risher
# Learning entity framework 6.1.3
COURSES = [
           'flutter-part-01-introduction',
           'flutter-part-02-building-apps',
           'flutter-part-03-flutter-widgets',
           'flutter-part-04-building-an-app-with-state',
           'flutter-part-05-flutter-and-dart-packages',
           'flutter-part-06-modularizing-and-organizing-flutter-code',
           'flutter-part-07-building-the-ui-or-flutter-part-07-building-uis',
           'flutter-part-08-powering-your-app-with-live-web-data',
           'flutter-part-09-dart-cupertino-and-widgets',
           'flutter-part-10-firebase-cloud-firestore'
]

# EDIT IF YOU NEED TO
BASE_DOWNLOAD_PATH = os.path.join(os.path.dirname(__file__), "downloads")
USE_PROXY = False
PROXY = "http://127.0.0.1:8888" if USE_PROXY else None
