<div align="center">

<img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="SnapClass Logo" width="100"/>

# SnapClass

### Multimodal AI-Powered Attendance System

**Automated classroom attendance through face recognition and voice verification.**  
No roll calls. No sign-in sheets. Just a photo.

<br/>

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

</div>

---

## Overview

SnapClass is a biometric attendance platform designed for educational institutions. It eliminates the manual overhead of attendance tracking by leveraging two independent AI modalities simultaneously:

- **Face Recognition** — identifies students present in a classroom photograph
- **Voice Verification** — confirms identity via speaker embeddings, not speech-to-text

Using both modalities in tandem makes the system significantly more robust against spoofing compared to single-factor approaches, while keeping the experience effortless for both teachers and students.

---

## Features

| Feature | Description |
|---|---|
| 📷 Snap-Based Attendance | Upload a class photo — AI identifies and marks present students automatically |
| 🎙️ Voice Verification | Speaker recognition using d-vector embeddings — language-agnostic |
| 👨‍🏫 Teacher Dashboard | Create classes, run attendance, view history, export reports |
| 🎓 Student Portal | Enroll biometrics, track personal attendance across all enrolled classes |
| 🔗 QR Code Enrollment | Students join classes by scanning a QR code or following a link |
| 🔐 Secure Authentication | Passwords hashed with `bcrypt`; biometric data stored as numerical vectors |
| ☁️ Cloud Backend | Powered by Supabase — no self-hosted infrastructure required |

---

## System Architecture

```
app.py                              # Application entry point & session routing
└── src/
    └── screens/
        ├── home_screen.py          # Landing page & authentication
        ├── teacher_screen.py       # Teacher dashboard & controls
        ├── student_screen.py       # Student attendance portal
        └── components/
            └── dialog_auto_enroll.py   # QR join-code deep-link handler
```

Navigation is managed through `st.session_state['login_type']`, which routes users to the appropriate screen based on their role (`"teacher"`, `"student"`, or `None` for the home screen). Deep-link enrollment is supported via the `?join-code=` URL query parameter.

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | `streamlit` | Web UI and session management |
| Face Recognition | `face-recognition`, `dlib-bin`, `scikit-learn` | Face encoding and classification |
| Voice Recognition | `resemblyzer`, `librosa` | Speaker embedding and verification |
| Database & Storage | `supabase` | Cloud PostgreSQL + file storage |
| Authentication | `bcrypt` | Secure password hashing |
| QR Codes | `segno` | Class join-code generation |
| Utilities | `numpy`, `pandas`, `pillow` | Data handling and image processing |

> **Note on `resemblyzer`:** Rather than transcribing speech, `resemblyzer` produces a compact numerical fingerprint of a speaker's voice (a d-vector embedding). This means the system identifies *who* is speaking regardless of *what* they say — enrollment and verification work in any language.

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Supabase](https://supabase.com) project (free tier is sufficient)
- A webcam or uploaded images as the photo source

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Kushagra-2112/SnapClass-Multimodal-AI-Attendance.git
cd SnapClass-Multimodal-AI-Attendance

# 2. (Recommended) Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

> `dlib-bin` ships pre-compiled binaries to avoid building dlib from source. On Linux, ensure `cmake` and `libopenblas-dev` are installed if you encounter issues.

### Environment Configuration

Create a `.env` file in the project root with your Supabase credentials:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your_supabase_anon_key
```

### Running the Application

```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501`.

---

## Database Schema

The following tables are required in your Supabase project:

| Table | Description |
|---|---|
| `users` | Teacher and student accounts with hashed passwords and roles |
| `classes` | Class metadata, teacher association, and join codes |
| `enrollments` | Many-to-many relationship between students and classes |
| `face_encodings` | 128-dimensional face vectors per enrolled student |
| `voice_embeddings` | 256-dimensional d-vector embeddings per enrolled student |
| `attendance` | Per-session attendance records with timestamps |

---

## Usage

### Teachers

1. Sign up and log in as a **Teacher**
2. Create a class — a unique QR code and join link are generated automatically
3. Share the QR code or join link with your students
4. At the start of class, upload a photo of the room
5. SnapClass identifies students and marks attendance; review and export records from the dashboard

### Students

1. Sign up and log in as a **Student**
2. Scan the class QR code or follow the join link to enroll
3. Complete biometric setup — upload a clear face photo and record a short voice sample
4. Attendance is marked automatically each session once the teacher runs recognition

---

## Security

- Passwords are never stored in plain text — all credentials are hashed with `bcrypt` prior to storage
- Biometric data is stored as compact numerical vectors, not as raw images or audio files
- QR join codes are scoped per class and can be regenerated by the teacher at any time
- Supabase Row Level Security (RLS) policies are recommended to restrict data access by user role

---

## Roadmap

- [ ] Liveness detection to prevent photo-based spoofing
- [ ] Attendance export to CSV and Excel formats
- [ ] Low-attendance alerts via email or SMS
- [ ] Institution-level admin panel with multi-class analytics
- [ ] Progressive Web App (PWA) support for mobile devices
- [ ] Pinned dependency versions for reproducible builds

---

## Contributing

Contributions are welcome. To propose a significant change, please open an issue first to discuss the approach. For smaller fixes, a pull request is sufficient.

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add your feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

---

<div align="center">

Built by [Kushagra](https://github.com/Kushagra-2112)

</div>
