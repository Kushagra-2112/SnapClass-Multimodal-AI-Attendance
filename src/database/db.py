from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    """Hash a password for storing."""
    return bcrypt.hashpw(pwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def check_pass(pwd, hashed):
    """Check a password against a hash."""
    return bcrypt.checkpw(pwd.encode('utf-8'), hashed.encode('utf-8'))

def check_teacher_exists(username):
    """Returns True if the username is already in the database."""
    try:
        response = supabase.table("teachers").select("username").eq("username", username).execute()
        return len(response.data) > 0 
    except Exception as e:
        print(f"Database error: {e}")
        return False

def create_teacher(username, password, name):
    """Inserts a new teacher into the Supabase table."""
    try:
        data = { 
            "username": username, 
            "password": hash_pass(password), 
            "name": name
        }
        response = supabase.table("teachers").insert(data).execute()
        return len(response.data) > 0
    except Exception as e:
        print(f"Registration error: {e}")
        return False

def teacher_login(username, password):
    """Verifies credentials and returns teacher data or None."""
    try:
        # Using ilike for case-insensitive username matching
        response = supabase.table("teachers").select("*").ilike("username", username).execute()
        if response.data:
            teacher = response.data[0]
            if check_pass(password, teacher['password']):
                return teacher
    except Exception as e:
        print(f"Login error: {e}")
    return None


def get_all_students():
    response = supabase.table('students').select("*").execute()
    return response.data