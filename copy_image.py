import shutil
import os

src = r"C:\Users\Sharm\.gemini\antigravity\brain\a8cb43e6-2ab0-4179-9c47-3fdb81f165a8\cute_cartoon_aditi_1785607264591.jpg"
dst_dir = r"C:\Users\Sharm\.gemini\antigravity\scratch\password-strength-checker\static\images"
dst = os.path.join(dst_dir, "aditi_cartoon.jpg")

os.makedirs(dst_dir, exist_ok=True)
shutil.copy(src, dst)
print("Copied cartoon Aditi image successfully to", dst)
