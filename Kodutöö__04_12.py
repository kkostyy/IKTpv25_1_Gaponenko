# praktika.py
# Код для всех задач 1️⃣–1️⃣6️⃣
# Комментарии на русском, подсказки и выводы на эстонском.
import random
import string

VOWELS = "aeiouõäöüAEIOUÕÄÖÜ"

def count_letters(text):
    """1️⃣ Sõna või lause analüüs: loendab täishäälikud, kaashäälikud, tühikud ja kirjavahemärgid"""
    vowels = 0
    consonants = 0
    spaces = 0
    punctuation = 0
    for ch in text:
        if ch.isspace():
            spaces += 1
        elif ch.isalpha():
            if ch in VOWELS:
                vowels += 1
            else:
                consonants += 1
        else:
            punctuation += 1
    return vowels, consonants, spaces, punctuation

# 2.1 Nimed — küsib viis nime, sorteerib, lubab redigeerida
def names_menu():
    print("2.1 NIMED — sisesta viis nime (Enter lõpetab, kui vähem kui 5) / Kirjuta 'exit' lõpetamiseks")
    names = []
    while len(names) < 5:
        n = input(f"Sisesta nimi #{len(names)+1}: ").strip()
        if not n or n.lower() == 'exit':
            break
        names.append(n)
    names.sort(key=lambda s: s.lower())
    print("\nNimed tähestikulises järjekorras:")
    for nm in names:
        print(nm)
    if names:
        print("\nViimane lisatud nimi:", names[-1])
    # redigeerimise võimalus
    if names:
        edit = input("Kas soovid nimekirjas nimesid muuta? (jah/ei): ").strip().lower()
        if edit == 'jah' or edit == 'y':
            for i, nm in enumerate(names):
                print(f"{i+1}. {nm}")
            try:
                idx = int(input("Vali, millist nr soovid muuta: ")) - 1
                if 0 <= idx < len(names):
                    new = input("Sisesta uus nimi: ").strip()
                    names[idx] = new
                    names.sort(key=lambda s: s.lower())
                    print("Uus nimekiri:")
                    for nm in names:
                        print(nm)
                else:
                    print("Valesti valitud indeks.")
            except ValueError:
                print("Pole korrektne number.")
    return names

# 2.2 Kordustega nimed — eemaldab kordused
def unique_names(names_with_dups):
    return list(dict.fromkeys(names_with_dups))  # säilitab järjekorra (py3.7+)

# 2.3 Vanused — suurim, väikseim, summa, keskmine
def age_stats(ages):
    if not ages:
        return None
    maks = max(ages)
    minv = min(ages)
    s = sum(ages)
    avg = s / len(ages)
    return maks, minv, s, avg

# 3️⃣ Tärnide lintdiagramm — võtab listi arvudest ja joonistab
def stars_chart(numbers):
    for n in numbers:
        print('*' * n)

# 4️⃣ Postiindeks kontroll — 5 numbrit, esimene number määrab maakonda
POSTI = {
    '1': "Tallinn",
    '2': "Narva, Narva-Jõesuu",
    '3': "Kohtla-Järve",
    '4': "Ida-Virumaa, Lääne-Virumaa, Jõgevamaa",
    '5': "Tartu linn",
    '6': "Tartumaa, Põlvamaa, Võrumaa, Valgamaa",
    '7': "Viljandimaa, Järvamaa, Harjumaa, Raplamaa",
    '8': "Pärnumaa",
    '9': "Läänemaa, Hiiumaa, Saaremaa"
}
def check_postcode(code):
    code = code.strip()
    if len(code) != 5 or not code.isdigit():
        return False, "Postiindeks peab olema 5 numbrit."
    region = POSTI.get(code[0], "Tundmatu maakond")
    special = "Mine merre!" if code[0] in ('1','2','3') else "Mine metsa!"
    return True, (region, special)

# 5️⃣ Vahetus ↔️ — vaheta paarid vastavalt, küsib mitu paari vahetada
def swap_pairs(lst, pairs_to_swap):
    n = len(lst)
    max_pairs = n // 2
    pairs = min(pairs_to_swap, max_pairs)
    for i in range(pairs):
        j = n - 1 - i
        lst[i], lst[j] = lst[j], lst[i]
    return lst

