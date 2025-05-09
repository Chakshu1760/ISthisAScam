# scam_detector.py

print("🔍 Scam Detection CLI Tool")
print("--------------------------")

# Simple list of scammy keywords
scam_keywords = ["urgent", "win", "click here", "free", "limited offer", "verify", "password", "lottery", "bank account", "gift"]

# Get user input
message = input("Enter the message to analyze: ").lower()

# Check for keywords
hits = [word for word in scam_keywords if word in message]

# Basic scoring
score = len(hits) / len(scam_keywords) * 100

# Output result
print(f"\nScam Likelihood Score: {score:.1f}%")
if score > 50:
    print("⚠️ Warning: This message is very likely a scam!")
elif score > 20:
    print("⚠️ Caution: This message could be a scam.")
else:
    print("✅ Low risk. Still, always stay alert.")

# Show matched keywords
if hits:
    print(f"🔑 Keywords detected: {', '.join(hits)}")
else:
    print("No suspicious keywords detected.")

