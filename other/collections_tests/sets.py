drama_series_codes = [1234, 5678]
horror_series_codes = [1010, 1234]

all_series = []
all_series.extend(drama_series_codes)
all_series.extend(horror_series_codes)
print(all_series) # print [1234, 5678, 1010, 1234] // 1234 twice
all_series = set(all_series)
print(all_series) # print {1234, 1010, 5678} // no duplicates 
print(set(drama_series_codes) | set(horror_series_codes)) # print the union of sets 
print(set(drama_series_codes) & set(horror_series_codes)) # print the interserction of sets
print(set(drama_series_codes) - set(horror_series_codes)) # print the diff between two sets
print(set(horror_series_codes) - set(drama_series_codes)) #  print the diff between two sets
print(set(drama_series_codes) ^ set(horror_series_codes)) # print exclusive or (xor)

all_series.add(2221)
all_series = frozenset(all_series)
print(all_series)

for serie in all_series:
    print(serie)
# cannot add to frozenset
# all_series.add(2222) # raise AttributeError