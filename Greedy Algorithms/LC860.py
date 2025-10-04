class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        gain = 0
        notes_5 = 0
        notes_10 = 0
        notes_20 = 0
        for i, e in enumerate(bills):
            if e == 5:
                notes_5 += 5
            if e == 10:
                notes_10 += 10
            if e == 20:
                notes_20 += 20

            return_notes = e - 5
            print(notes_5, notes_10, notes_20, return_notes)

            if return_notes == 5:
                notes_5 -= 5
            if return_notes == 15:
                notes_5 -= 5
                if notes_10 > 0:
                    notes_10 -= 10
                else:
                    notes_5 -= 2 * 5

            if notes_5 < 0:
                return False

        return True
