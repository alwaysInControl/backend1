Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del Geeks['bag']
Geeks['address'] = 'Ibraimova 103'
Geeks['contacts'] = {
    'telephone': '+996 *** **-**-**',
    'Instagram': 'geeks_edu'
}
Geeks['courses'].append('UX/UI')
print(f'Total number of courses: {len(Geeks["courses"])}')
for key, value in Geeks.items():
    print(f'{key}: {value}')