# 6️⃣ „Arvud“ — leia suurim, jaga pikkusega ja asenda tulemusena
def replace_max_with_division(numbers):
    if not numbers:
        return numbers
    maxi = max(numbers)
    idx = numbers.index(maxi)
    result = maxi / len(numbers)
    numbers[idx] = result
    return numbers

# 7️⃣ Sorteerimine — absoluutväärtuse järgi kasvavalt või kahanevalt
def sort_by_abs(numbers, reverse=False):
    return sorted(numbers, key=abs, reverse=reverse)

# 8️⃣ Võrdse pikkusega sõned — lühema täitmine '_' abil
def equalize_lengths(words):
    maxlen = max(len(w) for w in words)
    return [w + '_' * (maxlen - len(w)) for w in words]

# 9️⃣ Nime kontroll — ainult tähed, tervitus, loendamine, unikaalsed tähed tähestikulises järjekorras
def name_check(name):
    if not name.isalpha():
        return False, "Nimi peab sisaldama ainult tähti."
    capitalized = name.capitalize()
    letters = len([c for c in name if c.isalpha()])
    vowels = sum(1 for c in name if c in VOWELS)
    consonants = letters - vowels
    unique_sorted = ''.join(sorted(set(name.lower())))
    return True, {
        'greeting': f"Tere, {capitalized}!",
        'letters': letters,
        'vowels': vowels,
        'consonants': consonants,
        'unique_sorted': unique_sorted
    }

# 🔟 Töötajate andmed — maks palk, keskmine, mitu üle keskmise, keskmine vanus gruppides
def employees_stats(employees):
    if not employees:
        return {}
    salaries = [e['salary'] for e in employees]
    ages = [e['age'] for e in employees]
    max_salary = max(salaries)
    max_emp = [e for e in employees if e['salary'] == max_salary]
    avg_salary = sum(salaries) / len(salaries)
    over_avg = sum(1 for s in salaries if s > avg_salary)
    le = [e['age'] for e in employees if e['age'] <= avg_salary]
    gt = [e['age'] for e in employees if e['age'] > avg_salary]
    avg_le = sum(le)/len(le) if le else None
    avg_gt = sum(gt)/len(gt) if gt else None
    return {
        'max_salary_employees': max_emp,
        'avg_salary': avg_salary,
        'count_over_avg': over_avg,
        'avg_age_le_avg_salary': avg_le,
        'avg_age_gt_avg_salary': avg_gt
    }

# 1️⃣1️⃣ Inglise tähestik — loendid
def english_alphabets(n=26):
    letters = list(string.ascii_lowercase[:n])
    repeated = [letters[i] * (i+1) for i in range(len(letters))]
    return letters, repeated

# 1️⃣2️⃣ Min ja max vahetamine — genereeri 10 juhuslikku arvu ja vaheta väikseim ja suurim
def swap_min_max_random():
    lst = [random.randint(-50, 50) for _ in range(10)]
    minv = min(lst)
    maxv = max(lst)
    i_min = lst.index(minv)
    i_max = lst.index(maxv)
    lst[i_min], lst[i_max] = lst[i_max], lst[i_min]
    return lst, minv, maxv

# 1️⃣3️⃣ Arva sõna ära — lihtne hangman-like mäng
def guess_word_game(word_list=None):
    if word_list is None:
        word_list = ['kass', 'auto', 'mets', 'tamm', 'laev', 'kodus', 'õun', 'sõber']
    word = random.choice(word_list).lower()
    guessed = ['_' for _ in word]
    wrong = []
    attempts = 0
    while '_' in guessed:
        print("Sõna:", ' '.join(guessed))
        ch = input("Arva täht: ").strip().lower()
        if not ch or len(ch) != 1 or not ch.isalpha():
            print("Sisesta üks täht.")
            continue
        attempts += 1
        if ch in word:
            for i, c in enumerate(word):
                if c == ch:
                    guessed[i] = ch
            print("Õige!")
        else:
            if ch not in wrong:
                wrong.append(ch)
            print("Vale!")
        print("Valed tähed:", ','.join(wrong))
    print(f"Õnnitleme! Sõna '{word}' ära arvatud {attempts} katses.")
    return word, attempts, wrong

