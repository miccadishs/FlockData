from django.db import models
from django.contrib.auth.models import User
from datetime import date


# Create your models here.
class Breed(models.Model):
    breedType = models.ForeignKey('BreedType', on_delete=models.PROTECT, default=1, blank=True)
    breed_name = models.CharField(max_length=200, blank=True, null=True)
    target = models.ForeignKey('Target', on_delete=models.PROTECT)

    @property
    def get_expected_eggs(self):
        breed_flocks = self.flock_set.all()
        for i in breed_flocks:
            print(i)
        all_flock_records_eggs = [] # getting the total eggs for all flocks
        all_flocks_expected_eggs =[]
        for flock in breed_flocks:
            record = Record.objects.filter(flock=flock.id).order_by('date').last()
            eggs_produced = 0
            all_flocks_expected_eggs.append(int(flock.expected_eggs))


            if record != None:
                if record.eggs_produced is None:
                    all_flock_records_eggs.append(0)
                else:
                    all_flock_records_eggs.append(int(record.eggs_produced))
            else:
                continue


        total_latest_flock_eggs = sum(all_flock_records_eggs)
        total_flock_expected_eggs = sum(all_flocks_expected_eggs)

        breed_info = {
            'breed_eggs_produced':total_latest_flock_eggs,
            'breed_expected_eggs':total_flock_expected_eggs,
        }

        return breed_info

    def __str__(self):
        return str(self.breed_name)


class BreedType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


