import shutil
import os

poses = [
    r"C:\Users\Sharm\.gemini\antigravity\brain\a8cb43e6-2ab0-4179-9c47-3fdb81f165a8\aditi_pose1_1785607417886.jpg",
    r"C:\Users\Sharm\.gemini\antigravity\brain\a8cb43e6-2ab0-4179-9c47-3fdb81f165a8\aditi_pose2_1785607428578.jpg",
    r"C:\Users\Sharm\.gemini\antigravity\brain\a8cb43e6-2ab0-4179-9c47-3fdb81f165a8\aditi_pose3_1785607440628.jpg",
    r"C:\Users\Sharm\.gemini\antigravity\brain\a8cb43e6-2ab0-4179-9c47-3fdb81f165a8\aditi_pose4_1785607451626.jpg",
]

dst_dir = r"C:\Users\Sharm\.gemini\antigravity\scratch\password-strength-checker\static\images\poses"
os.makedirs(dst_dir, exist_ok=True)

for i, src in enumerate(poses, 1):
    dst = os.path.join(dst_dir, f"pose{i}.jpg")
    shutil.copy(src, dst)
    print(f"Copied pose {i} -> {dst}")
