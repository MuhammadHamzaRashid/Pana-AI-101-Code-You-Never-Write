import os
import hashlib
import shutil
import time
from collections import defaultdict

# --- CONFIGURATION ---
TARGET_DIR = os.path.expanduser("~/Downloads")
REPORT_DIR = os.path.join(TARGET_DIR, "Downloads_Reconciled")
LARGE_FILE_LIMIT_MB = 100
DRAFT_KEYWORDS = ['draft', 'working', 'copy', 'temp', 'v1', 'v2', 'v0', 'final_']

EXTENSIONS = {
    'Media': ['.jpg', '.jpeg', '.png', '.mp4', '.mp3', '.mov', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx', '.csv'],
    'Installers': ['.exe', '.msi', '.dmg', '.pkg'],
    'Compressed': ['.zip', '.rar', '.7z', '.tar.gz'],
}

def get_file_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except: return None

def audit_downloads():
    files_by_hash = defaultdict(list)
    draft_docs = []
    category_sizes = defaultdict(float) # To track duplicate waste by type
    total_files = 0
    
    print("🔍 Backstage: Scanning your Downloads folder...")

    for root, dirs, files in os.walk(TARGET_DIR):
        if "Downloads_Reconciled" in root: continue
        for filename in files:
            filepath = os.path.join(root, filename)
            total_files += 1
            
            # 1. Duplicate & Size Logic
            f_hash = get_file_hash(filepath)
            f_size = os.path.getsize(filepath) / (1024 * 1024)
            files_by_hash[f_hash].append((filepath, f_size))

            # 2. "Draft" Discovery Logic
            ext = os.path.splitext(filename)[1].lower()
            if ext in EXTENSIONS['Documents']:
                # If name contains draft keywords AND hasn't been touched in 2 weeks
                is_draft = any(k in filename.lower() for k in DRAFT_KEYWORDS)
                days_since_mod = (time.time() - os.path.getmtime(filepath)) / (24 * 3600)
                if is_draft and days_since_mod > 14:
                    draft_docs.append(filename)

    # Calculate duplicate waste by category
    waste_by_cat = defaultdict(float)
    for f_hash, paths in files_by_hash.items():
        if len(paths) > 1:
            # All copies except the first one are "waste"
            ext = os.path.splitext(paths[0][0])[1].lower()
            found_cat = "Others"
            for cat, exts in EXTENSIONS.items():
                if ext in exts: found_cat = cat; break
            
            waste_mb = sum(p[1] for p in paths[1:])
            waste_by_cat[found_cat] += waste_mb

    # --- THE "HUMAN" SUMMARY ---
    print("\n" + "="*40)
    print("      THE BOOKKEEPER'S RECONCILIATION")
    print("="*40)

    # Sentence 1: Duplicate Media
    media_waste_gb = waste_by_cat['Media'] / 1024
    if media_waste_gb > 0.01:
        print(f"✨ I found {media_waste_gb:.2f} GB of duplicate photos and videos I can delete.")
    
    # Sentence 2: Drafts
    if draft_docs:
        print(f"📝 I rediscovered {len(draft_docs)} half-finished documents worth returning to.")

    # Sentence 3: General Waste
    total_waste = sum(waste_by_cat.values())
    if total_waste > 100:
        print(f"🗑️  Overall, I can reclaim {total_waste/1024:.2f} GB by cleaning duplicates across all folders.")

    print(f"\nScanning complete. Total files processed: {total_files}")
    print(f"Files to be organized into: {REPORT_DIR}")
    
    # --- APPROVAL STEP ---
    user_input = input("\nType 'approve' to safely organize these files, or any other key to cancel: ").strip().lower()
    
    if user_input == 'approve':
        execute_cleanup(files_by_hash)
    else:
        print("❌ Action cancelled. No files were moved.")

def execute_cleanup(files_by_hash):
    if not os.path.exists(REPORT_DIR): os.makedirs(REPORT_DIR)
    
    print("\n🚀 Executing cleanup...")
    for f_hash, paths in files_by_hash.items():
        # Only move the primary file of each hash to keep it organized
        filepath = paths[0][0]
        filename = os.path.basename(filepath)
        ext = os.path.splitext(filename)[1].lower()
        
        found_cat = "Others"
        for category, extensions in EXTENSIONS.items():
            if ext in extensions: found_cat = category; break
        
        dest_folder = os.path.join(REPORT_DIR, found_cat)
        if not os.path.exists(dest_folder): os.makedirs(dest_folder)
        
        try:
            shutil.move(filepath, os.path.join(dest_folder, filename))
        except Exception as e:
            print(f"Could not move {filename}: {e}")
            
    print(f"\n✅ Done! Check your organized files in: {REPORT_DIR}")

if __name__ == "__main__":
    audit_downloads()
