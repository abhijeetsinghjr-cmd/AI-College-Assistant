from flask import Flask, request, jsonify, session, redirect
import requests

app = Flask(__name__)
app.secret_key = "ai-college-assistant-secret-key"


@app.route("/")
def home():
    if "student" not in session:
        return redirect("/login")

    return """
<!DOCTYPE html>
<html>
<head>
    <title>AI College Assistant</title>
<!DOCTYPE html>
<html>
<head>
    <title>AI College Assistant</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }

        header {
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white;
            padding: 28px 7%;
        }

        header h1 {
            margin: 0;
            font-size: 30px;
        }

        header p {
            margin: 8px 0 0;
            opacity: 0.9;
        }

        .container {
            max-width: 1100px;
            margin: 30px auto;
            padding: 0 20px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 16px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .card h3 {
            margin-top: 0;
        }

        .number {
            font-size: 32px;
            font-weight: bold;
            color: #2563eb;
        }

        .chat-box {
            margin-top: 30px;
            background: white;
            border-radius: 18px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            overflow: hidden;
        }

        .chat-header {
            padding: 22px 25px;
            border-bottom: 1px solid #eee;
        }

        .chat-header h2 {
            margin: 0;
        }

        .chat-header p {
            color: #6b7280;
            margin-bottom: 0;
        }

        #messages {
            height: 390px;
            overflow-y: auto;
            padding: 25px;
            background: #fafbff;
        }

        .message {
            max-width: 80%;
            padding: 13px 17px;
            margin-bottom: 15px;
            border-radius: 15px;
            line-height: 1.5;
            white-space: pre-wrap;
        }

        .bot {
            background: #e9efff;
            margin-right: auto;
        }

        .user {
            background: #2563eb;
            color: white;
            margin-left: auto;
        }

        .input-area {
            display: flex;
            gap: 10px;
            padding: 18px;
            border-top: 1px solid #eee;
        }

        #question {
            flex: 1;
            padding: 15px;
            border: 1px solid #d1d5db;
            border-radius: 12px;
            font-size: 16px;
            outline: none;
        }

        #question:focus {
            border-color: #2563eb;
        }

        button {
            padding: 15px 22px;
            border: none;
            border-radius: 12px;
            background: #2563eb;
            color: white;
            font-size: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .clear-btn {
            background: #6b7280;
            margin-left: 10px;
        }

        .clear-btn:hover {
            background: #4b5563;
        }

        @media (max-width: 700px) {
            .cards {
                grid-template-columns: 1fr;
            }

            .input-area {
                flex-direction: column;
            }

            .message {
                max-width: 90%;
            }
        }
        .navigation {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 15px;
    margin-top: 25px;
}

.navigation .nav-button {
    display: block;
    padding: 14px 18px;
    background: #2563eb;
    color: white;
    text-align: center;
    text-decoration: none;
    font-weight: bold;
    border-radius: 12px;
    box-shadow: 0 5px 12px rgba(0,0,0,0.10);
    transition: 0.2s;
}

.navigation .nav-button:hover {
    background: #1d4ed8;
    transform: translateY(-2px);
}
    </style>
</head>

<body>

<header>
    <h1>🎓 AI College Assistant</h1>
    <p>Smart Student Management & AI Support System</p>
</header>

<div class="container">

    <div class="cards">
    <div class="navigation">

    <a href="/attendance" class="nav-button">
        📊 Attendance
    </a>
<a href="/attendance-calculator" class="nav-button">
    🧮 Attendance Calculator
</a>
    <a href="/assignments" class="nav-button">
        📝 Assignments
    </a>

    <a href="/timetable" class="nav-button">
        📅 Timetable
        <a href="/notices" class="nav-button">
    📢 Notices
</a>
    </a>
<a href="/study-materials" class="nav-button">
    📚 Study Materials
</a>
<a href="/profile" class="nav-button">
    👤 Student Profile
</a>
</div>

        <div class="card">
            <h3>📊 Attendance</h3>
            <div class="number">82%</div>
            <p>Current attendance</p>
        </div>

        <div class="card">
            <h3>📝 Assignments</h3>
            <div class="number">4</div>
            <p>Pending assignments</p>
        </div>

        <div class="card">
            <h3>📚 Subjects</h3>
            <div class="number">6</div>
            <p>Current subjects</p>
        </div>

    </div>


    <div class="chat-box">

        <div class="chat-header">
            <h2>🤖 AI College Chatbot</h2>
            <p>Ask questions about studies, Python, Data Science, assignments and more.</p>
        </div>

        <div id="messages">

            <div class="message bot">
                👋 Hello! I am your AI College Assistant.
                How can I help you today?
            </div>

        </div>

        <div class="input-area">

            <input
                id="question"
                type="text"
                placeholder="Ask something..."
                onkeydown="handleEnter(event)"
            >

            <button onclick="askAI()">Send 🚀</button>

            <button class="clear-btn" onclick="clearChat()">
                Clear
            </button>

        </div>

    </div>

</div>


<script>

function addMessage(text, type) {

    let messages = document.getElementById("messages");

    let message = document.createElement("div");

    message.className = "message " + type;

    message.innerText = text;

    messages.appendChild(message);

    messages.scrollTop = messages.scrollHeight;

}


async function askAI() {

    let input = document.getElementById("question");

    let question = input.value.trim();

    if (question === "") {
        return;
    }

    addMessage(question, "user");

    input.value = "";

    addMessage("Thinking... 🤖", "bot");

    try {

        let response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        let data = await response.json();

        let messages = document.getElementById("messages");

        messages.removeChild(messages.lastElementChild);

        addMessage(data.answer, "bot");

    }

    catch (error) {

        let messages = document.getElementById("messages");

        messages.removeChild(messages.lastElementChild);

        addMessage(
            "❌ Local AI is not responding. Please make sure Ollama is running.",
            "bot"
        );

    }

}


function handleEnter(event) {

    if (event.key === "Enter") {
        askAI();
    }

}


function clearChat() {

    document.getElementById("messages").innerHTML = "";

    addMessage(
        "👋 Chat cleared! How can I help you?",
        "bot"
    );

}

</script>

</body>
</html>
"""
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({
            "answer": "Please enter a question."
        })

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:latest",
                "prompt": f"""You are an AI College Assistant.

Help the student with:
- Data Science
- Python
- Machine Learning
- Big Data Analytics
- Statistics
- Assignments
- Exams
- Programming
- College studies
- Career guidance

Give simple, clear and useful answers.

Student question:
{question}
""",
                "stream": False
            },
            timeout=120
        )

        result = response.json()

        answer = result.get(
            "response",
            "Sorry, I could not generate an answer."
        )

        return jsonify({
            "answer": answer
        })

    except Exception as e:
        print("OLLAMA ERROR:", e)

        return jsonify({
            "answer": "Sorry, AI is not available right now. Please make sure Ollama is running."
        })


