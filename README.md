# Survey Recommender

The Survey Recommender is a system designed to recommend friends with similar interests to students touring the Knowledge Engineering Lab. It utilizes survey question responses to match students based on their shared tendencies and interests.

## Features
- **Survey-Based Matching**: Uses survey responses to match students with similar interests.
- **User-Friendly Interface**: Simple and intuitive UI for easy navigation.
- **Real-Time Recommendations**: Provides instant friend recommendations based on survey results.

## Project Structure

```plaintext
Survey-Recommender-main
├── manage.py                         # Django project management script
├── kel_site                          # Main Django project directory
│   ├── settings.py                   # Django settings file
│   ├── urls.py                       # URL routing definitions
│   └── wsgi.py                       # WSGI configuration file
└── survey                            # Survey application directory
    ├── models.py                     # Database models definition
    ├── urls.py                       # Survey application URL routing
    ├── views.py                      # Handles HTTP requests and recommendation logic
    ├── static                        # Static files directory
    │   └── survey
    │       └── common                # Common static files (CSS, JS, images)
    └── templates                     # HTML templates directory
        └── survey
            ├── index.html            # Survey input form template
            └── result.html           # Recommendation results page template
```

## Demo
### Main Page
<img src="https://github.com/hoon0303/Survey-Recommender/assets/53135286/5d3ea39e-2abb-4398-bc4a-d2d8b1e37b16" alt="Main Page" width="650">

### Survey Page
<img src="https://github.com/hoon0303/Survey-Recommender/assets/53135286/52a73fce-b651-4e1e-9eba-c0d3df41596d" alt="Survey Page" width="650">

### Result Page
<img src="https://github.com/hoon0303/Survey-Recommender/assets/53135286/e89b4397-0a7e-4020-9a6e-e9b0c39baaaf" alt="Result Page" width="650">

