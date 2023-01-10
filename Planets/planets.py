from collections import defaultdict

def energy_calc(arr1, arr2):
    orbit_dict = defaultdict(int)
    enrg_ctr = 0
    for planet in arr2:
        orbit_dict[planet] += 1
    
    orbit_ctr = orbit_dict.values()
    
    for val in orbit_ctr:
        if val > arr1[1]:
            enrg_ctr += arr1[1]
        else:
            enrg_ctr += val
            
    print(enrg_ctr)

rng = int(input())

for i in range(rng):
    
    arr1 = list(map(int, input().split(" ")))
    arr2 = list(map(int, input().split(" ")))

    energy_calc(arr1, arr2)
