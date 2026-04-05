# AdStreamer User Manual

Welcome to the **AdStreamer Digital Signage Management System**. This platform enables centrally managed, dynamic content distribution to an unlimited array of screens (Smart TVs, Mobile Devices, Raspberry Pis) over the internet. 

This guide provides instructions for both System Administrators and Advertisers to operate the dashboard effectively.

---

## 1. Roles & Access
The platform separates functionalities into two secure roles:
- **System Administrator (ADMIN)**: Has absolute control over the platform. Admins can register users, provision new screens, approve/reject ad content, and command the scheduling of what plays on which screen.
- **Advertiser (ADVERTISER)**: A limited user who can log in to view the performance (analytics/impressions) of their specific ad campaigns.

---

## 2. Managing Users (Admins Only)
Before an advertiser can use the system, the Administrator must create an account for them.

1. Navigate to the **Users** tab on the left sidebar under *Management*.
2. Fill out the `Username`, `Password`, and ensure you select the correct `Role` (e.g., ADVERTISER).
3. Click **Register Account**.
4. The user is now registered and will appear in the "System Users" table below. They can now log in using `http://YOUR_SERVER_IP/`.

---

## 3. Provisioning Hardware Screens (Admins Only)
Before connecting a physical display (like a TV in a lobby), you must register it in the system.

1. Navigate to the **Screens** tab on the left sidebar.
2. In the "Provision New Screen" form, provide a memorable `Name` (e.g., *Main Lobby TV*) and `Location` (e.g., *1st Floor*).
3. Click **Register Screen**.
4. Important: Note the auto-generated **Pairing Token (UUID)** that appears in the table. You will use this securely unique code to link the hardware TV to the server.

---

## 4. Setting up a Smart TV / Display Player
Once a screen is provisioned, you need to point your actual hardware device (Smart TV browser, Raspberry Pi, etc.) to the AdStreamer server.

1. Open the web browser on your physical Display Screen pointing to:
   `http://YOUR_SERVER_IP/screen/viewer/?token=YOUR_PAIRING_TOKEN_UUID_HERE`
2. Example: `http://192.168.1.50/screen/viewer/?token=a1b2c3d4-e5f6-7890...`
3. Hit Enter. Ensure the Display is configured to remain fullscreen and never sleep.
4. The screen will automatically sync with the server, begin pinging, and download/play assigned ads on a continuous loop. On your Admin Dashboard, the screen's status will automatically change to **ONLINE**.

---

## 5. Ad Approvals & Library (Admins Only)
Advertisers provide media content (Ads). Before an Ad plays globally, an Admin must approve it.

1. Navigate to the **Ads** tab on the left sidebar.
2. Review the list of uploaded media. 
3. For each active Ad, you can use the drop-down to change the status to **APPROVED**, **REJECTED**, or **PENDING**. 
4. Click **Update Approvals** to save the changes.
5. *Note: Only ads with the `APPROVED` status and the `Active` checkbox checked will be dispatched to screens.*

---

## 6. Scheduling Ads to Screens (Assignments)
Ads do not play randomly. You must intentionally bridge an Ad to a specific Screen and set viewing parameters.

1. Navigate to the **Assignments** tab on the left sidebar.
2. In the "Assign Ad to Screen" form:
   - Select the target **Screen**.
   - Select the specific **Ad**.
   - Set exactly when the Ad begins playing (`Start Date`) and when it expires (`End Date`).
   - Assign a **Display Order** (e.g., if you assign two ads to a screen, the lower number plays first).
3. Click **Create Assignment**.

The moment this assignment is created, the connected distant screen will instantly pull the new schedule via its automated network heartbeat and adjust its live playback routine!

---

## 7. The Advertiser Experience
When Advertisers log in, they bypass all heavy management controls and are greeted with a sleek, read-only analytics portal:

- **My Ads**: A rundown of every ad they have running in the system.
- **Total Impressions**: A live counter capturing every exact moment their Ad successfully finished rendering on a screen.
- **Approval Tracking**: Advertisers can track whether their uploaded content is currently being reviewed, was rejected, or is actively approved and running.
