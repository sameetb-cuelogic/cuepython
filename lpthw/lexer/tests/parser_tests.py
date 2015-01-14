
from nose.tools import *
from lexer import parser

def test_subject_object_noun():
    sentence = parser.parse_sentence([("stop", "the"), ("noun", "bear"), ("verb", "eat"), ("stop", "the"), ("noun", "princess")])

    assert_equal(sentence.subject, "bear")
    assert_equal(sentence.verb, "eat")
    assert_equal(sentence.object, "princess")


def test_subject_none_object_direction():
    sentence = parser.parse_sentence([("verb", "go"),
                                      ("stop", "from"),
                                      ("stop", "the"),
                                      ("direction", "north")])

    assert_equal(sentence.subject, "player")
    assert_equal(sentence.verb, "go")
    assert_equal(sentence.object, "north")


def test_subject_exception():
    assert_raises(parser.ParserError, parser.parse_sentence, [("error", "error"),
                                                              ("verb", "eat"),
                                                              ("noun", "princess")])


def test_verb_expection():
    assert_raises(parser.ParserError, parser.parse_sentence, [("noun", "bear"),
                                                              ("error", "error"),
                                                              ("noun", "princess")])


def test_object_exception():
    assert_raises(parser.ParserError, parser.parse_sentence, [("noun", "bear"),
                                                              ("verb", "eat"),
                                                              ("error", "error")])
