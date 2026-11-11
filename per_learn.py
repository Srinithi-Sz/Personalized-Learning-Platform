import tkinter as tk
from tkinter import messagebox
import mysql.connector


# ---------------- DB ----------------
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root@123",
        database="learning_platform"
    )


# ---------------- MAIN APP ----------------
class LearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 Personalized Learning Platform")
        self.root.geometry("950x600")
        self.root.configure(bg="#0f172a")

        self.user_id = None
        self.login_page()


    # ---------------- UI CLEANER ----------------
    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()


    # ---------------- LOGIN PAGE ----------------
    def login_page(self):
        self.clear()

        frame = tk.Frame(self.root, bg="#1e293b", bd=2, relief="ridge")
        frame.place(x=250, y=80, width=450, height=420)

        tk.Label(frame, text="Welcome Back  👨‍🎓",
                 font=("Arial", 20, "bold"),
                 bg="#1e293b", fg="white").pack(pady=20)

        # Username label + entry
        tk.Label(frame, text="Name",
                 bg="#1e293b", fg="white",
                 font=("Arial", 12)).pack(pady=5)

        self.username = tk.Entry(frame, font=("Arial", 14))
        self.username.pack(pady=5)

        # Password label + entry
        tk.Label(frame, text="Password",
                 bg="#1e293b", fg="white",
                 font=("Arial", 12)).pack(pady=5)

        self.password = tk.Entry(frame, font=("Arial", 14), show="*")
        self.password.pack(pady=5)

        tk.Button(frame, text="Login",
                  bg="#22c55e", fg="white",
                  font=("Arial", 12),
                  command=self.login).pack(pady=15)

        tk.Button(frame, text="Register",
                  bg="#3b82f6", fg="white",
                  font=("Arial", 12),
                  command=self.register).pack()


    # ---------------- REGISTER ----------------
    def register(self):
        db = connect()
        cur = db.cursor()

        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                    (self.username.get(), self.password.get()))
        db.commit()
        db.close()

        messagebox.showinfo("Success", "Registered Successfully!")


    # ---------------- LOGIN ----------------
    def login(self):
        db = connect()
        cur = db.cursor()

        cur.execute("SELECT id FROM users WHERE username=%s AND password=%s",
                    (self.username.get(), self.password.get()))

        result = cur.fetchone()
        db.close()

        if result:
            self.user_id = result[0]
            self.dashboard()
        else:
            messagebox.showerror("Error", "Invalid Login")


    # ---------------- DASHBOARD ----------------
    def dashboard(self):
        self.clear()

        # Title
        tk.Label(self.root, text="📚 Learning Dashboard",
                 font=("Arial", 22, "bold"),
                 bg="#0f172a", fg="white").pack(pady=10)

        # Card frame
        card = tk.Frame(self.root, bg="#1e293b", bd=2, relief="ridge")
        card.place(x=220, y=80, width=500, height=420)

        # Course name
        tk.Label(card, text="Course Name",
                 bg="#1e293b", fg="white",
                 font=("Arial", 12)).pack(pady=5)

        self.course_entry = tk.Entry(card, font=("Arial", 14))
        self.course_entry.pack(pady=5)

        # Level selection
        tk.Label(card, text="Your Level (Beginner / Intermediate / Advanced)",
                 bg="#1e293b", fg="white",
                 font=("Arial", 12)).pack(pady=5)

        self.level_entry = tk.Entry(card, font=("Arial", 14))
        self.level_entry.pack(pady=5)

        tk.Button(card, text="Add Learning",
                  bg="#22c55e", fg="white",
                  command=self.add_course).pack(pady=10)

        tk.Button(card, text="Show My Courses",
                  bg="#3b82f6", fg="white",
                  command=self.show_courses).pack(pady=5)

        self.output = tk.Label(card, text="",
                               bg="#1e293b", fg="white",
                               font=("Arial", 12))
        self.output.pack(pady=10)

        tk.Button(card, text="Logout",
                  bg="red", fg="white",
                  command=self.login_page).pack(pady=10)


    # ---------------- LEVEL SUGGESTION ----------------
    def suggest_next_level(self, level):
        level = level.lower()

        if level == "beginner":
            return "👉 Next Step: Intermediate (Start DSA basics, mini projects)"
        elif level == "intermediate":
            return "👉 Next Step: Advanced (Build full projects + APIs)"
        elif level == "advanced":
            return "🔥 You are ready for real-world projects + internships!"
        else:
            return "⚠ Enter Beginner / Intermediate / Advanced"


    # ---------------- ADD COURSE ----------------
    def add_course(self):
        db = connect()
        cur = db.cursor()

        course = self.course_entry.get()
        level = self.level_entry.get()

        cur.execute(
            "INSERT INTO progress (user_id, course, progress) VALUES (%s, %s, %s)",
            (self.user_id, course, 0)
        )
        db.commit()
        db.close()

        suggestion = self.suggest_next_level(level)

        self.output.config(
            text=f"✅ Added: {course}\n📊 Level: {level}\n{suggestion}"
        )


    # ---------------- SHOW COURSES ----------------
    def show_courses(self):
        db = connect()
        cur = db.cursor()

        cur.execute("SELECT course, progress FROM progress WHERE user_id=%s",
                    (self.user_id,))
        data = cur.fetchall()
        db.close()

        text = "📖 Your Courses:\n\n"
        for c in data:
            text += f"• {c[0]} - {c[1]}%\n"

        self.output.config(text=text)


# ---------------- RUN ----------------
root = tk.Tk()
app = LearningApp(root)
root.mainloop()