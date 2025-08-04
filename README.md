
# RVM Deposit Logging & Reward Engine API

### Feature
- User registration/login with JWT
- Record deposits with material type, weight, and machine ID
- Reward points auto-calculated via reward engine
- Admin can update reward rules
- Async processing with Celery


### Setup Instructions
2. `python manage.py migrate`
3. Create a superuser
4. Run: `celery -A rvm_project worker --loglevel=info`
5. Run dev server: `python manage.py runserver`

### API Endpoints
- `POST /register/` — Register new user
- `POST /login/` — Login and receive JWT
- `POST /deposit/` — Submit deposit (auth required)
- `GET /summary/` — View user stats (auth required)
- `GET/POST /admin/reward-rules/` — Admin interface to view/update reward rules

### Architectural Decisions
- Separate reward logic in `reward_engine.py`
- Async background job with Celery to offload scoring
- Clean permission separation (user vs. admin)