# 1️⃣4️⃣ Euroopa pealinnad — loend, sort, lisa kaks, korda
def european_capitals(initial=None):
    if initial is None:
        initial = ["Tallinn","Helsinki","Stockholm","Oslo","Copenhagen","Riga","Vilnius","Warsaw","Prague","Vienna"]
    print("Iga linn eraldi:")
    for city in initial:
        print(city)
    initial_sorted = sorted(initial, key=lambda s: s.lower())
    print("\nTähestikuliselt sorteeritud:")
    for c in initial_sorted:
        print(c)
    a = input("Sisesta esimene lisa-pealinn: ").strip()
    b = input("Sisesta teine lisa-pealinn: ").strip()
    if a:
        initial.append(a)
    if b:
        initial.append(b)
    initial_sorted = sorted(initial, key=lambda s: s.lower())
    print("\nPärast lisamist ja sorteerimist:")
    for i, c in enumerate(initial_sorted, 1):
        print(f"{i}. {c}")
    print(f"\nMeie loendis on {len(initial_sorted)} Euroopa pealinna.")
    return initial_sorted

# 1️⃣5️⃣ Lihtne sõnaraamat — neli listi ja tabel
def simple_dict():
    numbers = [1, 2, 3, 4, 5]
    est = ['üks', 'kaks', 'kolm', 'neli', 'viis']
    eng = ['one', 'two', 'three', 'four', 'five']
    ita = ['uno', 'due', 'tre', 'quattro', 'cinque']
    numbers += [6,7]
    est += ['kuus','seitse']
    eng += ['six','seven']
    ita += ['sei','sette'] 
    exists_tre = 'tre' in ita
    est_sorted = sorted(est)
    eng_sorted = sorted(eng)
    ita_sorted = sorted(ita)
    return numbers, est_sorted, eng_sorted, ita_sorted, exists_tre

# 1️⃣6️⃣ Jah/Ei vastus — juhuslik vastus
def magic_8ball(question):
    answers = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]
    return random.choice(answers)