@app.route("/attendance")
def attendance():

    subjects = [
        {"name": "Data Science", "attendance": 88},
        {"name": "Python", "attendance": 92},
        {"name": "Machine Learning", "attendance": 79},
        {"name": "Big Data Analytics", "attendance": 84},
        {"name": "Statistics", "attendance": 76},
        {"name": "DBMS", "attendance": 81}
    ]

    return """
<!DOCTYPE html>
<html>
<head>

    <title>Attendance - AI College Assistant</title>

    <style>
.navigation {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-top: 25px;
}

.nav-button {
    display: block;
    text-align: center;
    padding: 16px;
    background: white;
    color: #2563eb;
    text-decoration: none;
    font-weight: bold;
    border-radius: 12px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.08);
}

.nav-button:hover {
    background: #2563eb;
    color: white;
}

@media (max-width: 700px) {
    .navigation {
        grid-template-columns: 1fr;
    }
}
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }

        header {
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white;
            padding: 28px 7%;
        }

        header h1 {
            margin: 0;
        }

        .container {
            max-width: 1000px;
            margin: 30px auto;
            padding: 20px;
        }

        .back {
            display: inline-block;
            margin-bottom: 20px;
            text-decoration: none;
            color: #2563eb;
            font-weight: bold;
        }

        .card {
            background: white;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 15px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }

        .subject {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .percentage {
            font-size: 24px;
            font-weight: bold;
            color: #2563eb;
        }

        .bar {
            height: 10px;
            background: #e5e7eb;
            border-radius: 10px;
            margin-top: 12px;
            overflow: hidden;
        }

        .fill {
            height: 100%;
            background: #2563eb;
            border-radius: 10px;
        }

    </style>

</head>

<body>

<header>

    <h1>📊 Attendance Management</h1>
    <p>AI College Assistant</p>

</header>

<div class="container">

    <a class="back" href="/">← Back to Dashboard</a>

    <h2>Subject-wise Attendance</h2>

    {%SUBJECTS%}

</div>

</body>
</html>
""".replace(
    "{%SUBJECTS%}",
    "".join(
        f"""
        <div class="card">

            <div class="subject">

                <strong>{subject["name"]}</strong>

                <span class="percentage">
                    {subject["attendance"]}%
                </span>

            </div>

            <div class="bar">

                <div class="fill"
                     style="width: {subject["attendance"]}%">
                </div>

            </div>

        </div>
        """
        for subject in subjects
    )
)


