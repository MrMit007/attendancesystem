import cognitive_face as CF
from global_variables import personGroupId

Key = 'aeac52f65e1a44da90aaeeab84360441'
CF.Key.set(Key)

res = CF.person_group.get_status(personGroupId)
print res