# Lihtne menüü kasutamiseks
def main_menu():
    while True:
        print("\nVali ülesanne (1-16) või 'q' lõpetamiseks:")
        print("1 – Sõna/ lause analüüs")
        print("2.1 – Nimed; 2.2 – Kordustega nimed; 2.3 – Vanused")
        print("3 – Tärnide diagramm")
        print("4 – Postiindeks kontroll")
        print("5 – Vaheta paare")
        print("6 – Asenda suurim jagatuga")
        print("7 – Sorteerimine absoluutväärtuse järgi")
        print("8 – Võrdse pikkusega sõned")
        print("9 – Nime kontroll")
        print("10 – Töötajate andmed")
        print("11 – Inglise tähestik")
        print("12 – Min/Max vahetus")
        print("13 – Arva sõna ära")
        print("14 – Euroopa pealinnad")
        print("15 – Lihtne sõnaraamat")
        print("16 – Jah/Ei vastus")
        choice = input("Sinu valik: ").strip().lower()
        if choice == 'q':
            print("Lõpetame. Nägemist!")
            break
        if choice == '1':
            text = input("Sisesta sõna või lause: ")
            v,c,sp,p = count_letters(text)
            print(f"Täishäälikud: {v}, Kaashäälikud: {c}, Tühikud: {sp}, Kirjavahemärgid: {p}")
        elif choice == '2.1' or choice == '2.1 ':
            names_menu()
        elif choice == '2.2':
            s = input("Sisesta nimed komadega (või jätke näidis: Anna,Peeter,Anna,Liisa): ")
            if not s:
                s = "Anna,Peeter,Anna,Liisa"
            lst = [x.strip() for x in s.split(',')]
            print("Ilma kordusteta:", unique_names(lst))
        elif choice == '2.3':
            s = input("Sisesta vanused komadega (näide: 23,34,45): ")
            ages = [int(x.strip()) for x in s.split(',') if x.strip().isdigit()]
            res = age_stats(ages)
            if res:
                print("Suurim:", res[0], "Väikseim:", res[1], "Summa:", res[2], "Keskmine:", res[3])
            else:
                print("Ühtegi vanust.")
        elif choice == '3':
            s = input("Sisesta arvud komadega (näide: 5,10,3): ")
            nums = [int(x.strip()) for x in s.split(',') if x.strip().lstrip('-').isdigit()]
            stars_chart(nums)
        elif choice == '4':
            code = input("Sisesta postiindeks (5 numbrit): ")
            ok, res = check_postcode(code)
            if not ok:
                print(res)
            else:
                region, special = res
                print("Maakond:", region)
                print(special)
        elif choice == '5':
            s = input("Sisesta elementide loend komadega (min 2): ")
            lst = [x.strip() for x in s.split(',') if x.strip()!='']
            try:
                pairs = int(input("Mitu paari vahetada? "))
            except ValueError:
                pairs = 1
            print("Tulemus:", swap_pairs(lst, pairs))
        elif choice == '6':
            s = input("Sisesta arvud komadega: ")
            nums = [float(x.strip()) for x in s.split(',') if x.strip()]
            print("Tulemus:", replace_max_with_division(nums))
        elif choice == '7':
            s = input("Sisesta arvud komadega: ")
            nums = [float(x.strip()) for x in s.split(',') if x.strip()]
            ordn = input("Sorteerimine kasvavalt või kahanevalt? (k/kah): ").strip().lower()
            rev = ordn.startswith('k') and ordn != 'kasvavalt'
            rev = (ordn == 'kahanevalt')
            print("Tulemus:", sort_by_abs(nums, reverse=rev))
        elif choice == '8':
            s = input("Sisesta sõnad komadega (näide: tamm,taevas,elevant): ")
            words = [x.strip() for x in s.split(',') if x.strip()]
            print(equalize_lengths(words))
        elif choice == '9':
            name = input("Sisesta nimi: ").strip()
            ok, info = name_check(name)
            if not ok:
                print(info)
            else:
                print(info['greeting'])
                print("Tähti:", info['letters'], "Täishäälikuid:", info['vowels'], "Kaashäälikuid:", info['consonants'])
                print("Unikaalsed tähed tähestikulises järjekorras:", info['unique_sorted'])
        elif choice == '10':
            # lihtne demo: küsime 3 töötajat
            employees = []
            for i in range(3):
                name = input(f"Töötaja {i+1} nimi: ").strip()
                salary = float(input(f"{name} palk: "))
                age = int(input(f"{name} vanus: "))
                employees.append({'name':name,'salary':salary,'age':age})
            stats = employees_stats(employees)
            print("Suurima palgaga töötaja(t):")
            for e in stats['max_salary_employees']:
                print(e)
            print("Keskmine palk:", stats['avg_salary'])
            print("Mitu teenib üle keskmise:", stats['count_over_avg'])
            print("Keskmine vanus ≤ keskmine palk:", stats['avg_age_le_avg_salary'])
            print("Keskmine vanus > keskmine palk:", stats['avg_age_gt_avg_salary'])
        elif choice == '11':
            letters, repeated = english_alphabets()
            print("Tähed:", letters)
            print("Korduvad:", repeated[:10])  # näita esimest 10
        elif choice == '12':
            lst, mn, mx = swap_min_max_random()
            print("Pärast vahetust:", lst)
        elif choice == '13':
            guess_word_game()
        elif choice == '14':
            european_capitals()
        elif choice == '15':
            nums, est_s, eng_s, ita_s, tre_exists = simple_dict()
            print("Tabel (näide):")
            for i in range(len(nums)):
                print(f"{nums[i]} - {est_s[i] if i < len(est_s) else ''} - {eng_s[i] if i < len(eng_s) else ''} - {ita_s[i] if i < len(ita_s) else ''}")
            print("'tre' olemas itaalia listis?", tre_exists)
        elif choice == '16':
            q = input("Esita oma küsimus: ")
            print("Vastus:", magic_8ball(q))
        else:
            print("Valik tundmatu. Proovi uuesti.")

if __name__ == "__main__":
    main_menu()

