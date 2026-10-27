# Hooks

The hook is everything above "…see more". On a phone that is roughly **two
lines, about 110 characters**. If the hook does not land there, the post's
quality does not matter.

Write three hooks before writing the post. Use a different formula for each.

## The 20 formulas that fit this account

**Tension / contradiction**
1. `[Expected thing]. [Opposite thing that is true].`
   "Five bugs. None of them threw an error."
2. `The fix was [small]. The problem was [big].`
   "I got my token count wrong for weeks. The fix was two lines."
3. `Everyone says [X]. I measured [Y].`
4. `[Thing] looks broken. It is actually [real cause].`

**Number / specificity**
5. `[Big number] [things], and no way to [basic action].`
   "181 Claude Code skills on my machine, and no way to see which ones were actually on."
6. `[N] [things] in [time]. Here is what broke.`
7. `I spent [time] on [narrow thing]. It changed [larger thing].`
8. `[Metric] went from [a] to [b]. The change was [one line].`

**Contrarian / diagnosis**
9. `It's not [what they blame]. It's [what is actually wrong].`
   "It's not your taste. It's that nobody asked."
10. `[Common advice] is wrong for [specific case]. Here is the case.`
11. `You do not have a [tool] problem. You have a [contract] problem.`
12. `The expensive bug is the one that does not throw.`

**Story / build log**
13. `I got tired of [manual chore]. So I built [thing].`
    "I got tired of opening files by hand."
14. `[Outcome]. The part I keep thinking about is [detail].`
    "First prize at VIHANSA-2K26 … The prize wasn't the part I'm still thinking about."
15. `Took [place] at [event] I went into alone.`
16. `[Time period] ago I [state]. Today [state].` (only if true)

**Technical teardown**
17. `[System] does [surprising thing] on purpose. Here is why.`
18. `One line in [file] costs [cost].`
19. `[Protocol/API] says MUST. Our implementation said nothing.`
20. `The spec had [requirement]. The test suite checked [nothing].`

## Hook rules

- Put the most specific noun first. "Five merged PRs" beats "My open-source
  contributions".
- Never open with "I'm excited", "Thrilled", "Humbled", "Hot take", or a
  question.
- Numbers should be exact. "2,050 lines" not "over 2,000 lines".
- If the hook needs context from a previous post, it is not a hook.
- Test on a phone: if the value of the post is not visible before "see more",
  rewrite the hook.

## Re-hook

Line three, after the hook, should raise the stakes or name the mechanism:

```
Five bugs. None of them threw an error.

That was the pattern in every HarnessRouter issue I picked up this week —
and it is why I ended up fixing five of them.
```

The re-hook is where the reader decides to keep going. It should not repeat the
hook in different words.
