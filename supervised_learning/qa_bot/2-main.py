#!/usr/bin/env python3
# Forwarning, this will give warnings for all answers
# You can apparantly include a "-W ignore" before calling the script
# So that's something I might try

answer_loop = __import__('2-qa').answer_loop

with open('ZendeskArticles/PeerLearningDays.md') as f:
    reference = f.read()

answer_loop(reference)