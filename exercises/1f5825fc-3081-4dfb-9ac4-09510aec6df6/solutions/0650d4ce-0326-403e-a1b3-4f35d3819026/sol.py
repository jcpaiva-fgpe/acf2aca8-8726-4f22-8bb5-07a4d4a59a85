class Sprendimas:
    def raidziu_kombinacijos(skaitmenys):
        if(len(skaitmenys) == 0):
            return []

        skaiciai_i_simbolius = {'1': '',     '2': 'abc', '3': 'def',
                      '4': 'ghi',  '5': 'jkl', '6': 'mno',
                      '7': 'pqrs', '8': 'tuv', '9': 'wxyz', '0': ''}

        resus = ['']

        for d in skaitmenys:
            tem = []
            for c in skaiciai_i_simbolius[d]:
                tem = tem + [r + c for r in resus]

            resus = tem
        return resus
Sprendimas.raidziu_kombinacijos("23")
