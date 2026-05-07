class Library:
    def __init__(self):
        self.kitoblar = []

    def kitob_qoish(self, nom, muallif, yil):
        self.kitoblar.append({
            'nom': nom,
            'muallif': muallif,
            'yil': yil
        })

    def kitoblarini_chiqar(self):
        for kitob in self.kitoblar:
            print(f"Nom: {kitob['nom']}")
            print(f"Muallif: {kitob['muallif']}")
            print(f"Yil: {kitob['yil']}")
            print("------------------------")

# Misol:
kitobxona = Library()
kitobxona.kitob_qoish("Don Kishot", "Miguel de Cervantes", 1605)
kitobxona.kitob_qoish("Gulliver sayohatlari", "Jonatan Swift", 1726)
kitobxona.kitoblarini_chiqar()
```

Bu kodda biz `Library` classini yaratib, `kitob_qoish` funksiyasini yozdik. Bu funksiya kitobni qo'shish uchun mo'ljallangan. `kitoblarini_chiqar` funksiyasi esa kitoblar ro'yxatini chiqarish uchun mo'ljallangan. Misol uchun ikkita kitob qo'shib, ularni chiqarish uchun funksiya chaqirildi.