class Owner(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name


class Adjustment(models.Model):
    adjust_choices = [('birds', 'birds'), ('eggs', 'eggs'), ('feed', 'feed')]
    date = models.DateField(null=True, blank=True)
    flock = models.ForeignKey('Flock', on_delete=models.PROTECT, null=True)
    quantity = models.FloatField()
    adjustment = models.CharField(max_length=150, choices=adjust_choices, null=True, default="open")
    notes = models.CharField(max_length=500)


    def __str__(self):
        return self.flock.name


class Farm(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    farm_attendant = models.ForeignKey('FarmAttendent', on_delete=models.PROTECT, null=True, blank=True, default=1)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=200)
    farm = models.ForeignKey(Farm, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Flock(models.Model):
    status_choices = [('open', 'open'), ('closed', 'closed')]
    house = models.ForeignKey('House', on_delete=models.CASCADE, null=True)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    flock_id = models.CharField(max_length=200, default="Default")
    stage = models.CharField(max_length=75)
    name = models.CharField(max_length=75)
    date_hatched = models.DateField()
    date_in = models.DateField()
    date_out = models.DateField(null=True)
    birds_placed = models.IntegerField()
    status = models.CharField(max_length=150, choices=status_choices, null=True, default="open")

    def __str__(self):
        return self.name

    @property
    def get_flock_age(self):

        today = date.today()
        records = Record.objects.all()
        record = Record.objects.filter(flock=self.id).last()
        print(f'flock -> {self.name}. record-exists -> { records.exists() }. ')

        print(f'record -> {record}')
        if record is None:
            print('record returned None')
            return None
        elif record.date:
            current_record_date = record.date
            print(f'currrent-record-date -> { current_record_date }')
            age =  (abs(current_record_date - self.date_hatched).days) // 7
            return age
        else:
            return None

    @property
    def get_flock_size (self):
        records = Record.objects.filter(flock=self.id)

        death_mortality = []
        death_culls = []

        for record in records:
            if record.deaths_mortality is None :
                death_mortality.append(0)
            else:
                death_mortality.append(record.deaths_mortality)
            if record.deaths_culls is None:
                death_culls.append(0)
            else:
                death_culls.append(record.deaths_culls)

        # print(f'death mortality -> {death_mortality}')
        # print(f'death culls -> {death_culls}')

        return int(self.birds_placed) - (sum(death_culls) + sum(death_mortality))

    @property
    def flock_performence(self):
        last_record = Record.objects.filter(flock=self.id).last()
        eggs_produced = last_record.eggs_produced

    @property
    def expected_eggs(self):

        breed = str(self.breed)
        expected_eggs = 0

        if 'Sasso' in breed:
            breed = 'Sasso'

        breed_max_week = int(TargetDetails.objects.filter(target__name=breed).last().name)
        breed_min_week = int(TargetDetails.objects.filter(target__name=breed).first().name)

        print(f'breed max week-> { breed_max_week }')
        print(f'breed min week-> {breed_min_week}')

        flock_age = self.get_flock_age

        if flock_age is None:
            return expected_eggs

        else:

            if flock_age > breed_max_week:
                return expected_eggs
            if flock_age < breed_min_week:
                return expected_eggs
            else:
                if 'Sasso' in breed:
                    breed = "Sasso"

                print(f'the breed is {breed}')
                print(f'the flock age is: {self.get_flock_age}')

                targets = TargetDetails.objects.get(target__name=breed, name=self.get_flock_age)

                if targets == None:
                    expected_eggs = 0
                else:
                    expected_eggs = targets.lay_rate * self.get_flock_size / 100
                return expected_eggs

    @property
    def eggs_produced(self):

        breed = str(self.breed)
        breed_max_week = int(TargetDetails.objects.filter(target__name=breed).last().name)
        breed_min_week = int(TargetDetails.objects.filter(target__name=breed).first().name)

        eggs_produced = 0
        if self.get_flock_age > breed_max_week:
            return eggs_produced

        breed = str(self.breed)
        record = Record.objects.filter(flock=self.id).last()
        eggs_produced = record.eggs_produced

        return eggs_produced


class House(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True, default=1)
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class Record(models.Model):
    bird_uniformity_choices = [('uniform', 'uniform'), ('un-uniform', 'un-uniform')]
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    deaths_mortality = models.IntegerField(null=True, blank=True)
    deaths_culls = models.IntegerField(null=True, blank=True)
    body_weight = models.FloatField(null=True, blank=True)
    body_uniformity = models.CharField(max_length=150, choices=bird_uniformity_choices, null=True)
    feed_consumed = models.FloatField(null=True, blank=True)
    feed_delivered = models.FloatField(null=True, blank=True)
    feed_formula = models.ForeignKey('FeedFormula', on_delete=models.CASCADE, null=True, blank=True)
    water_consumed = models.FloatField(null=True, blank=True)
    temperature_inside = models.FloatField(null=True, blank=True)
    eggs_produced = models.IntegerField(null=True, blank=True)
    eggs_broken = models.FloatField(null=True, blank=True)
    eggs_sold = models.IntegerField(null=True, blank=True)
    egg_weight = models.FloatField(null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.flock)



class Target(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class TargetDetails(models.Model):
    name = models.CharField(max_length=200, null=True)
    target = models.ForeignKey(Target, on_delete=models.PROTECT, default=1)
    body_weight = models.FloatField(null=True)
    body_uniform = models.CharField(max_length=10, null=True)
    feed_rate = models.IntegerField(null=True)
    feed_formula = models.CharField(max_length=75, null=True)
    water_rate = models.CharField(max_length=75, null=True)
    lay_rate = models.FloatField(null=True)
    liveability = models.FloatField(null=True)
    death_mortality = models.FloatField(null=True)
    egg_weight = models.FloatField(null=True)
    age_week = models.IntegerField(null=True)
    age_daily = models.IntegerField(null=True)

    def __str__(self):
        return str(self.target)


class Vaccination(models.Model):
    flock = models.ForeignKey(Flock, on_delete=models.CASCADE, null=True)
    vaccine = models.ForeignKey("Vaccine", on_delete=models.PROTECT, null=True, default=1)
    date = models.DateField(null=True)
    date_expiration = models.DateField(null=True)

    def __str__(self):
        return str(self.flock)


class Vaccine(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=75)
    method = models.CharField(max_length=75)

    def __str__(self):
        return self.name


class FeedFormula(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class FarmAttendent(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    uid = models.CharField(max_length=250)

    def __str__(self):
        return self.name
