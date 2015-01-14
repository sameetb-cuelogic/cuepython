
# -*- coding: utf-8 -*-

class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # the parameters are received as tuples, example: ('verb', 'go')
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    word_type = None

    if word_list:
        word = word_list[0]
        word_type = word[0]

    return word_type


def match(word_list, expected_type):
    matched_word = None

    if word_list:
        word = word_list.pop(0)

        if word[0] == expected_type:
            matched_word = word

    return matched_word


def skip(word_list, skip_type):
    while peek(word_list) == skip_type:
        match(word_list, skip_type)


def parse_subject(word_list):
    subject = None
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "noun":
        subject = (match(word_list, "noun"))
    elif next_word == "verb":
        subject = ("noun", "player")
    else:
        raise ParserError("Expecting a noun or verb next")

    return subject


def parse_verb(word_list):
    verb = None
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "verb":
        verb = (match(word_list, "verb"))
    else:
        raise ParserError("Expecting a verb next")

    return verb


def parse_object(word_list):
    obj = None
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "noun":
        obj = (match(word_list, "noun"))
    elif next_word == "direction":
        obj = (match(word_list, "direction"))
    else:
        raise ParserError("Expecting a noun or direction next")

    return obj


def parse_sentence(word_list):
    subject = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subject, verb, obj)
