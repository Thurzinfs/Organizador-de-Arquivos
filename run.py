import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

from app.main import use_case

if __name__ == "__main__":
    use_case.execute()
    print("Automação iniciada...")