@app.route("/assignments")
def assignments():

    assignments = [
        {
            "name": "Machine Learning Assignment",
            "subject": "Machine Learning",
            "due": "Friday",
            "status": "Pending"
        },
        {
            "name": "Python Data Analysis",
            "subject": "Python",
            "due": "Saturday",
            "status": "Pending"
        },
        {
            "name": "Big Data Project",
            "subject": "Big Data Analytics",
            "due": "Monday",
            "status": "Pending"
        },
        {
            "name": "Statistics Report",
            "subject": "Statistics",
            "due": "Completed",
            "status": "Completed"
        }
    ]

    cards = ""

    for assignment in assignments:

        if assignment["status"] == "Completed":
            status_class = "completed"
        else:
            status_class = "pending"

        cards += f"""
        <div class="card">

            <div class="top">

                <div>
                    <h3>📝 {assignment["name"]}</h3>
                    <p>📚 {assignment["subject"]}</p>
                </div>

                <span class="status {status_class}">
                    {assignment["status"]}
                </span>

            </div>

            <div class="due">
                📅 Due: {assignment["due"]}
            </div>

        </div>
        """

    return f"""
<!DOCTYPE html>
<html>

<head>

    <title>Assignments - AI College Assistant</title>

    <style>

        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }}

        header {{
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white;
            padding: 28px 7%;
        }}

        header h1 {{
            margin: 0;
        }}

        .container {{
            max-width: 1000px;
            margin: 30px auto;
            padding: 20px;
        }}

        .back {{
            display: inline-block;
            margin-bottom: 20px;
            text-decoration: none;
            color: #2563eb;
            font-weight: bold;
        }}

        .card {{
            background: white;
            padding: 22px;
            margin-bottom: 16px;
            border-radius: 16px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }}

        .top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        h3 {{
            margin: 0 0 8px 0;
        }}

        p {{
            margin: 0;
            color: #6b7280;
        }}

        .status {{
            padding: 8px 14px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 14px;
        }}

        .pending {{
            background: #fff3cd;
            color: #856404;
        }}

        .completed {{
            background: #d1fae5;
            color: #065f46;
        }}

        .due {{
            margin-top: 18px;
            color: #374151;
        }}

    </style>

</head>

<body>

<header>

    <h1>📝 Assignment Tracker</h1>
    <p>AI College Assistant</p>

</header>

<div class="container">

    <a class="back" href="/">
        ← Back to Dashboard
    </a>

    <h2>My Assignments</h2>

    {cards}

</div>

</body>

</html>
"""


