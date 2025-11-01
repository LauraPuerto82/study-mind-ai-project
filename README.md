# 🎓 StudyMind AI

**StudyMind AI** is an AI-powered educational platform designed to support students (ages 10–16) with personalized learning while providing parents with insights and progress tracking.

---

## 🚀 Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy 2.0** - ORM with type hints
- **Alembic** - Database migrations
- **PostgreSQL** - Relational database
- **JWT** - Token-based authentication
- **bcrypt** - Password hashing

### Frontend (Coming in Phase 1)
- **React** + **TypeScript**
- **Vite** - Build tool
- **Tailwind CSS** - Styling

### Infrastructure
- **Docker** & **Docker Compose** - Containerization
- **Uvicorn** - ASGI server

---

## 📁 Project Structure

```
study-mind-ai-project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── endpoints/
│   │   │       │   ├── auth.py          # Authentication endpoints
│   │   │       │   └── health.py        # Health check endpoints
│   │   │       └── router.py            # API router
│   │   ├── core/
│   │   │   ├── config.py                # Settings management
│   │   │   └── security.py              # JWT & password utilities
│   │   ├── database/
│   │   │   ├── base.py                  # Base model class
│   │   │   └── session.py               # Database session
│   │   ├── models/
│   │   │   └── user.py                  # User database model
│   │   ├── schemas/
│   │   │   └── user.py                  # Pydantic schemas
│   │   └── main.py                      # FastAPI app entry point
│   ├── alembic/                         # Database migrations
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env
├── frontend/                            # (Phase 1)
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Setup & Installation

### Prerequisites
- Docker Desktop installed
- Git

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd study-mind-ai-project
```

### 2. Configure environment variables

Create `.env` file in project root:

```env
POSTGRES_USER=studymind_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=studymind_db
```

Create `backend/.env` file:

```env
POSTGRES_USER=studymind_user
POSTGRES_PASSWORD=your_password
POSTGRES_DB=studymind_db
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

SECRET_KEY=your-secret-key-min-32-characters-change-in-production
```

**Generate SECRET_KEY:**
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 3. Start the application

```bash
docker-compose up --build
```

Wait for:
```
studymind_postgres  | database system is ready to accept connections
studymind_backend   | Application startup complete.
```

### 4. Run database migrations

```bash
docker-compose exec backend alembic upgrade head
```

---

## 🧪 Testing the API

### Using Swagger UI (Recommended)

Open your browser: **http://localhost:8000/docs**

### Using curl

#### Health checks
```bash
# API health
curl http://localhost:8000/api/v1/health

# Database health
curl http://localhost:8000/api/v1/health/db
```

#### Register a user
```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "securepass123"
  }'
```

#### Login
```bash
curl -X POST "http://localhost:8000/api/v1/auth/login?username=testuser&password=securepass123"
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

## 📚 Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API metadata |
| GET | `/docs` | Swagger UI documentation |
| GET | `/api/v1/health` | API health check |
| GET | `/api/v1/health/db` | Database health check |
| POST | `/api/v1/auth/register` | Register new user |
| POST | `/api/v1/auth/login` | Login and get JWT token |

---

## 🐳 Docker Commands

```bash
# Start services
docker-compose up

# Start in background
docker-compose up -d

# Rebuild images
docker-compose up --build

# Stop services
docker-compose down

# Stop and remove volumes (⚠️ deletes database data)
docker-compose down -v

# View logs
docker-compose logs -f

# View logs of specific service
docker-compose logs -f backend

# Execute command in backend container
docker-compose exec backend <command>

# Access PostgreSQL
docker-compose exec postgres psql -U studymind_user -d studymind_db
```

---

## 🗄️ Database Management

### Create a new migration

```bash
docker-compose exec backend alembic revision --autogenerate -m "description"
```

### Apply migrations

```bash
docker-compose exec backend alembic upgrade head
```

### Rollback migration

```bash
docker-compose exec backend alembic downgrade -1
```

### View migration history

```bash
docker-compose exec backend alembic history
```

### View current migration

```bash
docker-compose exec backend alembic current
```

---

## 🔐 Authentication Flow

### 1. Register
**Endpoint:** `POST /api/v1/auth/register`

**Request:**
```json
{
  "email": "user@example.com",
  "username": "john",
  "password": "securepass123"
}
```

**Response (201 Created):**
```json
{
  "id": 1,
  "email": "user@example.com",
  "username": "john",
  "is_active": true
}
```

### 2. Login
**Endpoint:** `POST /api/v1/auth/login`

**Request:**
```
?username=john&password=securepass123
```

**Response (200 OK):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### 3. Use token in requests
Include the token in the Authorization header:

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Example with curl:**
```bash
curl http://localhost:8000/api/v1/protected-endpoint \
  -H "Authorization: Bearer <your-token-here>"
