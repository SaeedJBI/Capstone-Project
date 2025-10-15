from django.contrib.auth.models import User
from .models import TechTrack, TechSkill, TechCodemon, QuizQuestion

def load_data():
    print("🗑️  Clearing existing data...")
    
    # Clear existing data (optional - be careful in production!)
    TechTrack.objects.all().delete()
    TechSkill.objects.all().delete() 
    TechCodemon.objects.all().delete()
    QuizQuestion.objects.all().delete()
    
    print("📚 Creating tech tracks...")
    
    # Create Tech Tracks
    web_track = TechTrack.objects.create(
        name="Web Development",
        description="Frontend and backend web technologies",
        color="#3498db"
    )
    
    data_track = TechTrack.objects.create(
        name="Data Science", 
        description="Data analysis, machine learning, and statistics",
        color="#e74c3c"
    )
    
    security_track = TechTrack.objects.create(
        name="Cybersecurity",
        description="Network security, encryption, and ethical hacking", 
        color="#2ecc71"
    )
    
    devops_track = TechTrack.objects.create(
        name="DevOps",
        description="Infrastructure, automation, and deployment",
        color="#f39c12"
    )
    
    print("🛠️ Creating tech skills...")
    
    # Create Tech Skills
    html_skill = TechSkill.objects.create(name="HTML", description="HyperText Markup Language")
    css_skill = TechSkill.objects.create(name="CSS", description="Cascading Style Sheets")
    js_skill = TechSkill.objects.create(name="JavaScript", description="Web interactivity programming")
    python_skill = TechSkill.objects.create(name="Python", description="General-purpose programming")
    react_skill = TechSkill.objects.create(name="React", description="JavaScript UI library")
    sql_skill = TechSkill.objects.create(name="SQL", description="Database query language")
    git_skill = TechSkill.objects.create(name="Git", description="Version control system")
    docker_skill = TechSkill.objects.create(name="Docker", description="Containerization platform")
    
    print("🐉 Creating Codemon...")
    
    # Create Web Development Codemon
    htmlizard = TechCodemon.objects.create(
        name="HTMLizard",
        image_url="",
        difficulty="B",
        tech_track=web_track
    )
    htmlizard.skills.add(html_skill, css_skill)
    
    cssaur = TechCodemon.objects.create(
        name="CSSaur", 
        image_url="",
        difficulty="B",
        tech_track=web_track
    )
    cssaur.skills.add(css_skill, js_skill)
    
    javascriptops = TechCodemon.objects.create(
        name="JavaScriptops",
        image_url="", 
        difficulty="I",
        tech_track=web_track
    )
    javascriptops.skills.add(js_skill, react_skill)
    
    # Create Data Science Codemon
    pythorch = TechCodemon.objects.create(
        name="Pythorch",
        image_url="",
        difficulty="I", 
        tech_track=data_track
    )
    pythorch.skills.add(python_skill, sql_skill)
    
    # Create DevOps Codemon  
    dockerchu = TechCodemon.objects.create(
        name="Dockerchu",
        image_url="",
        difficulty="A",
        tech_track=devops_track
    )
    dockerchu.skills.add(docker_skill, git_skill)

    print("👤 Creating demo users...")
    
    # Create demo users
    user1 = User.objects.create_user(
        username="coder_alex",
        email="alex@example.com", 
        password="testpass123"
    )
    
    user2 = User.objects.create_user(
        username="dev_sam",
        email="sam@example.com",
        password="testpass123" 
    )
    
    user3 = User.objects.create_user(
        username="tech_taylor",
        email="taylor@example.com", 
        password="testpass123"
    )

    print("🎮 Creating user collections and progress...")
    
    # Give users some rolls and collections
    alex_profile = user1.userprofile
    alex_profile.available_rolls = 5
    alex_profile.save()
    
    sam_profile = user2.userprofile  
    sam_profile.available_rolls = 3
    sam_profile.save()
    
    taylor_profile = user3.userprofile
    taylor_profile.available_rolls = 0  # No rolls left
    taylor_profile.save()

    print("📦 Adding Codemon to user collections...")
    
    # Alex has captured HTMLizard and CSSaur
    from codemon_app.models import UserCodemonCollection
    from django.utils import timezone
    
    # Alex's collection
    UserCodemonCollection.objects.create(
        user=,
        codemon=htmlizard,
        capture_score=85,
        captured_date=timezone.now()
    )
    
    UserCodemonCollection.objects.create(
        user=user1, 
        codemon=cssaur,
        capture_score=90,
        captured_date=timezone.now()
    )
    
    # Sam has captured JavaScriptops
    UserCodemonCollection.objects.create(
        user=user2,
        codemon=javascriptops, 
        capture_score=80,
        captured_date=timezone.now()
    )
    
    # Taylor has no Codemon (0 rolls)



    
    print("❓ Creating quiz questions...")
    
    # Create Quiz Questions
    # HTML Questions
    QuizQuestion.objects.create(
        question_text="What does HTML stand for?",
        correct_answer="HyperText Markup Language",
        wrong_answer1="HighText Machine Language",
        wrong_answer2="HyperTool Multi Language", 
        wrong_answer3="Home Tool Markup Language",
        difficulty="B"
    ).skills.add(html_skill)
    
    QuizQuestion.objects.create(
        question_text="Which HTML tag is used for the largest heading?",
        correct_answer="<h1>",
        wrong_answer1="<heading>",
        wrong_answer2="<h6>",
        wrong_answer3="<head>", 
        difficulty="B"
    ).skills.add(html_skill)
    
    # CSS Questions
    QuizQuestion.objects.create(
        question_text="Which CSS property is used to change the background color?",
        correct_answer="background-color", 
        wrong_answer1="color",
        wrong_answer2="bgcolor",
        wrong_answer3="background",
        difficulty="B"
    ).skills.add(css_skill)
    
    QuizQuestion.objects.create(
        question_text="Which CSS property controls the text size?",
        correct_answer="font-size",
        wrong_answer1="text-style",
        wrong_answer2="text-size", 
        wrong_answer3="font-style",
        difficulty="B"
    ).skills.add(css_skill)
    
    # JavaScript Questions
    QuizQuestion.objects.create(
        question_text="How do you create a function in JavaScript?",
        correct_answer="function myFunction()",
        wrong_answer1="function:myFunction()", 
        wrong_answer2="def myFunction()",
        wrong_answer3="function = myFunction()",
        difficulty="B"
    ).skills.add(js_skill)
    
    QuizQuestion.objects.create(
        question_text="Which operator is used to assign a value to a variable?",
        correct_answer="=",
        wrong_answer1="*", 
        wrong_answer2="-",
        wrong_answer3="x",
        difficulty="B"
    ).skills.add(js_skill)
    
    # Python Questions
    QuizQuestion.objects.create(
        question_text="Which collection is ordered, changeable, and allows duplicate members?",
        correct_answer="List",
        wrong_answer1="Tuple",
        wrong_answer2="Set", 
        wrong_answer3="Dictionary",
        difficulty="B"
    ).skills.add(python_skill)
    
    QuizQuestion.objects.create(
        question_text="How do you start a comment in Python?",
        correct_answer="#",
        wrong_answer1="//", 
        wrong_answer2="/*",
        wrong_answer3="--",
        difficulty="B"
    ).skills.add(python_skill)
    
    print("✅ Dummy data loaded successfully!")
    print("📊 Created:")
    print(f"   - {User.objects.filter(is_superuser=False).count()} demo users")
    print(f"   - {TechTrack.objects.count()} tech tracks")
    print(f"   - {TechSkill.objects.count()} tech skills") 
    print(f"   - {TechCodemon.objects.count()} Codemon")
    print(f"   - {QuizQuestion.objects.count()} quiz questions")
    print("\n🔑 Demo user logins:")
    print("   - coder_alex / testpass123 (5 rolls)")
    print("   - dev_sam / testpass123 (3 rolls)") 
    print("   - tech_taylor / testpass123 (0 rolls)")