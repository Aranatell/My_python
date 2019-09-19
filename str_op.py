#work_with_stringsPepegaPhone
s='У лукоморья 123 дуб зеленый 456'
print(bool(s.find('я')))
print(s.count('у'))
if s.isalpha():
    print('True')
else:
    print(s.upper())
if len(s)>=4:
    print(s.lower())
print(s.replace(s[0],'О'))