@app.route("/timetable")
def timetable():

    schedule = [
        ("Monday", "9:00 AM - 10:00 AM", "Data Science", "Room 101"),
        ("Monday", "11:00 AM - 12:00 PM", "Python", "Lab 1"),
        ("Monday", "2:00 PM - 3:00 PM", "Machine Learning", "Room 203"),

        ("Tuesday", "9:00 AM - 10:00 AM", "Big Data Analytics", "Room 105"),
        ("Tuesday", "11:00 AM - 12:00 PM", "Statistics", "Room 201"),
        ("Tuesday", "2:00 PM - 3:00 PM", "DBMS", "Room 102"),

        ("Wednesday", "9:00 AM - 10:00 AM", "Python", "Lab 1"),
        ("Wednesday", "11:00 AM - 12:00 PM", "Data Science", "Room 101"),
        ("Wednesday", "2:00 PM - 3:00 PM", "Big Data Analytics", "Room 105"),

        ("Thursday", "9:00 AM - 10:00 AM", "Machine Learning", "Room 203"),
        ("Thursday", "11:00 AM - 12:00 PM", "DBMS", "Room 102"),
        ("Thursday", "2:00 PM - 3:00 PM", "Statistics", "Room 201"),

        ("Friday", "9:00 AM - 10:00 AM", "Data Science", "Room 101"),
        ("Friday", "11:00 AM - 12:00 PM", "Machine Learning", "Room 203"),
        ("Friday", "2:00 PM - 3:00 PM", "Python", "Lab 1"),

        ("Saturday", "9:00 AM - 10:00 AM", "Big Data Analytics", "Room 105"),
        ("Saturday", "11:00 AM - 12:00 PM", "DBMS", "Room 102")
    ]

    rows = ""

    for day, time, subject, room in schedule:

        rows += f"""
        <tr>
            <td><strong>{day}</strong></td>
            <td>{time}</td>
            <td>📚 {subject}</td>
            <td>🏫 {room}</td>
        </tr>
        """

    return f"""
<!DOCTYPE html>
<html>

<head>

    <title>Timetable - AI College Assistant</title>

    <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }}

        header {{
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white;
            padding: 28px 7%;
        }}

        header h1 {{
            margin: 0;
            font-size: 30px;
        }}

        header p {{
            margin-bottom: 0;
            opacity: 0.9;
        }}

        .container {{
            max-width: 1100px;
            margin: 30px auto;
            padding: 20px;
        }}

        .back {{
            display: inline-block;
            margin-bottom: 20px;
            color: #2563eb;
            text-decoration: none;
            font-weight: bold;
        }}

        .table-box {{
            background: white;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
            overflow-x: auto;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        th {{
            background: #2563eb;
            color: white;
            padding: 15px;
            text-align: left;
        }}

        td {{
            padding: 15px;
            border-bottom: 1px solid #eee;
        }}

        tr:hover {{
            background: #f8faff;
        }}

        @media (max-width: 700px) {{
            table {{
                min-width: 700px;
            }}
        }}

    </style>

</head>

<body>

<header>

    <h1>📅 Class Timetable</h1>
    <p>AI College Assistant</p>

</header>

<div class="container">

    <a class="back" href="/">
        ← Back to Dashboard
    </a>

    <h2>Weekly Timetable</h2>

    <div class="table-box">

        <table>

            <thead>

                <tr>
                    <th>Day</th>
                    <th>Time</th>
                    <th>Subject</th>
                    <th>Room</th>
                </tr>

            </thead>

            <tbody>

                {rows}

            </tbody>

        </table>

    </div>

</div>

</body>

</html>
"""


