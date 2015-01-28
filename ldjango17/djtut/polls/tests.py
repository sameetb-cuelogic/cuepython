import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_for_future_date(self):
        """
        test_was_published_recently() should return False if the question was published
        on a future date
        """
        future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
        self.assertEqual(future_question.was_published_recently(), False)

    def test_was_published_recently_for_old_question(self):
        """
        test_was_published_recently() should return False if the question was published
        on a past date more than 1 day before
        """
        old_question = Question(pub_date=timezone.now() - datetime.timedelta(days=30))
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_for_recent_question(self):
        """
        test_was_published_recently() should return True if the question was published
        in the last 1 day
        """
        recent_question = Question(pub_date=timezone.now() - datetime.timedelta(hours=1))
        self.assertEqual(recent_question.was_published_recently(), True)


def create_question(question_text, days):
    """
    Creates a question with the given `question_text` published the given
    number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    return Question.objects.create(question_text=question_text,
                                   pub_date=(timezone.now() + datetime.timedelta(days=days)))


class QuestionViewTests(TestCase):

    def test_index_view_with_no_questions(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_index_view_with_a_past_question(self):
        """
        Questions with a pub_date in the past should be displayed on the
        index page
        """
        create_question("Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question>']
        )

    def test_index_view_with_a_future_question(self):
        """
        Questions with a pub_date in the future should not be displayed on
        the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_questions'], [])

    def test_index_view_with_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        should be displayed.
        """
        create_question("Past question", days=-30)
        create_question("Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question>']
        )

    def test_index_view_with_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_question("Past question 1", days=-10)
        create_question("Past question 2", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_questions'],
            ['<Question: Past question 2>', '<Question: Past question 1>']
        )


class QuestionIndexDetailTests(TestCase):

    def test_detail_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        question = create_question("Future question", days=10)
        response = self.client.get(reverse('polls:detail', args=(question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_detail_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse('polls:detail', args=(question.id,)))
        self.assertContains(response, text=question.question_text, status_code=200)


class QuestionIndexResultsTests(TestCase):

    def test_results_view_with_a_future_question(self):
        """
        The detail view of a question with a pub_date in the future should
        return a 404 not found.
        """
        question = create_question("Future question", days=10)
        response = self.client.get(reverse('polls:results', args=(question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_results_view_with_a_past_question(self):
        """
        The detail view of a question with a pub_date in the past should
        display the question's text.
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse('polls:results', args=(question.id,)))
        self.assertContains(response, text=question.question_text, status_code=200)