```

---

## 🏗️ Development Phases

- ✅ **Phase 0**: Backend foundation (authentication, database, Docker) - **COMPLETED**
- 🔄 **Phase 1**: Frontend + First AI agent (Study Buddy)
- ⏭️ **Phase 2**: Core features (study materials, quizzes, homework helper)
- ⏭️ **Phase 3**: Advanced AI agents (tutor, exam prep)
- ⏭️ **Phase 4**: Parent dashboard (progress tracking, insights)
- ⏭️ **Phase 5**: Production deployment (CI/CD, monitoring)

---

## 🧪 Running Tests

### Manual testing with Swagger UI

1. Open http://localhost:8000/docs
2. Use the interactive interface to test endpoints
3. Click "Try it out" on any endpoint
4. Fill in parameters and execute

### Testing authentication flow

1. Register a new user via `/api/v1/auth/register`
2. Login with credentials via `/api/v1/auth/login`
3. Copy the `access_token` from the response
4. Use the token in protected endpoints

---

## 🐛 Troubleshooting

### Port already in use

```bash
# Find what's using port 8000
lsof -i :8000  # Mac/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process or change port in docker-compose.yml
```

### Docker permission denied

**Linux:**
```bash
sudo usermod -aG docker $USER
# Then logout and login again
```

### Can't connect to database

1. Check PostgreSQL container is running: `docker ps`
2. Verify `POSTGRES_HOST=postgres` in `backend/.env`
3. Check database logs: `docker logs studymind_postgres`
4. Restart containers: `docker-compose restart`

### Database connection errors

```bash
# Reset database (⚠️ deletes all data)
docker-compose down -v
docker-compose up --build
docker-compose exec backend alembic upgrade head
```

### Alembic migration errors

```bash
# View current state
docker-compose exec backend alembic current

# View history
docker-compose exec backend alembic history

# If stuck, reset migrations (⚠️ deletes data)
docker-compose down -v
docker-compose up --build
docker-compose exec backend alembic upgrade head
```

---

## 🔧 Development Workflow

### Making changes to the code

1. Edit files in your IDE
2. Changes are reflected immediately (hot reload enabled)
3. Check logs: `docker-compose logs -f backend`

### Adding a new database field

1. Edit the model in `backend/app/models/`
2. Generate migration:
   ```bash
   docker-compose exec backend alembic revision --autogenerate -m "add field X"
   ```
3. Review the generated migration in `backend/alembic/versions/`
4. Apply migration:
   ```bash
   docker-compose exec backend alembic upgrade head
   ```

### Adding a new endpoint

1. Create/edit endpoint in `backend/app/api/v1/endpoints/`
2. Add router to `backend/app/api/v1/router.py` if needed
3. Test in Swagger UI: http://localhost:8000/docs

---

## 📖 API Documentation

### Automatic documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Key features

- Interactive API testing
- Request/response schemas
- Authentication examples
- Organized by tags (health, authentication, etc.)

---

## 🔒 Security Features

### Password Security
- Passwords hashed with **bcrypt** (never stored in plain text)
- Configurable hash rounds (default: 12)
- Automatic salt generation

### JWT Tokens
- Token-based authentication (stateless)
- Configurable expiration (default: 30 minutes)
- Secure signing with HS256 algorithm
- No sensitive data in token payload

### Environment Variables
- Secrets stored in `.env` files (not in code)
- `.env` excluded from Git (via `.gitignore`)
- `.env.example` provided as template

### Database
- Parameterized queries (SQLAlchemy ORM)
- Protection against SQL injection
- Connection pooling

---

## 📊 Database Schema

### Users Table

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    username VARCHAR UNIQUE NOT NULL,
    hashed_password VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE UNIQUE INDEX ix_users_email ON users(email);
CREATE UNIQUE INDEX ix_users_username ON users(username);
```

---

## 🤝 Contributing

This is a portfolio project. Feedback and suggestions are welcome!

### How to contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📄 License

MIT License - feel free to use this project for learning purposes.

---

## 👩‍💻 Author

**Laura Puerto**
[LinkedIn](https://www.linkedin.com/in/laura-puerto82) • [Portfolio](https://laura-puerto-portfolio.vercel.app/) • [GitHub](https://github.com/LauraPuerto82)  

---

## 🙏 Acknowledgments

Built with modern Python best practices and production-ready patterns.

### Technologies used
- FastAPI for high-performance async API
- SQLAlchemy 2.0 for modern ORM
- Pydantic for data validation
- Alembic for database migrations
- Docker for containerization
- PostgreSQL for reliable data storage

---

## 📚 Resources

### Official Documentation
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Docker](https://docs.docker.com/)

### Useful Tools
- [jwt.io](https://jwt.io) - JWT token decoder and debugger
- [Postman](https://www.postman.com/) - API testing
- [DBeaver](https://dbeaver.io/) - Database management

---

## 🎯 Project Goals

### Educational Focus
- Personalized learning for students aged 10-16
- AI-powered study assistance
- Interactive quizzes and homework help
- Progress tracking and analytics

### Parent Features
- Real-time progress monitoring
- AI-generated insights
- Communication tools
- Performance reports

### Technical Excellence
- Clean, maintainable code
- Production-ready architecture
- Comprehensive testing
- Professional documentation

---

## 📈 Future Enhancements

### Phase 1 (In Progress)
- React frontend with TypeScript
- User authentication UI
- First AI agent (Study Buddy)
- Basic chat interface

### Phase 2
- Study material management
- Quiz generation system
- Homework helper agent
- Progress tracking

### Phase 3
- Advanced AI tutors
- Exam preparation system
- Spaced repetition learning
- Gamification features

### Phase 4
- Parent dashboard
- Real-time notifications
- AI insights and recommendations
- Performance analytics

### Phase 5
- Production deployment
- CI/CD pipeline
- Monitoring and logging
- Performance optimization

---

**Built with ❤️ for better education through AI**
