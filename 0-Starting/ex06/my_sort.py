d = {
    'Hendrix' : '1942',
    'Allman' : '1946',
    'King' : '1925',
    'Clapton' : '1945',
    'Johnson' : '1911',
    'Berry' : '1926',
    'Vaughan' : '1954',
    'Cooder' : '1947',
    'Page' : '1944',
    'Richards' : '1943',
    'Hammett' : '1962',
    'Cobain' : '1967',
    'Garcia' : '1942',
    'Beck' : '1944',
    'Santana' : '1947',
    'Ramone' : '1948',
    'White' : '1975',
    'Frusciante': '1970',
    'Thompson' : '1949',
    'Burton' : '1939',
}

def my_sort():
    sorted_years = {}
    for key, value in d.items():
        if value not in sorted_years:
            sorted_years[value] = [key]
        else:
            sorted_years[value].append(key)
    return sorted_years

def print_sorted_years(sorted_years):
    for year, names in sorted(sorted_years.items()):
        if len(names) > 1:
            print(f"{', '.join(sorted(names))}")
        else:
            print(f"{names[0]}")

if __name__ == "__main__":
    sorted_years = my_sort()
    if sorted_years:
        print_sorted_years(sorted_years)
