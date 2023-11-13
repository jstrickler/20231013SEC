
print('26\u00B0')  # Use \uXXXX where XXXX is the Unicode value in hex
print(r'26\u00B0\n')  # unicode is not evaluated in raw strings

print('we spent \u20ac1.23M for an original C\u00e9zanne')
print("Romance in F\u266F Major")
print()

print("\u0928\u092e\u0938\u094d\u0924\u0947\u0020\u0926\u0941\u0928\u093f\u092f\u093e!") # hindi
print("\u4f60\u597d\u4e16\u754c!") # chinese
print("\u0417\u0434\u0440\u0430\u0432\u0435\u0439\u0020\u0441\u0432\u044f\u0442!") # bulgarian
print("\u00a1\u0048\u006f\u006c\u0061\u0020\u004d\u0075\u006e\u0064\u006f\u0021") # spanish
print("!\u0645\u0631\u062d\u0628\u0627\u0020\u0628\u0627\u0644\u0639\u0627\u0644\u0645") # arabic
print()

data = ['\U0001F95A', '\U0001F414']  # answers the age-old question (at least for Python)
print("unsorted:", data)
print("sorted:", sorted(data))
