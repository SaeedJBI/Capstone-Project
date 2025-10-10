# CodeMon - Learn Tech Skills, Collect Pokemon!

A mobile-first, gamified learning platform where users master tech concepts by "battling" Pokemon through AI-generated quizzes. Prove your knowledge to capture Pokemon and build your tech collection!

## 🎯 The Concept
**Battle → Capture → Collect!** 

- **Battle**: Face Pokemon in skill-based quiz battles
- **Capture**: Prove your knowledge to add Pokemon to your collection  
- **Collect**: Build your tech Pokemon portfolio across learning tracks

## 🚀 Live Demo
[Deployed Link Will Be Here]

## 📋 Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Learning Tracks](#learning-tracks)
- [Game Mechanics](#game-mechanics)
- [Project Structure](#project-structure)
- [Development Phases](#development-phases)

## ✨ Features

### 🎮 Core Gameplay
- **Track-Based Enrollment** - Choose learning paths (Web Dev, Cybersecurity, etc.)
- **Skill-Based Encounters** - Each Pokemon represents specific tech skills
- **AI-Generated Quizzes** - Dynamic quizzes based on Pokemon skills
- **Prove-to-Capture** - Score 80%+ in battles to collect Pokemon
- **Roll Economy** - Earn rolls through learning activities

### 📚 Learning System
- **Multiple Tech Tracks**: Web Dev, Data Science, Cybersecurity, DevOps
- **Personalized Quizzes**: AI-generated based on encountered Pokemon skills
- **Progressive Difficulty**: Beginner → Intermediate → Advanced Pokemon
- **Track Progression**: Unlock new tracks as you advance

### 📱 Mobile-First Design
- **Responsive** - Works seamlessly on all devices
- **Touch-Optimized** - Designed for mobile interaction

## 🛠 Technologies

### Backend
- **Python** 🐍 + **Django**
- **PostgreSQL** database
- **AI Integration** for dynamic quiz generation

### Frontend
- **HTML5**, **CSS3**, **JavaScript**
- **Django Templates**
- **Mobile-first** CSS architecture

## 🎯 Learning Tracks

### 🔵 Web Development
- HTML/CSS Fundamentals
- JavaScript & DOM Manipulation  
- React/Vue.js Concepts
- Django Framework

### 🔴 Cybersecurity
- Network Security Basics
- Cryptography Concepts
- Security Best Practices
- Ethical Hacking Principles

### 🟢 Data Science
- Python Basics
- Pandas & Data Analysis
- Machine Learning Concepts
- SQL & Database Fundamentals

### 🟠 DevOps
- Linux Basics
- Containerization (Docker)
- CI/CD Pipelines
- Cloud Infrastructure

## 🎮 Game Mechanics

### User Journey:
1. **Sign Up & Choose Track** → Select your learning path
2. **Earn Rolls** → Daily logins, content completion, achievements
3. **Encounter Pokemon** → Use rolls to find Pokemon from your enrolled tracks
4. **Battle Quiz** → AI generates quiz based on Pokemon's skills
5. **Capture** → Score 80%+ to add Pokemon to your collection
6. **Progress** → Unlock new tracks and encounter harder Pokemon

### Example Pokemon:
- **HTMLizard** (Web Dev) - Skills: "HTML5, Semantic Tags, Forms"
- **Cryptorby** (Cybersecurity) - Skills: "Encryption, Hashing, SSL"
- **Pythorch** (Data Science) - Skills: "Python, Pandas, Data Analysis"
- **Dockerchu** (DevOps) - Skills: "Containers, Docker, Orchestration"

## 🗃️ Database Schema

![CodeMon ERD Schema](media/erd-schema.png)

### Core Tables:
- **users** - User accounts and roll balances
- **tech_tracks** - Learning categories (Web Dev, Security, etc.)
- **tech_pokemon** - Collectible Pokemon with skills and difficulty  
- **user_pokemon_collection** - Captured Pokemon with battle history
- **user_track_progress** - Tracks user enrollment and progress per track

### Relationships:
- Users enroll in Tech Tracks (many-to-many via user_track_progress)
- Pokemon belong to Tech Tracks (one-to-many)
- Users collect Pokemon (many-to-many via user_pokemon_collection)

## 🚀 Quick Start
### Prerequisites
- Python 3.8+
- PostgreSQL
- Django 4.2+

### Installation
```bash
# Clone the Capstone Project repository
git clone https://github.com/SaeedJBI/Capstone-Project.git
cd Capstone-Project

# Navigate to the CodeMon Django project
cd codemon

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up database
createdb codemon

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver


git commit -m "Simplifying ERD schema , README updated"