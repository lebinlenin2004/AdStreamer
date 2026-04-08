# AdStreamer

AdStreamer is a centralized, production-ready digital signage and advertising management system built with Django. It provides a robust backend to dispatch, schedule, and monitor video/image advertisements across distributed screens over the internet.

## Architecture & Tech Stack
- **Framework**: Django (Python)
- **Database**: SQLite (Configured for easy local testing, easily swappable to PostgreSQL)
- **Admin UI Theme**: django-jazzmin
- **Authentication**: Built-in Django session authentication with Custom User roles (`ADMIN`, `ADVERTISER`).

## Core Modules & Apps
The project follows a clean, modular architecture divided into specific functional Django apps:

1. **`accounts`**: Manages custom User models (extending `AbstractUser`), defining roles, profiles, and basic authentication flows.
2. **`content`**: The core media engine. Handles the upload, storage, and approval status of `Ad` media (videos, images). It also manages `AdAssignments`, which dictates the start date, end date, and order in which an ad plays on a given screen.
3. **`displays`**: Manages the physical hardware (`Screen`). Generates secure pairing tokens (UUIDs) that allow remote Smart TVs or Raspberry Pis to authenticate with the server.
4. **`analytics`**: Houses the telemetry engine. Listens for API pings from screens and records `AdPlayLog` entries to accurately track how many impressions an ad received.
5. **`api`**: Fast, lightweight endpoints used by the remote Screens to fetch their current schedules and report playback metrics.
6. **`core`**: The main project configuration folder housing settings, URLs, and global configurations (like the Jazzmin UI tweaks and Admin permission overrides).

## Recent Enhancements
- **Premium Admin Interface**: Integrated `django-jazzmin` for a stunning Bootstrap-powered administrative interface including specific `FontAwesome` icons and a sleek Dark/Light mode theme.
- **Admin Security**: Bypassed standard staff permissions. The `/admin/` portal has been hardcoded in `core/urls.py` to strictly allow `is_superuser` traffic only. 
- **Enhanced Filtering & Search**: The Admin portal provides deep search capabilities across ads, advertisers, and play logs.
- **Data Export**: Built-in CSV exporting tool within the Ads Play Logs to allow Administrators to download specific, filtered chronological play records. 
- **Clear Filters Button**: A custom `search_form.html` override within the `analytics` admin app provides a seamless one-click reset for deep data table analysis.

## Local Development Setup

**1. Clone & Setup Virtual Environment**
```bash
git clone <repository_url>
cd Advisor
python -m venv venv
.\venv\Scripts\activate
```

**2. Install Dependencies**
```bash
pip install django django-cors-headers djangorestframework django-jazzmin
```

**3. Run Migrations & Setup Database**
```bash
python manage.py makemigrations
python manage.py migrate
```

**4. Create Superuser (Admin)**
```bash
python manage.py createsuperuser
```

**5. Start the Server**
```bash
python manage.py runserver
```

Navigate to `http://localhost:8000/admin/` to log in to the newly styled superuser dashboard. 

## Advertiser Portal
Advertisers who are provided accounts but lack `is_superuser` privileges are directed to the main root application (`http://localhost:8000/`) where they have access to a read-only analytics dashboard tracking their specific Ad impressions. They are completely locked out of the core Jazzmin Database control panel.

## Documentation
For instructions on how to use the web interfaces from a business perspective (Approving ads, provisioning screens, etc.), please refer to the `user_manual.md` located in the root of the project.
