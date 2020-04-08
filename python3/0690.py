from typing import List


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        n = len(employees)
        d = {}  # id:pos
        if n == 0:
            return False
        for employee in employees:
            d[employee.id] = employee

        def getsubImportance(id):
            person = d.get(id)
            subs = person.subordinates
            subImportance = 0
            for id in subs:
                subImportance += getsubImportance(id)
            return person.importance+subImportance

        return getsubImportance(id)
