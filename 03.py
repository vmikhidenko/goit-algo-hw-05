import timeit

# Завантаження текстів
with open('стаття 1.txt', 'r', encoding='ISO-8859-1') as f1:
    text1 = f1.read()

with open('стаття 2.txt', 'r', encoding='ISO-8859-1') as f2:
    text2 = f2.read()

# Алгоритм Бойєра-Мура
def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1

    # Створюємо таблицю зсувів
    shift = {char: m for char in set(text)}
    for i in range(m - 1):
        shift[pattern[i]] = m - i - 1

    i = m - 1
    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += shift.get(text[i], m)
    
    return -1

# Алгоритм Кнута-Морріса-Пратта (КМП)
def kmp_search(text, pattern):
    def compute_prefix_function(pattern):
        m = len(pattern)
        pi = [0] * m
        k = 0
        for q in range(1, m):
            while k > 0 and pattern[k] != pattern[q]:
                k = pi[k - 1]
            if pattern[k] == pattern[q]:
                k += 1
            pi[q] = k
        return pi

    n = len(text)
    m = len(pattern)
    pi = compute_prefix_function(pattern)
    q = 0
    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            return i - m + 1
            q = pi[q - 1]
    return -1

# Алгоритм Рабіна-Карпа
def rabin_karp_search(text, pattern, d=256, q=101):
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s + m] == pattern:
                return s
        if s < n - m:
            t = (t - h * ord(text[s])) % q
            t = (t * d + ord(text[s + m])) % q
            t = (t + q) % q
    return -1

# Вибір існуючого та вигаданого підрядків
existing_substring = "алгоритм"
non_existing_substring = "вигаданийпідрядок"

# Вимірювання часу виконання за допомогою timeit
def measure_time(text, substring, algorithm):
    timer = timeit.timeit(lambda: algorithm(text, substring), number=1000)
    return timer

# Результати для статті 1
print("Стаття 1 (існуючий підрядок): ")
print("Бойєр-Мур:", measure_time(text1, existing_substring, boyer_moore_search))
print("КМП:", measure_time(text1, existing_substring, kmp_search))
print("Рабін-Карп:", measure_time(text1, existing_substring, rabin_karp_search))

print("Стаття 1 (вигаданий підрядок):")
print("Бойєр-Мур:", measure_time(text1, non_existing_substring, boyer_moore_search))
print("КМП:", measure_time(text1, non_existing_substring, kmp_search))
print("Рабін-Карп:", measure_time(text1, non_existing_substring, rabin_karp_search))

# Результати для статті 2
print("Стаття 2 (існуючий підрядок): ")
print("Бойєр-Мур:", measure_time(text2, existing_substring, boyer_moore_search))
print("КМП:", measure_time(text2, existing_substring, kmp_search))
print("Рабін-Карп:", measure_time(text2, existing_substring, rabin_karp_search))

print("Стаття 2 (вигаданий підрядок): ")
print("Бойєр-Мур:", measure_time(text2, non_existing_substring, boyer_moore_search))
print("КМП:", measure_time(text2, non_existing_substring, kmp_search))
print("Рабін-Карп:", measure_time(text2, non_existing_substring, rabin_karp_search))
