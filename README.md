# inblog — Personal Blog & Coding Solutions Platform

**inblog** is a personal portfolio, blog, and algorithmic coding solutions platform built with Django for software engineer **Islom Nurmukhammadov**. It provides a centralized web application for publishing technical articles, sharing problem-solving code snippets with explanations, and managing personal profile links.

## Key Features

- **Home & Portfolio Card:** Displays the author's profile photo, title (`Software Engineer`), social links (Telegram, GitHub, LinkedIn), and quick navigation buttons to the Blog and About Me sections.
- **Blog Section:** Lists all published articles with publication dates (automatically truncating titles longer than 45 characters in the list view) and renders individual posts with HTML formatting support (`|safe` template filter).
- **Coding Solutions Section:** Showcases algorithmic and programming problems with a problem description, a macOS-styled code window (`solution.py`), explanatory notes, and the publication date.
- **About Me Page:** Renders an editable biography section managed directly from the Django admin interface with HTML tag support.
- **Singleton Model Architecture:** Both social media links (`LinksModel`) and the biography text (`AboutMeModel`) inherit from a custom abstract `SingleModel` class, enforcing a single database record (`pk=1`) that is automatically retrieved or initialized via `.load()`.
- **Customized Admin Panel:** The management dashboard is mapped to `/boshqaruv/` instead of the default `/admin/` path, and `SingleAdminModel` prevents creating duplicate records or deleting existing singleton entries.
- **Responsive Design:** Dedicated desktop and mobile stylesheets (`static/style/` and `static/style/mobile/`) paired with CSS animations (`animations.css`) ensure proper rendering across screen sizes.

## Tech Stack

| Layer | Technology / Tool | Description |
| :--- | :--- | :--- |
| **Backend** | Python `3.14`, Django `5.2.18` | Class-Based Views (`TemplateView`, `ListView`, `DetailView`) and Django ORM |
| **Database** | SQLite3 (`db.sqlite3`) | File-based relational database for local development |
| **Frontend** | HTML5 (Django Templates), CSS3 | Template inheritance (`base.html`), custom desktop/mobile CSS, and animations |
| **Icons** | Font Awesome `6.5.2` (CDN) | Social media and UI icons |
| **Environment** | Pipenv (`Pipfile`, `Pipfile.lock`) | Virtual environment and dependency management (`django`, `asgiref`, `sqlparse`) |

## Project Structure

- `config/` — Project-level configuration (`settings.py`), root URL routing (`urls.py`), and WSGI/ASGI entry points.
- `blog/` — Core application:
  - `models.py` — Database models (`BlogModel`, `SolutionModel`, abstract `SingleModel`, `LinksModel`, and `AboutMeModel`).
  - `views.py` — Class-Based Views (`homeView`, `aboutView`, `blogView`, `oneBlogPostView`, `solutionsView`, `oneSolutionPostView`).
  - `urls.py` — Application URL routes.
  - `admin.py` — Model registrations and `SingleAdminModel` permission rules.
  - `tests.py` — Automated unit tests verifying HTTP status codes, templates, and singleton behavior.
  - `migrations/` — Database schema migrations (`0001`–`0007`).
- `templates/` — HTML templates (`base.html`, `home.html`, `about.html`, `blog.html`, `blogpost.html`, `solutions.html`, `solutionpost.html`).
- `static/` — Static assets:
  - `img/base.jpeg` — Profile image displayed on the home page.
  - `style/` — Desktop CSS files and `mobile/` responsive stylesheets.
- `manage.py` — Django command-line utility.
- `Pipfile` & `Pipfile.lock` — Dependency definitions and exact version locks.

## Database Models

