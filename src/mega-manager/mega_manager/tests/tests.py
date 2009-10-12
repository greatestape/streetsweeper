from django.test import TestCase

from mega_manager.tests.models import SportsLocker, Frisbee, RED, BLUE


class MegaManagerTestCase(TestCase):
    def setUp(self):
        self.sports_locker = SportsLocker.objects.create(
                owner='Bheel'
                )
        self.fancy_red_frisbee = Frisbee.objects.create(
                colour=RED,
                fancy=True,
                sports_locker=self.sports_locker,
                )
        self.normal_red_frisbee = Frisbee.objects.create(
                colour=RED,
                fancy=False,
                sports_locker=self.sports_locker
                )
        self.fancy_blue_frisbee = Frisbee.objects.create(
                colour=BLUE,
                fancy=True,
                sports_locker=self.sports_locker
                )

    def testDefaultQuery(self):
        qs = Frisbee.objects.all()
        self.assertEqual(
                set([frisbee.id for frisbee in qs]),
                set([self.fancy_red_frisbee.id, self.normal_red_frisbee.id, self.fancy_blue_frisbee.id])
                )

    def testCustomManagerMethod(self):
        qs = Frisbee.objects.fancy()
        self.assertEqual(
                set([frisbee.id for frisbee in qs]),
                set([self.fancy_red_frisbee.id, self.fancy_blue_frisbee.id])
                )

    def testStackedCustomManagerMethods(self):
        qs = Frisbee.objects.fancy().blue()
        self.assertEqual(
                set([frisbee.id for frisbee in qs]),
                set([self.fancy_blue_frisbee.id])
                )

    def testDefaultQueryOnRelatedManager(self):
        qs = self.sports_locker.frisbee_set.all()
        self.assertEqual(
                set([frisbee.id for frisbee in qs]),
                set([self.fancy_red_frisbee.id, self.normal_red_frisbee.id, self.fancy_blue_frisbee.id])
                )

    def testCustomManagerMethodOnRelatedManager(self):
        qs = self.sports_locker.frisbee_set.fancy()
        self.assertEqual(
                set([frisbee.id for frisbee in qs]),
                set([self.fancy_red_frisbee.id, self.fancy_blue_frisbee.id])
                )

    def testStackedCustomManagerMethodsOnRelatedManager(self):
        qs = self.sports_locker.frisbee_set.fancy().blue()
        self.assertEqual(
                set([frisbee.id for frisbee in qs]),
                set([self.fancy_blue_frisbee.id])
                )