@app.route("/notices")
def notices():

    notices = [
        {
            "title": "Mid Semester Examination",
            "date": "15 September 2026",
            "type": "Exam"
        },
        {
            "title": "Machine Learning Assignment Submission",
            "date": "18 September 2026",
            "type": "Assignment"
        },
        {
            "title": "Big Data Analytics Project Submission",
            "date": "20 September 2026",
            "type": "Project"
        },
        {
            "title": "College Cultural Event",
            "date": "25 September 2026",
            "type": "Event"
        }
    ]

    cards = ""

    for notice in notices:

        cards += f"""
        <div class="notice-card">

            <div class="notice-icon">
                📢
            </div>

            <div class="notice-content">

                <h3>{notice["title"]}</h3>

                <p>📅 {notice["date"]}</p>

                <span>{notice["type"]}</span>

            </div>

        </div>
        """

    return f"""
<!DOCTYPE html>
<html>

<head>

    <title>College Notices</title>

    <style>

        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f5f7fb;
            color: #1f2937;
        }}

        header {{
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            color: white;
            padding: 28px 7%;
        }}

        header h1 {{
            margin: 0;
        }}

        .container {{
            max-width: 1000px;
            margin: 30px auto;
            padding: 20px;
        }}

        .back {{
            color: #2563eb;
            text-decoration: none;
            font-weight: bold;
        }}

        .notice-card {{
            display: flex;
            align-items: center;
            gap: 20px;
            background: white;
            padding: 22px;
            margin-top: 18px;
            border-radius: 16px;
            box-shadow: 0 5px 20px rgba(0,0,0,0.08);
        }}

        .notice-icon {{
            font-size: 35px;
        }}

        .notice-content h3 {{
            margin: 0 0 8px 0;
        }}

        .notice-content p {{
            color: #6b7280;
        }}

        .notice-content span {{
            display: inline-block;
            padding: 6px 12px;
            background: #e9efff;
            color: #2563eb;
            border-radius: 15px;
            font-size: 13px;
            font-weight: bold;
        }}

    </style>

</head>

<body>

<header>

    <h1>📢 College Notices</h1>
    <p>AI College Assistant</p>

</header>

<div class="container">

    <a class="back" href="/">
        ← Back to Dashboard
    </a>

    <h2>Latest Notices</h2>

    {cards}

</div>

</body>

</html>
"""

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

      
                    # Demo login
        if username == "student" and password == "1234":

            session["student"] = username

            return """
            <script>
                window.location.href = "/";
            </script>
            """

        else:

            return """
            <h2>❌ Invalid Login</h2>
            <p>Username or password is incorrect.</p>
            <a href="/login">Try Again</a>
            """ 
            

    return """
<!DOCTYPE html>
<html>

<head>

    <title>Student Login</title>

    <style>

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #2563eb, #4f46e5);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .login-box {
            width: 350px;
            background: white;
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        h1 {
            text-align: center;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #6b7280;
            margin-bottom: 25px;
        }

        label {
            display: block;
            margin-top: 15px;
            margin-bottom: 6px;
            font-weight: bold;
        }

        input {
            width: 100%;
            padding: 13px;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            font-size: 15px;
        }

        button {
            width: 100%;
            margin-top: 25px;
            padding: 14px;
            border: none;
            border-radius: 8px;
            background: #2563eb;
            color: white;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #1d4ed8;
        }

        .demo {
            margin-top: 20px;
            padding: 12px;
            background: #eef4ff;
            border-radius: 8px;
            font-size: 14px;
            text-align: center;
        }

    </style>

</head>

<body>

<div class="login-box">

    <h1>🎓 Student Login</h1>

    <p class="subtitle">
        AI College Assistant
    </p>

    <form method="POST">

        <label>Username</label>

        <input
            type="text"
            name="username"
            placeholder="Enter username"
            required
        >

        <label>Password</label>

        <input
            type="password"
            name="password"
            placeholder="Enter password"
            required
        >

        <button type="submit">
            Login 🚀
        </button>

    </form>

    <div class="demo">
        Demo Login<br>
        Username: <b>student</b><br>
        Password: <b>1234</b>
    </div>

</div>

</body>

</html>
"""
@app.route("/attendance-calculator")
def attendance_calculator():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Attendance Calculator</title>
        <style>
            body {
                font-family: Arial;
                background: #f4f7fb;
                padding: 40px;
            }

            .box {
                max-width: 500px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.1);
            }

            h1 {
                color: #2563eb;
            }

            input {
                width: 100%;
                padding: 12px;
                margin: 8px 0 15px;
                box-sizing: border-box;
            }

            button {
                width: 100%;
                padding: 12px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                font-size: 16px;
            }

            #result {
                margin-top: 20px;
                font-size: 18px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>

        <div class="box">
            <h1>📊 Attendance Calculator</h1>

            <label>Total Classes</label>
            <input type="number" id="total" placeholder="Example: 50">

            <label>Classes Attended</label>
            <input type="number" id="attended" placeholder="Example: 40">

            <button onclick="calculate()">Calculate Attendance</button>

            <div id="result"></div>
        </div>

        <script>
            function calculate() {
                let total = Number(document.getElementById("total").value);
                let attended = Number(document.getElementById("attended").value);

                if (total <= 0 || attended < 0 || attended > total) {
                    document.getElementById("result").innerHTML =
                        "❌ Please enter valid numbers.";
                    return;
                }

                let percentage = (attended / total) * 100;

                document.getElementById("result").innerHTML =
                    "Your Attendance: " + percentage.toFixed(2) + "%";
            }
        </script>

    </body>
    </html>
    """
@app.route("/study-materials")
def study_materials():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Study Materials</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                margin: 0;
                padding: 40px;
            }

            .container {
                max-width: 1000px;
                margin: auto;
            }

            h1 {
                color: #2563eb;
                text-align: center;
            }

            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
            }

            .grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
            }

            .card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }

            .card h2 {
                color: #2563eb;
            }

            .card p {
                color: #555;
            }

            .btn {
                display: inline-block;
                margin-top: 10px;
                padding: 10px 18px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }

            .back {
                display: block;
                text-align: center;
                margin-top: 30px;
                color: #2563eb;
                text-decoration: none;
            }
        </style>
    </head>

    <body>

        <div class="container">

            <h1>📚 Study Materials</h1>
            <p class="subtitle">
                Subject-wise learning resources for students
            </p>

            <div class="grid">

                <div class="card">
                    <h2>🐍 Python</h2>
                    <p>Learn Python programming, variables, loops, functions and OOP.</p>
                    <a class="btn" href="https://www.python.org/about/gettingstarted/" target="_blank">
                        Start Learning
                    </a>
                </div>

                <div class="card">
                    <h2>📊 Data Science</h2>
                    <p>Learn data analysis, visualization and important data science concepts.</p>
                    <a class="btn" href="https://www.kaggle.com/learn" target="_blank">
                        Start Learning
                    </a>
                </div>

                <div class="card">
                    <h2>🤖 Machine Learning</h2>
                    <p>Learn machine learning algorithms and practical concepts.</p>
                    <a class="btn" href="https://developers.google.com/machine-learning/crash-course" target="_blank">
                        Start Learning
                    </a>
                </div>

                <div class="card">
                    <h2>📈 Statistics</h2>
                    <p>Learn probability, mean, median, correlation and statistical concepts.</p>
                    <a class="btn" href="https://www.khanacademy.org/math/statistics-probability" target="_blank">
                        Start Learning
                    </a>
                </div>

                <div class="card">
                    <h2>💻 SQL</h2>
                    <p>Learn databases, SQL queries, filtering, joins and data management.</p>
                    <a class="btn" href="https://www.w3schools.com/sql/" target="_blank">
                        Start Learning
                    </a>
                </div>

                <div class="card">
                    <h2>🧠 AI</h2>
                    <p>Understand artificial intelligence and modern AI concepts.</p>
                    <a class="btn" href="https://www.ibm.com/think/topics/artificial-intelligence" target="_blank">
                        Explore AI
                    </a>
                </div>

            </div>

            <a class="back" href="/">← Back to Dashboard</a>

        </div>

    </body>
    </html>
    """