| Model | Type | Fields | Purpose |
| :--- | :--- | :--- | :--- |
| `BlogModel` | Standard | `title` (`CharField`, 200), `text` (`TextField`, 5000), `time` (`DateField`, auto) | Stores blog articles and publication dates |
| `SolutionModel` | Standard | `title` (`CharField`, 200), `question` (`TextField`, 5000), `code` (`TextField`), `comment` (`TextField`, 500), `time` (`DateField`, auto) | Stores problem statements, Python code solutions, and explanations |
| `LinksModel` | Singleton (`pk=1`) | `telegram` (`CharField`, 100), `github` (`CharField`, 100), `linkedin` (`CharField`, 100) | Stores social profile URLs displayed on the home page |
| `AboutMeModel` | Singleton (`pk=1`) | `text` (`TextField`, 5000) | Stores content for the About Me page |

## URL Routes

| Path | URL Name (`name`) | View Class | Template | Description |
| :--- | :--- | :--- | :--- | :--- |
| `/` | `home` | `homeView` | `home.html` | Home page with profile card and social links |
| `/about/` | `about` | `aboutView` | `about.html` | Author biography page |
| `/blog/` | `blog` | `blogView` | `blog.html` | List of all blog posts |
| `/blog/<int:pk>/` | `post` | `oneBlogPostView` | `blogpost.html` | Detailed view of a single blog post |
| `/solutions/` | `solutions` | `solutionsView` | `solutions.html` | List of all coding solutions |
| `/solutions/<int:pk>/` | `solution` | `oneSolutionPostView` | `solutionpost.html` | Detailed view of a problem, code snippet, and commentary |
| `/boshqaruv/` | — | `admin.site.urls` | Django Admin | Administration dashboard |

## Installation & Setup

### 1. Prerequisites

- **Python** `3.14` (or Python `3.10+` compatible with Django `5.2.x`)
- **Pipenv** (or standard `venv` and `pip`)

### 2. Setup with Pipenv (Recommended)

Navigate to the project directory, install dependencies, and activate the virtual environment:

```bash
cd inblog
pipenv install
pipenv shell
```

### 3. Setup with Standard `venv` (Alternative)

If you prefer not to use Pipenv, create and activate a standard virtual environment:

```bash
cd inblog
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install django==5.2.18
```

### 4. Database Migrations & Superuser Creation

Apply database migrations and create an administrator account:

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Once the server is running, access the application in your browser:
- **Main Website:** `http://127.0.0.1:8000/`
- **Admin Dashboard:** `http://127.0.0.1:8000/boshqaruv/`

After logging into `/boshqaruv/`, configure your Telegram, GitHub, and LinkedIn URLs under **Links models** and add your bio under **About me models**.

## Running Tests

The repository includes unit tests (`blog/tests.py`) that verify the home page status code (`200 OK`), template inheritance (`home.html` and `base.html`), `SingleModel` uniqueness enforcement, and social link rendering. Run the test suite with:

```bash
python manage.py test
```

## Production Deployment Checklist

The project is currently configured for local development. Before deploying to a production environment, update `config/settings.py`:

1. **Secret Key (`SECRET_KEY`):** Move the hardcoded `SECRET_KEY` to an environment variable (`.env`).
2. **Debug Mode (`DEBUG`):** Set `DEBUG = False`.
3. **Allowed Hosts (`ALLOWED_HOSTS`):** Replace `ALLOWED_HOSTS = ['*']` with your explicit domain names.
4. **Static Files (`STATIC_ROOT`):** Configure `STATIC_ROOT` so `python manage.py collectstatic` can gather static files for your web server.
5. **HTML Sanitization:** Because `about.html`, `blogpost.html`, and `solutionpost.html` render content using the `|safe` filter, ensure only trusted administrators have access to `/boshqaruv/`.


## Author

**Islom Nurmukhammadov** — Software Engineer
- **GitHub:** [islomnurmukhammadov](https://www.google.com/search?q=https://github.com/islomnurmukhammadov)
- **Telegram:** [@islomnurmukhammadov](https://www.google.com/search?q=https://t.me/islomnurmukhammadov)
- **LinkedIn:** [Islom Nurmukhammadov](https://www.google.com/search?q=https://www.linkedin.com/in/islomnurmukhammadov/)