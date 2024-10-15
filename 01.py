class HashTable:
    def __init__(self, size):
        # Ініціалізація хеш-таблиці з заданим розміром.
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        # Функція хешування для знаходження індексу ключа.
        return hash(key) % self.size

    def insert(self, key, value):
        # Вставка пари ключ-значення.
        key_hash = self.hash_function(key)  # Отримуємо хеш для ключа.
        key_value = [key, value]  # Створюємо пару ключ-значення.

        # Перевіряємо, чи є щось у цій позиції хеш-таблиці.
        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])  # Створюємо новий список з парою.
            return True
        else:
            # Якщо вже є пари, оновлюємо значення для ключа або додаємо новий запис.
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value  # Оновлюємо значення, якщо ключ вже існує.
                    return True
            self.table[key_hash].append(key_value)  # Додаємо нову пару, якщо ключа не було.
            return True

    def get(self, key):
        # Отримання значення за ключем.
        key_hash = self.hash_function(key)  # Отримуємо хеш ключа.
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]  # Повертаємо значення, якщо знайдено ключ.
        return None  # Повертаємо None, якщо ключ не знайдено.

    def delete(self, key):
        # Видалення пари ключ-значення за ключем.
        key_hash = self.hash_function(key)  # Отримуємо хеш ключа.
        if self.table[key_hash] is not None:
            for i in range(len(self.table[key_hash])):
                if self.table[key_hash][i][0] == key:
                    self.table[key_hash].pop(i)  # Видаляємо пару, якщо знайдено ключ.
                    return True
        return False  # Повертаємо False, якщо ключ не знайдено.

# Тестуємо нашу хеш-таблицю:
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print(H.get("apple"))   # Виведе: 10
H.delete("apple")  # Видаляємо ключ "apple"
print(H.get("apple"))   # Виведе: None, бо "apple" було видалено