@app.route("/profile")
def profile():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Profile</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f7fb;
                margin: 0;
                padding: 40px;
            }

            .profile {
                max-width: 600px;
                margin: auto;
                background: white;
                padding: 35px;
                border-radius: 20px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.12);
                text-align: center;
            }

            .avatar {
                font-size: 70px;
                margin-bottom: 10px;
            }

            h1 {
                color: #2563eb;
                margin-bottom: 5px;
            }

            .subtitle {
                color: #666;
                margin-bottom: 25px;
            }

            .info {
                text-align: left;
                background: #f8fafc;
                padding: 18px;
                border-radius: 12px;
                margin-top: 15px;
            }

            .info p {
                font-size: 17px;
                margin: 12px 0;
            }

            .back {
                display: inline-block;
                margin-top: 25px;
                padding: 12px 20px;
                background: #2563eb;
                color: white;
                text-decoration: none;
                border-radius: 8px;
            }
        </style>
    </head>

    <body>

        <div class="profile">

            <div class="avatar">👨‍🎓</div>

            <h1>Abhijeet Singh</h1>
            <p class="subtitle">Data Science Student</p>

            <div class="info">
                <p><strong>👤 Username:</strong> Abhijeet Singh</p>
                <p><strong>🎓 Course:</strong> B.Tech / Data Science</p>
                <p><strong>🆔 Roll Number:</strong> 0177CD231002</p>
                <p><strong>📊 Attendance:</strong> 82%</p>
                <p><strong>📚 Subjects:</strong> 6</p>
                <p><strong>📝 Pending Assignments:</strong> 4</p>
                <p><strong>💻 Specialization:</strong> Data Science & AI</p>
            </div>

            <a class="back" href="/">← Back to Dashboard</a>

        </div>

    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(debug=True)