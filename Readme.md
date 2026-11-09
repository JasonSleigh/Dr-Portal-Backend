# DRPortal Database Schema

## Users

### Purpose

Authentication and account management.

### Table: users

| Field | Type | Required | Constraints | Description |
|---------|---------|---------|---------|---------|
| id | UUID | ✅ | PK | Unique user identifier |
| email | VARCHAR(255) | ✅ | UNIQUE | Login email address |
| password_hash | VARCHAR(255) | ✅ | | Secure password hash |
| is_verified | BOOLEAN | ✅ | DEFAULT FALSE | Doctor verification status |
| is_active | BOOLEAN | ✅ | DEFAULT TRUE | Account active status |
| created_at | TIMESTAMP | ✅ | | Account creation timestamp |
| last_login | TIMESTAMP | ❌ | | Last successful login |

---

## Doctor Profiles

### Purpose

Stores professional doctor information.

### Table: doctor_profiles

| Field | Type | Required | Constraints | Description |
|---------|---------|---------|---------|---------|
| id | UUID | ✅ | PK | Profile identifier |
| user_id | UUID | ✅ | FK users.id | Associated user |
| first_name | VARCHAR(100) | ✅ | | Doctor first name |
| last_name | VARCHAR(100) | ✅ | | Doctor surname |
| registration_number | VARCHAR(50) | ✅ | UNIQUE | Medical registration number |
| specialty_id | UUID | ✅ | FK specialties.id | Medical specialty |
| practice_id | UUID | ✅ | FK practices.id | Associated practice |
| country | VARCHAR(50) | ✅ | | Country |
| city | VARCHAR(100) | ✅ | | City |
| phone | VARCHAR(50) | ❌ | | Contact number |
| bio | TEXT | ❌ | | Professional biography |
| profile_photo_url | VARCHAR(500) | ❌ | | Profile image |
| accepting_referrals | BOOLEAN | ✅ | | Open to referrals |
| accepting_urgent_referrals | BOOLEAN | ✅ | | Open to urgent referrals |
| average_response_minutes | INTEGER | ❌ | | Average response time |
| verified_at | TIMESTAMP | ❌ | | Verification date |
| created_at | TIMESTAMP | ✅ | | Record creation timestamp |

---

## Relationships

| Parent Table | Child Table | Relationship |
|--------------|------------|---------------|
| users | doctor_profiles | One-to-One |
| specialties | doctor_profiles | One-to-Many |
| practices | doctor_profiles | One-to-Many |

---

## TODO

### Users

- [ ] Create SQLAlchemy model
- [ ] Create Alembic migration
- [ ] Create CRUD service
- [ ] Create authentication endpoints
- [ ] Implement password hashing
- [ ] Implement JWT authentication

### Doctor Profiles

- [ ] Create SQLAlchemy model
- [ ] Create Alembic migration
- [ ] Create CRUD endpoints
- [ ] Implement profile update endpoint
- [ ] Implement doctor search
- [ ] Implement doctor verification workflow