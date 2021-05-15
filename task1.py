def func(name, **kwargs):
    print(name)
    for key, value in kwargs.items():
        print(f'{key}-{value}')

print(func(name='USA', population='330 million', is_democratic=True))
print(func(name='Kyrgyzstan', area='200 km2',have_borders_with=['Kazakhstan', 'Uzbekistan', 'Tajikistan', 'China']))


