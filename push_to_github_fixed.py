
import subprocess
import os
import sys

def run_command(cmd):
    '''Run a shell command and return output'''
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def push_to_github():
    print("🚀 Starting GitHub push process...")
    
    # Step 1: Configure git
    print("1. Configuring git...")
    run_command('git config --global user.name "Santuuuuu"')
    run_command('git config --global user.email "shantu.das77@gmail.com"')
    
    # Step 2: Check if we're in a git repository
    if not os.path.exists('.git'):
        print("   Initializing git repository...")
        run_command('git init')
    
    # Step 3: Check current branch
    print("2. Checking branches...")
    returncode, stdout, stderr = run_command('git branch')
    print(f"   Current branches: {stdout}")
    
    # Step 4: Create main branch if it doesn't exist
    if 'main' not in stdout:
        print("   Creating main branch...")
        run_command('git checkout -b main')
    else:
        print("   Switching to main branch...")
        run_command('git checkout main')
    
    # Step 5: Add files
    print("3. Adding files...")
    returncode, stdout, stderr = run_command('git add .')
    if returncode == 0:
        print("   ✅ Files added successfully")
    else:
        print(f"   ❌ Error adding files: {stderr}")
    
    # Step 6: Commit changes
    print("4. Committing changes...")
    commit_message = "Add complete Iris data poisoning experiment with MLFlow tracking"
    returncode, stdout, stderr = run_command(f'git commit -m "{commit_message}"')
    if returncode == 0:
        print("   ✅ Changes committed")
    else:
        print(f"   ❌ Commit failed: {stderr}")
        # If commit fails due to no changes, try with different message
        if "nothing to commit" in stderr:
            run_command('git commit -m "Update Iris data poisoning experiment" --allow-empty')
    
    # Step 7: Add remote origin
    print("5. Setting up remote...")
    run_command('git remote remove origin')  # Remove if exists
    run_command('git remote add origin https://github.com/Santuuuuu/mlops_week8.git')
    
    # Step 8: Push to GitHub
    print("6. Pushing to GitHub...")
    push_url = 'https://Santuuuuu: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@github.com/Santuuuuu/mlops_week8.git'
    returncode, stdout, stderr = run_command(f'git push -u {push_url} main')
    
    if returncode == 0:
        print("🎉 ✅ Code pushed successfully to GitHub!")
        print("📁 Repository: https://github.com/Santuuuuu/mlops_week8")
    else:
        print(f"❌ Push failed: {stderr}")
        print("Trying force push...")
        returncode, stdout, stderr = run_command(f'git push -f -u {push_url} main')
        if returncode == 0:
            print("🎉 ✅ Code pushed successfully with force push!")
        else:
            print(f"❌ Force push also failed: {stderr}")

if __name__ == "__main__":
    push_to_github()
