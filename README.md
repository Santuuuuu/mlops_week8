#!/usr/bin/env python3
"""
Create complete submission zip file with code, outputs, and documentation
"""

import os
import zipfile
import datetime
from pathlib import Path

def create_submission_zip():
    """Create submission zip with all required components"""
    
    # Create timestamp for unique filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_filename = f"iris_classifier_vertexai_submission_{timestamp}.zip"
    
    # Files and directories to include
    components = {
        'code': [
            'iris_classifier_vertexai.ipynb',  # Your main notebook
            '*.py',                            # Any Python scripts
            '*.sh',                            # Any shell scripts
        ],
        'outputs': [                           # Demonstration outputs
            'outputs/'
        ],
        'documentation': [
            'README.md'
        ]
    }
    
    print("📦 Creating submission zip file...")
    print("=" * 50)
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        files_added = 0
        
        # Add code files
        print("\n💻 Adding code files:")
        for pattern in components['code']:
            if '*' in pattern:
                # Handle wildcard patterns
                import glob
                files = glob.glob(pattern)
                for file in files:
                    if os.path.exists(file):
                        zipf.write(file, f"code/{os.path.basename(file)}")
                        print(f"  ✅ code/{os.path.basename(file)}")
                        files_added += 1
            else:
                # Single file
                if os.path.exists(pattern):
                    zipf.write(pattern, f"code/{os.path.basename(pattern)}")
                    print(f"  ✅ code/{os.path.basename(pattern)}")
                    files_added += 1
        
        # Add output files
        print("\n📊 Adding output files:")
        for item in components['outputs']:
            if os.path.exists(item):
                if os.path.isdir(item):
                    # Add entire directory
                    for root, dirs, files in os.walk(item):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.join('outputs', os.path.relpath(file_path, 'outputs'))
                            zipf.write(file_path, arcname)
                            print(f"  ✅ {arcname}")
                            files_added += 1
                else:
                    # Single file
                    zipf.write(item, f"outputs/{os.path.basename(item)}")
                    print(f"  ✅ outputs/{os.path.basename(item)}")
                    files_added += 1
        
        # Add documentation
        print("\n📖 Adding documentation:")
        for doc_file in components['documentation']:
            if os.path.exists(doc_file):
                zipf.write(doc_file, doc_file)
                print(f"  ✅ {doc_file}")
                files_added += 1
    
    # Verify and show summary
    if os.path.exists(zip_filename):
        file_size = os.path.getsize(zip_filename) / 1024 / 1024  # Size in MB
        
        print(f"\n🎉 SUBMISSION ZIP CREATED SUCCESSFULLY!")
        print("=" * 50)
        print(f"📁 File: {zip_filename}")
        print(f"📊 Size: {file_size:.2f} MB")
        print(f"📦 Files included: {files_added}")
        
        # Show contents
        print(f"\n📋 ZIP FILE CONTENTS:")
        with zipfile.ZipFile(zip_filename, 'r') as zipf:
            for file in sorted(zipf.namelist()):
                print(f"  📄 {file}")
        
        print(f"\n✅ READY FOR SUBMISSION!")
        
    else:
        print("❌ Failed to create zip file")

if __name__ == "__main__":
    create_submission_zip()