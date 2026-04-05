# Digital Signage System Overview

We have successfully built the core centralized system for deploying and managing distributed screen content. The architecture follows a robust separation of concerns, balancing ease of management through dashboards with API endpoints designed strictly for lightweight client hardware.

## Implemented Features

### 1. Unified Dashboards
- **Admin Dashboard**: Provides the top-level view of all active hardware (`screens`), the total pool of uploaded `ads`, and overall impressions across the network.
- **Advertiser Dashboard**: Allows individual advertisers to log in, review their own specifically uploaded media, and monitor the individual play analytics (impressions) generated for their campaigns.
- Both dashboards use a custom-built, modern aesthetic featuring smooth CSS gradients, custom typography (`Outfit` font), and glass/surface blending using vanilla CSS—delivering a premium, lightweight UI without bulky frameworks.

> [!TIP]  
> The dashboard UI is fully responsive! It utilizes CSS Grid and flexible variables so it works comfortably whether viewed on a desktop or an advertiser's mobile device.

### 2. Digital Signage Client (Screen Viewer)
- Built entirely with **Vanilla JavaScript** in `viewer.html`.
- It mimics a continuously running hardware loop for Smart TVs or Raspberry Pis.
- Automatically handles token verification, heartbeat pings for "Online Status", fetching playlists, and auto-transitioning between images and video.
- **Micro-animations**: Includes sleek CSS hardware loading spinners and crossfade opacities between playing media.

### 3. API Layer
- Implemented via `Django REST Framework`.
- **`GET /api/screens/playlist/`**: Supplies screens with active, approved ads assigned specifically to their unique pairing tokens.
- **`POST /api/screens/ping/`**: Keep-alive heartbeat that updates the central dashboard with live status ("ONLINE").
- **`POST /api/screens/analytics/`**: Registers the exact timestamp when a screen effectively finishes rendering/playing an ad.

## Verification & Usage

The application successfully boots up and passes all Django internal checks.

You can now start a local testing server using the following command:
```bash
.\venv\Scripts\Activate
python manage.py runserver
```

> [!NOTE]  
> Before logging in, you'll want to initialize superuser credentials so you can access the admin panels to provision initial users or screens:
> `python manage.py createsuperuser`

To connect a dummy TV client locally, simply open a browser and navigate to:
`http://localhost:8000/screen/viewer/?token=<your_assigned_uuid_here>`
