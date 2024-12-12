#a
slownik = {
    'Marek' : 123456789,
    'Patryk' : 987654321,
    'Marcin' : 123123123,
    'Marysia' : 12344567
}

def print_phone_numbers(slownik):
    for x in slownik:
        y = slownik[x]
        print(x, "ma numer", y)

print_phone_numbers(slownik)

#b
dni = {
    1 : 'Poniedziałek',
    2 : 'Wtorek',
    3 : 'Środa',
    4 : 'Czwatek',
    5 : 'Piątek',
    6 : 'Sobota',
    7 : 'Niedziela'
}

days = {
     1 : 'Monday',
     2 : 'Tuesday',
     3 : 'Wednesday',
     4 : 'Thursday',
     5 : 'Friday',
     6 : 'Saturday',
     7 : 'Sunday'
}


def pol_to_ang(dni,days):
    for x in dni:
        day = days.get(x)
        dni[x] = day
    return dni

print(pol_to_ang(dni, days))

def ang_to_pol(days,dni):
    for x in days:
        dzien = dni.get(x)
        days[x] = dzien
    return days

print(ang_to_pol(days, dni))

kalendarz = {
    'marzec',
    'październik',
    'styczeń',
    'grudzień',
    'listopad',
    'czerwiec',
    'lipiec',

}

k_slownik = {
    1: 'styczeń',
    2: 'luty',
    3: 'marzec',
    4: 'kwiecień',
    5: 'maj',
    6: 'czerwiec',
    7: 'lipiec',
    8: 'sierpień',
    9: 'wrzesień',
    10: 'październik',
    11: 'listopad',
    12: 'grudzień'
}

def sorting_kalendarz(kalendarz, k_slownik):
    for x in kalendarz:
        print(x)

print(sorting_kalendarz(kalendarz, k_slownik))


liczba = {
    I : 1,
    II : 2,
    III : 3,
    IV : 4,
    V : 5,
    VI : 6,
    VII : 7,
    VIII : 8,
    IX : 9,
    X : 10
}