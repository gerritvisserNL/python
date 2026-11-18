# Python Training

Daily one-hour practice sessions, from junior to professional Python developer.

## Daily routine (60 min)

1. **Warm-up (5 min):** reread your teacher's feedback from the previous day.
2. **Exercises (45 min):** open `dayXX/exercises.py` and make the tests pass.
3. **Review (10 min):** ask your teacher for a review ("review dag X").
   You'll get feedback and the next day's exercises.

```bash
source .venv/bin/activate   # once per terminal session
pytest day01 -v             # run the tests for a day
```

## Curriculum

Speed adapts to your progress; these are estimates.

| Phase | Weeks | Topics |
|-------|-------|--------|
| 1. Fundamentals | 1-2 | Types, strings, lists/dicts/sets/tuples, control flow, functions, comprehensions |
| 2. Pythonic code | 3-4 | Unpacking, `enumerate`/`zip`, exceptions, files & `pathlib`, modules, `collections`, `itertools` |
| 3. Object-oriented | 5-6 | Classes, `dataclasses`, dunder methods, properties, composition vs inheritance |
| 4. Professional tooling | 7-8 | pytest in depth, type hints & mypy, ruff, virtual environments, packaging, git workflow |
| 5. Advanced Python | 9-10 | Iterators, generators, closures, decorators, context managers |
| 6. Real-world | 11-12 | JSON & HTTP APIs, CLI with `argparse`, SQLite, `asyncio` basics, final project |

Each week ends with a small project that combines what you learned.
