data_user = {
    "u001": {
        "nama": "Aaron",
        "post": [
            ("2025-01-01", 120, 15, ["python", "coding"]),
            ("2025-01-02", 200, 30, ["ai", "machinelearning"])
        ]
    },
    "u002": {
        "nama": "XR",
        "post": [
            ("2025-01-01", 300, 40, ["design", "creativity"]),
            ("2025-01-03", 150, 10, ["coding", "uiux"])
        ]
    }
}

def user_activity_summary(data):
    per_user = {}
    tag_count = {}
    for _, info in data.items():
        nama = info["nama"]
        total_like = 0
        total_comment = 0
        for (tanggal, like, comment, tag_list) in info["post"]:
            total_like += like
            total_comment += comment
            for t in tag_list:
                tag_count[t] = tag_count.get(t, 0) + 1
        per_user[nama] = (total_like, total_comment)
    return per_user, tag_count

per_user, tag_count = user_activity_summary(data_user)

print("=== Aktivitas Pengguna ===")
for nama in sorted(per_user.keys()):
    like, comm = per_user[nama]
    print(f"{nama} → Likes: {like} | Comments: {comm}")

print("=== Tag Populer ===")
for tag, cnt in sorted(tag_count.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"{tag}: {cnt} kali")