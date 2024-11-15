import random, string
open('./items/' + ''.join(random.choices(string.ascii_lowercase, k=5)) + ".txt", 'w').close()
