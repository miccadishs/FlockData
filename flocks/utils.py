from .models import *

def farm_allert_list(flock):

    flock = Flock.objects.get(name=flock)
    breed = str(flock.breed)

    if 'Sasso' in breed:
        breed="Sasso"

    print(f'the breed is { breed }')
    print(f'the flock age is: {flock.get_flock_age}')

    targets = TargetDetails.objects.get(target__name=breed, name=flock.get_flock_age) or None

    if targets is None:
        return 'no data available '

    expected_eggs = targets.lay_rate

    return expected_eggs

    #MAIN A&B 20-12




