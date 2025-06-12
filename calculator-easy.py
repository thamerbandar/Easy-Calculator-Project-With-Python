import tkinter as tk

def count_words():
    text = text_box.get("1.0", tk.END)  # جلب النص من بداية الصندوق حتى نهايته
    words = text.split()  # تقسيم النص لكلمات بناءً على الفراغات
    count = len(words)
    result_label.config(text=f"عدد الكلمات: {count}")

# إنشاء النافذة
window = tk.Tk()
window.title("عداد الكلمات")
window.geometry("400x300")

# صندوق النصوص
text_box = tk.Text(window, height=10, width=40)
text_box.tag_configure("w", justify='w') # محاذاة النص إلى اليمين
text_box.tag_add("right", "1.0", "end") #تطبيق المحاذاة على النص 
text_box.insert("1.0", "اكتب نصك هنا...") # نص افتراضي
text_box.pack(pady=10)

# زر العد
count_button = tk.Button(window, text="احسب عدد الكلمات", command=count_words)
count_button.pack()

# لعرض النتيجة
result_label = tk.Label(window, text="عدد الكلمات: 0", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
