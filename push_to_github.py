
import subprocess
import os

def push_to_github():
    # Configure git
    subprocess.run(['git', 'config', '--global', 'user.name', 'Santuuuuu'])
    subprocess.run(['git', 'config', '--global', 'user.email', 'shantu.das77@gmail.com'])
    
    # Initialize git if not already
    if not os.path.exists('.git'):
        subprocess.run(['git', 'init'])
    
    # Add all files
    subprocess.run(['git', 'add', '.'])
    
    # Commit
    subprocess.run(['git', 'commit', '-m', 'Add complete Iris data poisoning experiment with MLFlow tracking'])
    
    # Add remote origin
    subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/Santuuuuu/mlops_week8.git'])
    
    # Push using token (this will be visible in process list, use with caution)
    print("Pushing to GitHub...")
    result = subprocess.run([
        'git', 'push', 
        'https://Santuuuuu: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@github.com/Santuuuuu/mlops_week8.git', 
        'main'
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Code pushed successfully to GitHub!")
    else:
        print("❌ Push failed:")
        print(result.stderr)

push_to_github()
