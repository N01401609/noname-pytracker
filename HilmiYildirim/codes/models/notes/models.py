from django.db import models


class User(models.Model):
    user_fname = models.CharField(max_length=200)
    user_lname = models.CharField(max_length=200)

    def __str__(self):
        return self.user_fname + " " + self.user_lname


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_color = models.CharField(max_length=200)
    note_card_width = models.CharField(max_length=200)
    note_card_height = models.CharField(max_length=200)
    note_title = models.CharField(max_length=200)
    note_text = models.CharField(max_length=200)
    note_position = models.CharField(max_length=200)

    def __str__(self):
        return self.note_title
